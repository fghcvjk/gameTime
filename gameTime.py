# -*- coding: utf-8 -*-

import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from PySide.QtCore import *
from PySide.QtGui import *
from PyQt4.QtGui import QPixmap

from statistics import GameStatistics
from str_define import *
from res import mainUI, addGameUI, rmGameUI, gameItemUI

import copy
import codecs
import win32gui
import win32ui
import traceback

class Form(QWidget): #主界面
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.ui= mainUI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("GameTime")
        # self.setWindowFlags(Qt.FramelessWindowHint) #去掉边框相关处理，配合mousePressEvent、mouseMoveEvent、mouseReleaseEvent的重写使用
        #还可以设置永在最上等处理

        self.ui.actionAddGame.triggered.connect(self.tryAddGame)
        self.ui.actionRmGame.triggered.connect(self.tryRmGame)
        self.ui.gameItems = {}

        self.st = GameStatistics(True, self)
        self.lastUpTextTime = 0
        timer = QTimer(self)
        self.connect(timer, SIGNAL("timeout()"), self.onTick)
        timer.start(TICK_TIME)

    # def mousePressEvent(self, event):
        # if event.button()== Qt.LeftButton:
            # self.m_drag=True
            # self.m_DragPosition=event.globalPos()-self.pos()
            # event.accept()

    # def mouseMoveEvent(self, QMouseEvent):
        # if QMouseEvent.buttons() and Qt.LeftButton:
            # self.move(QMouseEvent.globalPos()-self.m_DragPosition)
            # QMouseEvent.accept()

    # def mouseReleaseEvent(self, QMouseEvent):
        # self.m_drag=False

    def getGameItem(self, name, time, num, game, st):
        path = game.path
        gameItem = gameItemUI.GameItem(self.ui.centralwidget)
        try:
            name = name.decode('utf-8')
        except:
            pass
        gameItem.nameLabe.setText(name)
        h, m, s = st.getPrintTime(time)
        allTimestr = '总共运行：%s小时%s分%s秒'%(h, m, s)
        allTimestr = allTimestr.decode('GBK')
        gameItem.timeLabe.setText(allTimestr)
        gameItem.setToolTip4All(allTimestr)
        if os.path.exists(path):
            large, small = win32gui.ExtractIconEx(game.path, 0)
            pixmap = QPixmap.fromWinHBITMAP(self.bitmapFromHIcon(large[0]), 2)
            pixmap.save("./data/%s.ico"%num,"ico")
        if os.path.exists("./data/%s.ico"%num):
            gameItem.startButton.setIcon(QIcon("./data/%s.ico"%num))
        gameItem.connect(gameItem.startButton, SIGNAL("clicked()"), game.startGame)
        return gameItem

    def bitmapFromHIcon(self, hIcon):
        hdc = win32ui.CreateDCFromHandle(win32gui.GetDC(0))
        hbmp = win32ui.CreateBitmap()
        hbmp.CreateCompatibleBitmap(hdc, 32, 32)
        hdc = hdc.CreateCompatibleDC()
        hdc.SelectObject(hbmp)
        hdc.DrawIcon((0, 0), hIcon)
        hdc.DeleteDC()
        return hbmp.GetHandle()

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
            print traceback.format_exc()
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
            errFile.write(str(traceback.format_exc()))

    def upOnlineTime(self): #刷新显示数据
        runGameList = copy.deepcopy(self.st.runGameList)
        weight = 0
        height = 25
        for num in runGameList:
            game = self.st.num2game[num]
            h, m, s = self.st.getPrintTime(game.playTime)
            onceTimeStr = '本次运行：%s小时%s分%s秒'%(h, m, s)
            onceTimeStr = onceTimeStr.decode('GBK')
            h, m, s = self.st.getPrintTime(game.allTime)
            allTimestr = '总共运行：%s小时%s分%s秒'%(h, m, s)
            allTimestr = allTimestr.decode('GBK')
            typeText = '（运行中）'.decode('GBK')
            gameItem = self.ui.gameItems[num]
            gameItem.setToolTip4All(allTimestr)
            gameItem.timeLabe.setText(onceTimeStr)
            gameItem.move(weight, height)
            gameItem.show()
            weight, height = gameItem.getNextItemPosition(weight, height)
        numList = self.st.num2game.keys()
        numList.reverse()
        for num in numList:
            if num not in runGameList:
                game = self.st.num2game[num]
                h, m, s = self.st.getPrintTime(game.allTime)
                allTimestr = '总共运行：%s小时%s分%s秒'%(h, m, s)
                allTimestr = allTimestr.decode('GBK')
                gameItem = self.ui.gameItems[num]
                gameItem.setToolTip4All(allTimestr)
                gameItem.timeLabe.setText(allTimestr)
                gameItem.move(weight, height)
                gameItem.show()
                weight, height = gameItem.getNextItemPosition(weight, height)

    def showErrorMessage(self, errorMessage):
        QMessageBox.warning (self, "Blanc message", errorMessage, QMessageBox.Ok, QMessageBox.Ok)

class AddGameForm(QWidget): #添加游戏界面
    def __init__(self, parent=None, mainUI = None):
        super(AddGameForm, self).__init__(parent)

        self.ui= addGameUI.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("添加游戏".decode('GBK'))
        # self.setWindowIcon(QIcon('./res/ico64.ico'))
        self.mainUI = mainUI

        self.connect(self.ui.toolButtonPath, SIGNAL("clicked()"), self.addPath)
        self.connect(self.ui.toolButtonStartPath, SIGNAL("clicked()"), self.addStartPath)
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
            if not self.ui.lineEditStartPath.text():
                self.ui.lineEditStartPath.setText(showTest)

    def addStartPath(self):
        absolute_path = QFileDialog.getOpenFileName(self, 'Open file', '.', "exe files (*.exe)") 
        if absolute_path[0]:
            showTest = absolute_path[0]
            self.ui.lineEditStartPath.setText(showTest)

    def addGame(self):
        name = self.ui.lineEditName.text()
        path = self.ui.lineEditPath.text()
        startPath = self.ui.lineEditStartPath.text()
        newPath = u''
        for str in path:
            if u'/' == str:
                newPath += u'\\'
            else:
                newPath += str
        path = newPath
        if name and path:
            self.mainUI.st.tryAddGame(name, path, startPath)
        QMessageBox.information(self, "添加成功".decode('GBK'), "添加成功".decode('GBK'), QMessageBox.Ok, QMessageBox.Ok)
        self.close()

class RmGameForm(QWidget): #移除游戏界面
    def __init__(self, parent=None, mainUI = None):
        super(RmGameForm, self).__init__(parent)

        self.ui= rmGameUI.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("移除游戏".decode('GBK'))
        # self.setWindowIcon(QIcon('./res/ico64.ico'))
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


