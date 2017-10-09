# -*- coding:utf-8 -*-

import os
import psutil
import threading
from nt import chdir

import time
import datetime

import copy
import codecs
import zipfile

from game import Game
from str_define import *

class GameStatistics(object):

    def __init__(self, isStartServer = True, form = None):
        self.num2game = {} #编号到游戏映射
        self.waitSaveGames = [] #等待存盘的游戏
        self.runGameList = [] #正在运行的游戏
        self.rmList = [] #等待移除的游戏
        self.addList = [] #等待添加的游戏
        self.isStartServer = isStartServer
        self.isNormalRun = 0 #上次是否正常关闭
        self.form = form
        self.maxNum = 0
        self.initGameTime()
        self.backPackData()

        #定时活动相关
        self.lastUpTime = 0
        self.lastOnSaveTime = 0
        self.lastSaveTime = 0
        # if self.isStartServer:
            # self.onTick()

    def onTick(self):
        if self.isStartServer:
            timestamp = self.getTimestamp()
            addList = copy.deepcopy(self.addList)
            for addData in addList:
                self.addGame(addData['name'], addData['path'])
                self.addList.remove(addData)
            rmList = copy.deepcopy(self.rmList) 
            for num in rmList:
                self.removeGame(num)
                self.rmList.remove(num)

            if timestamp - self.lastUpTime > UP_ONLINE_TIME:
                self.upTime()
                self.lastUpTime = timestamp
            if timestamp - self.lastOnSaveTime > AUTO_SAVE_TIME:
                self.onSaveTime()
                self.lastOnSaveTime = timestamp
            if timestamp - self.lastSaveTime > SAVE_TIME:
                self.saveTime()
                self.lastSaveTime = timestamp

            # action = threading.Timer(0.1, self.onTick)
            # action.start()

    def initGameTime(self):
        if not os.path.exists(GAME_DATA_PATH):
            os.makedirs(GAME_DATA_PATH)
        try:
            gameListFile = codecs.open(GAME_LIST_FILE, 'r')
            systemData = gameListFile.readlines()
        except:
            self.isNormalRun = 1
            return
        gameNumList = eval(systemData[0])
        self.maxNum = int(systemData[1])
        self.isNormalRun = int(systemData[2])
        for num in gameNumList:
            gameDataFile = codecs.open(GAME_DATA_FILE%(num), 'r')
            data = gameDataFile.readline()
            gameData = eval(data)
            num= gameData['num']
            game = Game(gameData['name'], gameData['path'], num, gameData['time'], self, isStart = True)
            self.num2game[num] = game

    def backPackData(self):
        if self.isNormalRun:
            z = zipfile.ZipFile('backData.zip', 'w', zipfile.ZIP_DEFLATED)
            startdir = GAME_DATA_PATH
            for dirpath, dirnames, filenames in os.walk(startdir):
                for filename in filenames:
                    z.write(os.path.join(dirpath, filename))
            z.close()
        else:
            errorMessage = '程序未正常关闭，时间数据可能已被丢失，数据已备份在backData.zip中，请联系作者处理'.decode('utf-8')
            self.form.showErrorMessage(errorMessage)

    def tryAddGame(self, name, path):
        self.addList.append({'name':name, 'path':path})

    def addGame(self, name, path): #添加游戏
        num = self.maxNum + 1
        self.maxNum = num
        try:
            gameDataFile = codecs.open(GAME_DATA_FILE%(num), 'r', )
            gameData = gameDataFile.readlines()
            if not gameData:
                gameData = GAME_DATA_INIT_LIST
        except:
            gameData = GAME_DATA_INIT_LIST
        gameData[0] = GAME_DATA_HEAD%(name, path, 0, num)
        gameDataFile = codecs.open(GAME_DATA_FILE%(num), 'w')
        gameDataFile.writelines(gameData)
        try:
            gameListFile = codecs.open(GAME_LIST_FILE, 'r')
            systemData = gameListFile.readlines()
            if not systemData:
                 systemData = GAME_LIST_INIT_LIST
        except:
            systemData = GAME_LIST_INIT_LIST
        gameNumList = eval(systemData[0])
        gameNumList.append(num)
        systemData[0] = SYSTEM_DATA_HEAD%gameNumList
        systemData[1] = SYSTEM_DATA_HEAD%self.maxNum
        systemData[2] = SYSTEM_DATA_HEAD%self.isNormalRun
        gameListFile = codecs.open(GAME_LIST_FILE, 'w')
        gameListFile.writelines(systemData)
        game = Game(name, path, num, 0, self)
        self.num2game[num] = game

    def tryRemoveGame(self, num):
        self.rmList.append(num)

    def removeGame(self, num):
        num = int(num)
        if num in self.num2game:
            del self.num2game[num]
        if num in self.runGameList:
            self.runGameList.remove(num)
        os.remove(GAME_DATA_FILE%num)
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
        # d = int(playTime / 60 / 60 / 24)
        # playTime -= d * 24 * 60 * 60
        h = int(playTime / 60 / 60)
        playTime -= h * 60 * 60
        m = int(playTime / 60)
        playTime -= m * 60
        s = int(playTime)
        return h, m, s

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
            # print 'game path:', game.path
            if game.path in exeLists:
                if game.num not in self.runGameList:
                    self.runGameList.append(game.num)
                if game.isStart:
                    game.playTime += upTimestamp - game.tickTime
                    game.allTime += upTimestamp - game.tickTime
                    print game.name
                    h, m, s = self.getPrintTime(game.playTime)
                    str = '本次运行：%s小时%s分%s秒'%(h, m, s)
                    print str.decode(USE_CODE)
                    h, m, s = self.getPrintTime(game.allTime)
                    str = '总共运行：%s小时%s分%s秒'%(h, m, s)
                    print str.decode(USE_CODE)
                    print '-------------------------------------------'
                else:
                    game.isStart = True
                    game.tickTime = self.getTimestamp()
                game.tickTime = upTimestamp
            elif game.isStart:
                if game.num in self.runGameList:
                    self.runGameList.remove(game.num)
                self.trySaveTime(game.num)
                game.isStart = False
                game.tickTime = 0
                game.playTime = 0

    def onSaveTime(self):
        self.waitSaveGames.extend(self.runGameList)

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
        print 'onExit'
        for num in self.num2game.keys():
            game = self.num2game[num]
            gameDataFile = codecs.open(GAME_DATA_FILE%(num), 'r')
            gameData = gameDataFile.readlines()
            gameData[0] = GAME_DATA_HEAD%(game.name, game.path, int(game.allTime), game.num)
            #每日记录
            gameDataFile = codecs.open(GAME_DATA_FILE%(num), 'w')
            gameDataFile.writelines(gameData)
        self.isStartServer = False

        try:
            gameListFile = codecs.open(GAME_LIST_FILE, 'r')
            systemData = gameListFile.readlines()
            if not systemData:
                 systemData = GAME_LIST_INIT_LIST
        except:
            systemData = GAME_LIST_INIT_LIST
        gameNumList = eval(systemData[0])
        systemData[2] = SYSTEM_DATA_HEAD%self.isNormalRun
        gameListFile = codecs.open(GAME_LIST_FILE, 'w')
        gameListFile.writelines(systemData)

