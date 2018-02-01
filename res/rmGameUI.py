# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rmGameUI.ui'
#
# Created: Thu Feb 01 10:19:03 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setMinimumSize(QtCore.QSize(400, 300))
        Form.setMaximumSize(QtCore.QSize(400, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/ico64.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.comboBoxRmGame = QtGui.QComboBox(Form)
        self.comboBoxRmGame.setGeometry(QtCore.QRect(170, 100, 171, 22))
        self.comboBoxRmGame.setObjectName("comboBoxRmGame")
        self.labelRmGame = QtGui.QLabel(Form)
        self.labelRmGame.setGeometry(QtCore.QRect(50, 103, 120, 16))
        self.labelRmGame.setObjectName("labelRmGame")
        self.pushButtonGo = QtGui.QPushButton(Form)
        self.pushButtonGo.setEnabled(True)
        self.pushButtonGo.setGeometry(QtCore.QRect(160, 220, 75, 23))
        self.pushButtonGo.setObjectName("pushButtonGo")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.labelRmGame.setText(QtGui.QApplication.translate("Form", "请选择要移除的游戏：", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonGo.setText(QtGui.QApplication.translate("Form", "移除游戏", None, QtGui.QApplication.UnicodeUTF8))

import ico_rc
