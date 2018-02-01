# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created: Thu Feb 01 10:14:35 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!



from PySide import QtCore, QtGui

class GameItem(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        super(GameItem, self).__init__(*args, **kwargs)
        self.defaultWeight = 280
        self.defaultHeight = 40
        self.resize(self.defaultWeight, self.defaultHeight)
        self.setMinimumSize(QtCore.QSize(self.defaultWeight, self.defaultHeight))
        self.setMaximumSize(QtCore.QSize(self.defaultWeight, self.defaultHeight))

        #添加自定义控件
        self.startButton = QtGui.QPushButton(self)
        self.startButton.setText("")
        self.startButton.setMinimumSize(QtCore.QSize(32, 32))
        self.startButton.setMaximumSize(QtCore.QSize(32, 32))
        self.startButton.setGeometry(QtCore.QRect(10, 5, 32, 32))
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

    def setMyPosition(self, position):
        positionW, positionH = position
        self.setGeometry(QtCore.QRect(positionW, positionH, self.defaultWeight, self.defaultHeight))

