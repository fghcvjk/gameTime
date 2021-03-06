# -*- coding:utf-8 -*-

import os
import win32api

from str_define import *

SPECIAL_STR = {u'\n': u'\\n', u'\t': u'\\t', u'\f': u'\\f', u'\r': u'\\r', u'\a': u'\\a', u'\b': u'\\b', u'\v': u'\\v', u'\0': u'\\0'}

class Game(object):

    def __init__(self, name, path, startPath, num, allTime, server, isStart = False):
        self.server = server
        self.num = num

        try:
            self.name = name.decode(USE_CODE)
            self.path = path.decode(USE_CODE)
            self.startPath = startPath.decode(USE_CODE)
        except:
            self.name = name.decode(WINDOWS_CODE)
            self.path = path.decode(WINDOWS_CODE)
            self.startPath = startPath.decode(USE_CODE)
        name = u''
        for index, str in enumerate(self.name):
            if str in SPECIAL_STR:
                name += SPECIAL_STR[str]
            else:
                name += str
        self.name = name
        path = u''
        for index, str in enumerate(self.path):
            if str in SPECIAL_STR:
                path += SPECIAL_STR[str]
            else:
                path += str
        self.path = path
        startPath = u''
        for index, str in enumerate(self.startPath):
            if str in SPECIAL_STR:
                startPath += SPECIAL_STR[str]
            else:
                startPath += str
        self.startPath = startPath

        self.isStart = isStart
        self.tickTime = server.getTimestamp() #上次统计时间
        self.playTime = 0 #本次在线时间
        self.allTime = allTime #总在线时间

        self.date2time = {} #每日时间

    def startGame(self):
        if self.num not in self.server.runGameList:
            if os.path.exists(self.startPath):
                win32api.ShellExecute(0, 'open', self.startPath, '','',1)
            else:
                errorMessage = '游戏路径不存在'.decode('utf-8')
                self.server.form.showErrorMessage(errorMessage)
        else:
            errorMessage = '此游戏已在运行中'.decode('utf-8')
            self.server.form.showErrorMessage(errorMessage)

