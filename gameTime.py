# -*- coding: utf-8 -*-

import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from PySide.QtCore import *
from PySide.QtGui import *

import mainUI
import addGameUI
import rmGameUI

from statistics import GameStatistics
from str_define import *

import copy
import codecs

class Form(QWidget): #主界面
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.ui= mainUI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("GameTime")
        # self.setWindowIcon(QIcon('./res/ico64.ico'))

        self.ui.actionAddGame.triggered.connect(self.tryAddGame)
        self.ui.actionRmGame.triggered.connect(self.tryRmGame)

        self.st = GameStatistics(True, self)
        self.lastUpTextTime = 0
        timer = QTimer(self)
        self.connect(timer, SIGNAL("timeout()"), self.onTick)
        timer.start(TICK_TIME)

    def setMenuBar(self, a):
        pass

    def setCentralWidget(self, a):
        pass

    def setStatusBar(self, a):
        pass

    def closeEvent(self, a): #关闭时存档
        self.st.onExit()
        self.st = None
        super(Form, self).closeEvent(a)

    def tryAddGame(self):
        self.addGameForm = AddGameForm(mainUI = self)
        self.addGameForm.show() 

    def tryRmGame(self):
        self.rmGameForm = RmGameForm(mainUI = self)
        self.rmGameForm.show() 

    def onTick(self): #心跳
        try:
            self.st.onTick()
            timestamp = self.st.getTimestamp()
            if timestamp - self.lastUpTextTime > UP_TEXT_TIME:
                self.upOnlineTime()
                self.lastUpTextTime = timestamp
        except Exception as e:
            print e
            self.st.isNormalRun = 0
            try:
                gameListFile = codecs.open(GAME_LIST_FILE, 'r')
                systemData = gameListFile.readlines()
                if not systemData:
                     systemData = [u'[]\n', u'\n', u'\n']
            except:
                systemData = [u'[]\n', u'\n', u'\n']
            gameNumList = eval(systemData[0])
            systemData[2] = SYSTEM_DATA_HEAD%0
            gameListFile = codecs.open(GAME_LIST_FILE, 'w')
            gameListFile.writelines(systemData)

            errFile = file(ERR_LOG_FILE, 'w')
            errFile.write(str(e))

    def upOnlineTime(self): #刷新显示数据
        runGameList = copy.deepcopy(self.st.runGameList)
        text = u''
        for num in runGameList:
            game = self.st.num2game[num]
            d, h, m, s = self.st.getPrintTime(game.playTime)
            onceTimeStr = '本次运行：%s小时%s分%s秒'%(h, m, s)
            onceTimeStr = onceTimeStr.decode('GBK')
            d, h, m, s = self.st.getPrintTime(game.allTime)
            allTimestr = '总共运行：%s天%s小时%s分%s秒'%(d, h, m, s)
            allTimestr = allTimestr.decode('GBK')
            typeText = '（运行中）'.decode('GBK')
            text += u'%s%s\n%s\n%s\n'%(game.name, typeText, onceTimeStr, allTimestr)
            text += u'----------\n'
        for num in self.st.num2game.keys():
            if num not in runGameList:
                game = self.st.num2game[num]
                d, h, m, s = self.st.getPrintTime(game.allTime)
                allTimestr = '总共运行：%s天%s小时%s分%s秒'%(d, h, m, s)
                allTimestr = allTimestr.decode('GBK')
                text += u'%s\n%s\n'%(game.name, allTimestr)
                text += u'----------\n'
        self.ui.textEdit.setText(text)

    def showErrorMessage(self, errorMessage):
        QMessageBox.warning (self, "Blanc message", errorMessage, QMessageBox.Ok, QMessageBox.Ok)

class AddGameForm(QWidget): #添加游戏界面
    def __init__(self, parent=None, mainUI = None):
        super(AddGameForm, self).__init__(parent)

        self.ui= addGameUI.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("添加游戏".decode('GBK'))
        self.setWindowIcon(QIcon('./res/ico64.ico'))
        self.mainUI = mainUI

        self.connect(self.ui.toolButtonPath, SIGNAL("clicked()"), self.addPath)
        self.connect(self.ui.pushButtonGo, SIGNAL("clicked()"), self.addGame)

    def setMenuBar(self, a):
        pass

    def setCentralWidget(self, a):
        pass

    def setStatusBar(self, a):
        pass

    def addPath(self):
        absolute_path = QFileDialog.getOpenFileName(self, 'Open file', '.', "exe files (*.exe)") 
        if absolute_path[0]:
            showTest = absolute_path[0]
            self.ui.lineEditPath.setText(showTest)

    def addGame(self):
        name = self.ui.lineEditName.text()
        path = self.ui.lineEditPath.text()
        newPath = u''
        for str in path:
            if u'/' == str:
                newPath += u'\\'
            else:
                newPath += str
        path = newPath
        if name and path:
            self.mainUI.st.tryAddGame(name, path)
        QMessageBox.information(self, "添加成功".decode('GBK'), "添加成功".decode('GBK'), QMessageBox.Ok, QMessageBox.Ok)
        self.close()

class RmGameForm(QWidget): #移除游戏界面
    def __init__(self, parent=None, mainUI = None):
        super(RmGameForm, self).__init__(parent)

        self.ui= rmGameUI.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("移除游戏".decode('GBK'))
        self.setWindowIcon(QIcon('./res/ico64.ico'))
        self.mainUI = mainUI
        for num in self.mainUI.st.num2game.keys():
            game = self.mainUI.st.num2game[num]
            name = game.name
            self.ui.comboBoxRmGame.addItem("%s:%s"%(num, name))

        self.connect(self.ui.pushButtonGo, SIGNAL("clicked()"), self.rmGame)

    def setMenuBar(self, a):
        pass

    def setCentralWidget(self, a):
        pass

    def setStatusBar(self, a):
        pass

    def rmGame(self):
        num = self.ui.comboBoxRmGame.currentText().split(':')[0]
        self.mainUI.st.tryRemoveGame(num)
        QMessageBox.information(self, "移除成功".decode('GBK'), "移除成功".decode('GBK'), QMessageBox.Ok, QMessageBox.Ok)
        self.close()

app = QApplication(sys.argv)
form = Form()
form.show()
# app.connect(b,SIGNAL("clicked()"),app,SLOT("quit()")) #点击b关闭
app.exec_()


