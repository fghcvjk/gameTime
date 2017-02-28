# -*- coding:utf-8 -*-

from str_define import *

class Game(object):

    def __init__(self, name, path, num, allTime, server, isStart = False):
        self.server = server
        try:
            self.name = name.decode(USE_CODE)
            self.path = path.decode(USE_CODE)
        except:
            self.name = name.decode(WINDOWS_CODE)
            self.path = path.decode(WINDOWS_CODE)
        self.num = num

        self.isStart = isStart
        self.tickTime = server.getTimestamp() #上次统计时间
        self.playTime = 0 #本次在线时间
        self.allTime = allTime #总在线时间

        self.date2time = {} #每日时间

