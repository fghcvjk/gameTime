# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created: Thu Feb 01 10:14:35 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

MAIN_HEIGHT = 40
MAIN_WEIGHT = 280
ADD_WEIGHT = MAIN_HEIGHT + 5

from PySide import QtCore, QtGui

class GameItem(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        super(GameItem, self).__init__(*args, **kwargs)
        self.resize(MAIN_WEIGHT, MAIN_HEIGHT)
        self.setMinimumSize(QtCore.QSize(MAIN_WEIGHT, MAIN_HEIGHT))
        self.setMaximumSize(QtCore.QSize(MAIN_WEIGHT, MAIN_HEIGHT))

        #添加自定义控件
        self.startButton = QtGui.QPushButton(self)
        self.startButton.setText('')
        self.startButton.setToolTip('启动游戏'.decode('utf-8'))
        self.startButton.setMinimumSize(QtCore.QSize(32, 32))
        self.startButton.setMaximumSize(QtCore.QSize(32, 32))
        self.startButton.setGeometry(QtCore.QRect(10, 5, 32, 32))
        self.startButton.setIconSize(QtCore.QSize(32, 32))
        self.nameLabe = QtGui.QLabel(self)
        self.nameLabe.setMinimumSize(QtCore.QSize(220, 16))
        self.nameLabe.setMaximumSize(QtCore.QSize(220, 16))
        self.nameLabe.setText('nameLabe')
        self.nameLabe.setGeometry(QtCore.QRect(50, 0, 220, 16))
        self.timeLabe = QtGui.QLabel(self)
        self.timeLabe.setMinimumSize(QtCore.QSize(220, 16))
        self.timeLabe.setMaximumSize(QtCore.QSize(220, 16))
        self.timeLabe.setText('timeLabe')
        self.timeLabe.setGeometry(QtCore.QRect(50, 20, 220, 16))

    def getNextItemPosition(self, weight, height):
        return (weight, height+ADD_WEIGHT)

    def setToolTip4All(self, tips):
        # self.startButton.setToolTip(tips)
        self.nameLabe.setToolTip(tips)
        self.timeLabe.setToolTip(tips)
        self.setToolTip(tips)

