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
        self.resize(280, 40)
        self.setMinimumSize(QtCore.QSize(280, 40))
        self.setMaximumSize(QtCore.QSize(280, 40))

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

