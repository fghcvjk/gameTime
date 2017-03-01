# -*- coding: utf-8 -*-

import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from PySide.QtCore import *
from PySide.QtGui import *

from mainUI import Ui_MainWindow

from statistics import GameStatistics

class Form(QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.ui= Ui_MainWindow()
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

    def tryAddGame(self):
        pass

    def tryRmGame(self):
        pass

    def upOnlineTime(self):
        text = u''
        for num in self.st.runGameList:
            game = self.st.num2game[num]
            d, h, m, s = self.st.getPrintTime(game.playTime)
            onceTimeStr = '本次运行：%s小时%s分%s秒'%(h, m, s)
            onceTimeStr = onceTimeStr.decode('GBK')
            d, h, m, s = self.st.getPrintTime(game.allTime)
            allTimestr = '总共运行：%s天%s小时%s分%s秒'%(d, h, m, s)
            allTimestr = allTimestr.decode('GBK')
            text += u'%s\n%s\n%s\n'%(game.name, onceTimeStr, allTimestr)
            text += u'----------'
        self.ui.textEdit.setText(text)

app = QApplication(sys.argv)
form = Form()
form.show()
# app.connect(b,SIGNAL("clicked()"),app,SLOT("quit()")) #点击b关闭
app.exec_()