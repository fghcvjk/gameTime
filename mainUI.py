# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created: Wed Mar 01 14:08:03 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 200)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 20, 300, 191))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.actionAddGame = QtGui.QAction(MainWindow)
        self.actionAddGame.setObjectName("actionAddGame")
        self.actionRmGame = QtGui.QAction(MainWindow)
        self.actionRmGame.setObjectName("actionRmGame")
        self.menu.addAction(self.actionAddGame)
        self.menu.addAction(self.actionRmGame)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menu.setTitle(QtGui.QApplication.translate("MainWindow", "操作", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddGame.setText(QtGui.QApplication.translate("MainWindow", "添加游戏", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRmGame.setText(QtGui.QApplication.translate("MainWindow", "删除游戏", None, QtGui.QApplication.UnicodeUTF8))

