# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addGameUI.ui'
#
# Created: Thu Feb 01 10:19:02 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(400, 300)
        Form.setMinimumSize(QtCore.QSize(400, 300))
        Form.setMaximumSize(QtCore.QSize(400, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/ico64.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.toolButtonPath = QtGui.QToolButton(Form)
        self.toolButtonPath.setGeometry(QtCore.QRect(280, 150, 37, 18))
        self.toolButtonPath.setObjectName("toolButtonPath")
        self.lineEditName = QtGui.QLineEdit(Form)
        self.lineEditName.setGeometry(QtCore.QRect(150, 70, 113, 20))
        self.lineEditName.setObjectName("lineEditName")
        self.labelName = QtGui.QLabel(Form)
        self.labelName.setGeometry(QtCore.QRect(100, 75, 54, 12))
        self.labelName.setObjectName("labelName")
        self.labelPath = QtGui.QLabel(Form)
        self.labelPath.setGeometry(QtCore.QRect(110, 155, 54, 12))
        self.labelPath.setObjectName("labelPath")
        self.lineEditPath = QtGui.QLineEdit(Form)
        self.lineEditPath.setGeometry(QtCore.QRect(150, 150, 113, 20))
        self.lineEditPath.setObjectName("lineEditPath")
        self.pushButtonGo = QtGui.QPushButton(Form)
        self.pushButtonGo.setEnabled(True)
        self.pushButtonGo.setGeometry(QtCore.QRect(160, 230, 75, 23))
        self.pushButtonGo.setObjectName("pushButtonGo")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButtonPath.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.labelName.setText(QtGui.QApplication.translate("Form", "游戏名：", None, QtGui.QApplication.UnicodeUTF8))
        self.labelPath.setText(QtGui.QApplication.translate("Form", "路径：", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonGo.setText(QtGui.QApplication.translate("Form", "添加游戏", None, QtGui.QApplication.UnicodeUTF8))

import ico_rc
