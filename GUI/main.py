# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(811, 562)
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.wordList = QtWidgets.QTreeView(Dialog)
        self.wordList.setGeometry(QtCore.QRect(20, 40, 191, 471))
        self.wordList.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.wordList.setObjectName("wordList")
        self.label_wl = QtWidgets.QLabel(Dialog)
        self.label_wl.setGeometry(QtCore.QRect(19, 20, 191, 20))
        self.label_wl.setAlignment(QtCore.Qt.AlignCenter)
        self.label_wl.setObjectName("label_wl")
        self.label_word = QtWidgets.QLabel(Dialog)
        self.label_word.setGeometry(QtCore.QRect(240, 40, 541, 21))
        self.label_word.setTextFormat(QtCore.Qt.AutoText)
        self.label_word.setScaledContents(False)
        self.label_word.setAlignment(QtCore.Qt.AlignCenter)
        self.label_word.setObjectName("label_word")
        self.label_word_show = QtWidgets.QLabel(Dialog)
        self.label_word_show.setGeometry(QtCore.QRect(240, 60, 541, 21))
        self.label_word_show.setText("")
        self.label_word_show.setAlignment(QtCore.Qt.AlignCenter)
        self.label_word_show.setObjectName("label_word_show")
        self.label_def = QtWidgets.QLabel(Dialog)
        self.label_def.setGeometry(QtCore.QRect(240, 90, 541, 20))
        self.label_def.setAlignment(QtCore.Qt.AlignCenter)
        self.label_def.setObjectName("label_def")
        self.label_def_show = QtWidgets.QLabel(Dialog)
        self.label_def_show.setGeometry(QtCore.QRect(240, 110, 541, 21))
        self.label_def_show.setText("")
        self.label_def_show.setAlignment(QtCore.Qt.AlignCenter)
        self.label_def_show.setObjectName("label_def_show")
        self.label_samp = QtWidgets.QLabel(Dialog)
        self.label_samp.setGeometry(QtCore.QRect(240, 140, 541, 21))
        self.label_samp.setAlignment(QtCore.Qt.AlignCenter)
        self.label_samp.setObjectName("label_samp")
        self.label_samp_show = QtWidgets.QLabel(Dialog)
        self.label_samp_show.setGeometry(QtCore.QRect(240, 160, 541, 41))
        self.label_samp_show.setAlignment(QtCore.Qt.AlignCenter)
        self.label_samp_show.setObjectName("label_samp_show")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(240, 240, 541, 271))
        self.textBrowser.setObjectName("textBrowser")
        self.label_console = QtWidgets.QLabel(Dialog)
        self.label_console.setGeometry(QtCore.QRect(240, 220, 541, 21))
        self.label_console.setAlignment(QtCore.Qt.AlignCenter)
        self.label_console.setObjectName("label_console")
        self.button_show_wordlist = QtWidgets.QPushButton(Dialog)
        self.button_show_wordlist.setGeometry(QtCore.QRect(22, 520, 191, 32))
        self.button_show_wordlist.setObjectName("button_show_wordlist")
        self.button_quit = QtWidgets.QPushButton(Dialog)
        self.button_quit.setGeometry(QtCore.QRect(672, 520, 111, 32))
        self.button_quit.setObjectName("button_quit")
        self.actionread_in = QtWidgets.QAction(Dialog)
        self.actionread_in.setCheckable(False)
        self.actionread_in.setObjectName("actionread_in")

        self.retranslateUi(Dialog)
        self.button_quit.clicked.connect(Dialog.close)
        self.button_show_wordlist.clicked.connect(self.wordList.showNormal)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.button_show_wordlist, self.wordList)
        Dialog.setTabOrder(self.wordList, self.textBrowser)
        Dialog.setTabOrder(self.textBrowser, self.button_quit)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_wl.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">WORD LIST</span></p></body></html>"))
        self.label_word.setText(_translate("Dialog", "WORD"))
        self.label_def.setText(_translate("Dialog", "DEFINITION"))
        self.label_samp.setText(_translate("Dialog", "SAMPLE SENTENCE"))
        self.label_samp_show.setText(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.label_console.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">CONSOLE</span></p></body></html>"))
        self.button_show_wordlist.setText(_translate("Dialog", "SHOW"))
        self.button_quit.setText(_translate("Dialog", "QUIT"))
        self.actionread_in.setText(_translate("Dialog", "read_in"))

