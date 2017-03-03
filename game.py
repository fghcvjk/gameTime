# -*- coding:utf-8 -*-

from str_define import *

SPECIAL_STR = {u'\n': u'\\n', u'\t': u'\\t', u'\f': u'\\f', u'\r': u'\\r', u'\r': u'\\r', u'\r': u'\\r', u'\r': u'\\r', u'\r': u'\\r', u'\r': u'\\r', u'\r': u'\\r'}

class Game(object):

    def __init__(self, name, path, num, allTime, server, isStart = False):
        self.server = server
        self.num = num

        try:
            self.name = name.decode(USE_CODE)
            self.path = path.decode(USE_CODE)
        except:
            self.name = name.decode(WINDOWS_CODE)
            self.path = path.decode(WINDOWS_CODE)
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

        self.isStart = isStart
        self.tickTime = server.getTimestamp() #上次统计时间
        self.playTime = 0 #本次在线时间
        self.allTime = allTime #总在线时间

        self.date2time = {} #每日时间

