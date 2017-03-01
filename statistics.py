# -*- coding:utf-8 -*-

import os
import psutil
import threading

import time
import datetime

import copy
import codecs

from game import Game
from str_define import *

class GameStatistics(object):

    def __init__(self, isStartServer = True, Form = None):
        self.num2game = {} #编号到游戏映射
        self.waitSaveGames = [] #等待存盘的游戏
        self.runGameList = [] #正在运行的游戏
        self.isStartServer = isStartServer
        self.Form = Form
        self.maxNum = 0
        self.initGameTime()

        #定时活动相关
        self.lastUpTime = 0
        self.lastOnSaveTime = 0
        self.lastSaveTime = 0
        # self.onTickList = [] #添加的定时活动
        if self.isStartServer:
            self.onTick()

    def onTick(self):
        timestamp = self.getTimestamp()

        if timestamp - self.lastUpTime > UP_ONLINE_TIME:
            self.upTime()
            self.lastUpTime = timestamp
        if timestamp - self.lastOnSaveTime > AUTO_SAVE_TIME:
            self.onSaveTime()
            self.lastOnSaveTime = timestamp
        if timestamp - self.lastSaveTime > SAVE_TIME:
            self.saveTime()
            self.lastSaveTime = timestamp

        # for tickAction in self.onTickList:
            # if timestamp - tickAction['lastTime'] > tickAction['time']:
                # tickAction['action']()

        if self.isStartServer:
            action = threading.Timer(0.1, self.onTick)
            action.start()

    # def addTick(self, action, time):
        # self.onTickList.append({'action':action, 'time':time, 'lastTime':0})

    def initGameTime(self):
        try:
            gameListFile = codecs.open(GAME_LIST_FILE, 'r')
            systemData = gameListFile.readlines()
        except:
            return
        gameNumList = eval(systemData[0])
        self.maxNum = int(systemData[1])
        for num in gameNumList:
            gameDataFile = codecs.open(GAME_DATA_FILE%(num), 'r')
            data = gameDataFile.readline()
            gameData = eval(data)
            num= gameData['num']
            game = Game(gameData['name'], gameData['path'], num, gameData['time'], self, isStart = True)
            self.num2game[num] = game

    def addGame(self, name, path): #添加游戏
        num = self.maxNum + 1
        self.maxNum = num
        try:
            gameDataFile = codecs.open(GAME_DATA_FILE%(num), 'r', )
            gameData = gameDataFile.readlines()
            if not gameData:
                gameData = ['\n']
        except:
            gameData = ['\n']
        gameData[0] = GAME_DATA_HEAD%(name, path, 0, num)
        gameDataFile = codecs.open(GAME_DATA_FILE%(num), 'w')
        gameDataFile.writelines(gameData)
        try:
            gameListFile = codecs.open(GAME_LIST_FILE, 'r')
            systemData = gameListFile.readlines()
            if not systemData:
                 systemData = [u'[]\n', u'\n']
        except:
            systemData = [u'[]\n', u'\n']
        gameNumList = eval(systemData[0])
        gameNumList.append(num)
        systemData[0] = SYSTEM_DATA_HEAD%gameNumList
        systemData[1] = SYSTEM_DATA_HEAD%self.maxNum
        gameListFile = codecs.open(GAME_LIST_FILE, 'w')
        gameListFile.writelines(systemData)
        game = Game(name, path, num, 0, self)
        self.num2game[num] = game

    def removeGame(self, num):
        if num in self.num2game:
            del self.num2game[num]
        os.remove(GAME_DATA_FILE%(num))
        gameListFile = codecs.open(GAME_LIST_FILE, 'r')
        systemData = gameListFile.readlines()
        gameNumList = eval(systemData[0])
        gameNumList.remove(int(num))
        systemData[0] = SYSTEM_DATA_HEAD%gameNumList
        gameListFile = codecs.open(GAME_LIST_FILE, 'w')
        gameListFile.writelines(systemData)

    def getTimestamp(self):
        return int(time.time() * 1000)

    def getDatetime(self):
        return str(datetime.date.today())

    def getPrintTime(self, playTime):
        playTime = playTime / 1000
        d = int(playTime / 60 / 60 / 24)
        playTime -= d * 24 * 60 * 60
        h = int(playTime / 60 / 60)
        playTime -= h * 60 * 60
        m = int(playTime / 60)
        playTime -= m * 60
        s = int(playTime)
        return d, h, m, s

    def getAllActionExe(self): #获得所有在运行的exe
        exeLists = []
        pidList = psutil.pids()

        for pid in pidList:
            try:
                exeLists.append(unicode(psutil.Process(pid).exe(), WINDOWS_CODE))
            except:
                pass
        # for exe in exeLists:
            # print 'exe name:', exe
        return exeLists

    def upTime(self): #更新时间
        exeLists = self.getAllActionExe()
        upTimestamp = self.getTimestamp()
        for game in self.num2game.values():
            print 'game path:', game.path
            if game.path in exeLists:
                if game.num not in self.runGameList:
                    self.runGameList.append(game.num)
                if game.isStart:
                    game.playTime += upTimestamp - game.tickTime
                    game.allTime += upTimestamp - game.tickTime
                    print game.name
                    d, h, m, s = self.getPrintTime(game.playTime)
                    str = '本次运行：%s小时%s分%s秒'%(h, m, s)
                    print str.decode(USE_CODE)
                    d, h, m, s = self.getPrintTime(game.allTime)
                    str = '总共运行：%s天%s小时%s分%s秒'%(d, h, m, s)
                    print str.decode(USE_CODE)
                    print '-------------------------------------------'
                else:
                    game.isStart = True
                    game.tickTime = self.getTimestamp()
                game.tickTime = upTimestamp
            else:
                if game.num in self.runGameList:
                    self.runGameList.remove(game.num)
                self.trySaveTime(game.num)
                game.isStart = False
                game.tickTime = 0
                game.playTime = 0

    def onSaveTime(self):
        self.waitSaveGames.extend(self.num2game.keys())

    def trySaveTime(self, num = None):
        self.waitSaveGames.append(num)

    def saveTime(self): #保存
        saveList = copy.deepcopy(self.waitSaveGames)
        for num in saveList:
            if num in self.num2game:
                try:
                    game = self.num2game[num]
                    gameDataFile = codecs.open(GAME_DATA_FILE%(num), 'r')
                    gameData = gameDataFile.readlines()
                    gameData[0] = GAME_DATA_HEAD%(game.name, game.path, int(game.allTime), game.num)
                    #每日记录
                    gameDataFile = codecs.open(GAME_DATA_FILE%(num), 'w')
                    gameDataFile.writelines(gameData)
                    self.waitSaveGames.remove(num)
                except:
                    pass

    def onExit(self):
        #退出保存
        for num in self.num2game.keys():
            game = self.num2game[num]
            gameDataFile = codecs.open(GAME_DATA_FILE%(num), 'r')
            gameData = gameDataFile.readlines()
            gameData[0] = GAME_DATA_HEAD%(game.name, game.path, int(game.allTime), game.num)
            #每日记录
            gameDataFile = codecs.open(GAME_DATA_FILE%(num), 'w')
            gameDataFile.writelines(gameData)
        self.isStartServer = False

