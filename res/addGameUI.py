# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addGameUI.ui'
#
# Created: Fri Feb 02 16:07:17 2018
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
        self.toolButtonPath.setGeometry(QtCore.QRect(280, 120, 37, 18))
        self.toolButtonPath.setObjectName("toolButtonPath")
        self.lineEditName = QtGui.QLineEdit(Form)
        self.lineEditName.setGeometry(QtCore.QRect(150, 70, 113, 20))
        self.lineEditName.setObjectName("lineEditName")
        self.labelName = QtGui.QLabel(Form)
        self.labelName.setGeometry(QtCore.QRect(100, 75, 54, 12))
        self.labelName.setObjectName("labelName")
        self.labelPath = QtGui.QLabel(Form)
        self.labelPath.setGeometry(QtCore.QRect(110, 125, 54, 12))
        self.labelPath.setObjectName("labelPath")
        self.lineEditPath = QtGui.QLineEdit(Form)
        self.lineEditPath.setGeometry(QtCore.QRect(150, 120, 113, 20))
        self.lineEditPath.setObjectName("lineEditPath")
        self.pushButtonGo = QtGui.QPushButton(Form)
        self.pushButtonGo.setEnabled(True)
        self.pushButtonGo.setGeometry(QtCore.QRect(160, 230, 75, 23))
        self.pushButtonGo.setObjectName("pushButtonGo")
        self.lineEditStartPath = QtGui.QLineEdit(Form)
        self.lineEditStartPath.setGeometry(QtCore.QRect(150, 170, 113, 20))
        self.lineEditStartPath.setObjectName("lineEditStartPath")
        self.labelStartPath = QtGui.QLabel(Form)
        self.labelStartPath.setGeometry(QtCore.QRect(90, 170, 61, 20))
        self.labelStartPath.setObjectName("labelStartPath")
        self.toolButtonStartPath = QtGui.QToolButton(Form)
        self.toolButtonStartPath.setGeometry(QtCore.QRect(280, 170, 37, 18))
        self.toolButtonStartPath.setObjectName("toolButtonStartPath")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButtonPath.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.labelName.setText(QtGui.QApplication.translate("Form", "游戏名：", None, QtGui.QApplication.UnicodeUTF8))
        self.labelPath.setText(QtGui.QApplication.translate("Form", "路径：", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonGo.setText(QtGui.QApplication.translate("Form", "添加游戏", None, QtGui.QApplication.UnicodeUTF8))
        self.labelStartPath.setText(QtGui.QApplication.translate("Form", "启动路径：", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButtonStartPath.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))

import ico_rc
