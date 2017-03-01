# -*- coding: utf-8 -*-

import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from PySide.QtCore import *
from PySide.QtGui import *

import mainUI
import addGameUI

from statistics import GameStatistics

class AddGameForm(QWidget):
    def __init__(self, parent=None, mainUI = None):
        super(AddGameForm, self).__init__(parent)

        self.ui= addGameUI.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("������Ϸ".decode('GBK'))
        self.mainUI = mainUI

        self.connect(self.ui.toolButtonPath, SIGNAL("clicked()"),self.addPath)
        self.connect(self.ui.pushButtonGo, SIGNAL("clicked()"),self.addGame)

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
        if name and path:
            self.mainUI.st.addGame(name, path)
        QMessageBox.information(self, "���ӳɹ�".decode('GBK'), "���ӳɹ�".decode('GBK'), QMessageBox.Ok, QMessageBox.Ok)
        self.close()

class Form(QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.ui= mainUI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("BlancTrans")

        self.ui.actionAddGame.triggered.connect(self.tryAddGame)
        self.ui.actionRmGame.triggered.connect(self.tryRmGame)

        self.st = GameStatistics(True, self)
        timer = QTimer(self)
        self.connect(timer, SIGNAL("timeout()"), self.upOnlineTime)
        timer.start(1000)
        # self.st.addTick(self.upOnlineTime, 1000)

    def setMenuBar(self, a):
        pass

    def setCentralWidget(self, a):
        pass

    def setStatusBar(self, a):
        pass

    def closeEvent(self, a):
        self.st.onExit()
        self.st = None
        super(Form, self).closeEvent(a)

    def tryAddGame(self):
        self.addGameForm = AddGameForm(mainUI = self)
        self.addGameForm.show() 

    def tryRmGame(self):
        pass

    def upOnlineTime(self):
        text = u''
        for num in self.st.runGameList:
            game = self.st.num2game[num]
            d, h, m, s = self.st.getPrintTime(game.playTime)
            onceTimeStr = '�������У�%sСʱ%s��%s��'%(h, m, s)
            onceTimeStr = onceTimeStr.decode('GBK')
            d, h, m, s = self.st.getPrintTime(game.allTime)
            allTimestr = '�ܹ����У�%s��%sСʱ%s��%s��'%(d, h, m, s)
            allTimestr = allTimestr.decode('GBK')
            text += u'%s\n%s\n%s\n'%(game.name, onceTimeStr, allTimestr)
            text += u'----------'
        self.ui.textEdit.setText(text)

app = QApplication(sys.argv)
form = Form()
form.show()
# app.connect(b,SIGNAL("clicked()"),app,SLOT("quit()")) #���b�ر�
app.exec_()