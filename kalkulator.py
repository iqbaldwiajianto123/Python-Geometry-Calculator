# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\python\kalkulator.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QObject, pyqtSignal, Qt
from fungsiBangunRuang import *
import sys


palette = QtGui.QPalette()
brush = QtGui.QBrush(QtGui.QColor(0, 126, 0))
brush.setStyle(QtCore.Qt.SolidPattern)
palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
brush = QtGui.QBrush(QtGui.QColor(0, 107, 0))
brush.setStyle(QtCore.Qt.SolidPattern)
palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
brush.setStyle(QtCore.Qt.SolidPattern)
palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
brush = QtGui.QBrush(QtGui.QColor(70, 70, 70))
brush.setStyle(QtCore.Qt.SolidPattern)
palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
brush.setStyle(QtCore.Qt.SolidPattern)
palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
brush = QtGui.QBrush(QtGui.QColor(88, 88, 88))
brush.setStyle(QtCore.Qt.SolidPattern)
palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
brush.setStyle(QtCore.Qt.SolidPattern)
palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
brush.setStyle(QtCore.Qt.SolidPattern)
palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
brush = QtGui.QBrush(QtGui.QColor(91, 91, 91))
brush.setStyle(QtCore.Qt.SolidPattern)
palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
brush = QtGui.QBrush(QtGui.QColor(48, 48, 48))
brush.setStyle(QtCore.Qt.SolidPattern)
palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
brush = QtGui.QBrush(QtGui.QColor(58, 58, 58))
brush.setStyle(QtCore.Qt.SolidPattern)
palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
brush = QtGui.QBrush(QtGui.QColor(6, 135, 21))
brush.setStyle(QtCore.Qt.SolidPattern)
palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
brush.setStyle(QtCore.Qt.SolidPattern)
palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
brush = QtGui.QBrush(QtGui.QColor(0, 126, 0))
brush.setStyle(QtCore.Qt.SolidPattern)
palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
brush = QtGui.QBrush(QtGui.QColor(0, 107, 0))
brush.setStyle(QtCore.Qt.SolidPattern)
palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
brush.setStyle(QtCore.Qt.SolidPattern)
palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
brush = QtGui.QBrush(QtGui.QColor(70, 70, 70))
brush.setStyle(QtCore.Qt.SolidPattern)
palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
brush.setStyle(QtCore.Qt.SolidPattern)
palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
brush = QtGui.QBrush(QtGui.QColor(88, 88, 88))
brush.setStyle(QtCore.Qt.SolidPattern)
palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
brush.setStyle(QtCore.Qt.SolidPattern)
palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
brush.setStyle(QtCore.Qt.SolidPattern)
palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
brush = QtGui.QBrush(QtGui.QColor(91, 91, 91))
brush.setStyle(QtCore.Qt.SolidPattern)
palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
brush = QtGui.QBrush(QtGui.QColor(48, 48, 48))
brush.setStyle(QtCore.Qt.SolidPattern)
palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
brush = QtGui.QBrush(QtGui.QColor(58, 58, 58))
brush.setStyle(QtCore.Qt.SolidPattern)
palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
brush = QtGui.QBrush(QtGui.QColor(6, 135, 21))
brush.setStyle(QtCore.Qt.SolidPattern)
palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
brush.setStyle(QtCore.Qt.SolidPattern)
palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
brush.setStyle(QtCore.Qt.SolidPattern)
palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
brush = QtGui.QBrush(QtGui.QColor(0, 107, 0))
brush.setStyle(QtCore.Qt.SolidPattern)
palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
brush.setStyle(QtCore.Qt.SolidPattern)
palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
brush = QtGui.QBrush(QtGui.QColor(70, 70, 70))
brush.setStyle(QtCore.Qt.SolidPattern)
palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
brush.setStyle(QtCore.Qt.SolidPattern)
palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
brush = QtGui.QBrush(QtGui.QColor(88, 88, 88))
brush.setStyle(QtCore.Qt.SolidPattern)
palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
brush.setStyle(QtCore.Qt.SolidPattern)
palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
brush.setStyle(QtCore.Qt.SolidPattern)
palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
brush = QtGui.QBrush(QtGui.QColor(48, 48, 48))
brush.setStyle(QtCore.Qt.SolidPattern)
palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
brush = QtGui.QBrush(QtGui.QColor(48, 48, 48))
brush.setStyle(QtCore.Qt.SolidPattern)
palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
brush = QtGui.QBrush(QtGui.QColor(58, 58, 58))
brush.setStyle(QtCore.Qt.SolidPattern)
palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
brush = QtGui.QBrush(QtGui.QColor(6, 135, 21))
brush.setStyle(QtCore.Qt.SolidPattern)
palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
brush.setStyle(QtCore.Qt.SolidPattern)
palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)

button_font = QtGui.QFont()
button_font.setFamily("Quicksand")
button_font.setPointSize(14)
button_font.setBold(True)
button_font.setWeight(75)

title_font = QtGui.QFont()
title_font.setFamily("Quicksand SemiBold")
title_font.setPointSize(18)
title_font.setBold(True)
title_font.setWeight(75)

label_font = QtGui.QFont()
label_font.setFamily("Quicksand")
label_font.setPointSize(16)
label_font.setBold(True)
label_font.setWeight(75)


class OptionWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setPalette(palette)
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.onlyInt = QtGui.QIntValidator()
        self.QMessageBox = QtWidgets.QMessageBox(MainWindow)

        # WINDOW CONTROLLER
        self.kalkulator_page = QtWidgets.QStackedWidget(self.centralwidget)
        self.kalkulator_page.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.kalkulator_page.setObjectName("kalkulator_page")

        # MAIN PAGE
        self.main_page = QtWidgets.QWidget()
        self.main_page.setObjectName("main_page")

        # TITLE
        self.title1 = QtWidgets.QLabel(self.main_page)
        self.title1.setGeometry(QtCore.QRect(210, 190, 340, 41))
        self.title1.setFont(title_font)
        self.title1.setObjectName("title1")

        # TABUNG OPTION
        self.tabung_opt = QtWidgets.QPushButton(self.main_page)
        self.tabung_opt.setGeometry(QtCore.QRect(170, 270, 131, 41))
        self.tabung_opt.setFont(button_font)
        self.tabung_opt.setFlat(False)
        self.tabung_opt.setObjectName("tabung_opt")

        # KERUCUT OPTION
        self.kerucut_opt = QtWidgets.QPushButton(self.main_page)
        self.kerucut_opt.setGeometry(QtCore.QRect(310, 270, 131, 41))
        self.kerucut_opt.setFont(button_font)
        self.kerucut_opt.setObjectName("kerucut_opt")

        # BOLA OPTION
        self.ball_opt = QtWidgets.QPushButton(self.main_page)
        self.ball_opt.setGeometry(QtCore.QRect(450, 270, 131, 41))
        self.ball_opt.setFont(button_font)
        self.ball_opt.setObjectName("ball_opt")

        self.kalkulator_page.addWidget(self.main_page)

        # TABUNG PAGE
        self.opt1_page = QtWidgets.QWidget()
        self.opt1_page.setObjectName("opt1_page")

        self.opt1_preset_page = QtWidgets.QStackedWidget(self.opt1_page)
        self.opt1_preset_page.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.opt1_preset_page.setObjectName("opt1_preset_page")

        # OUTPUT
        self.output0 = QtWidgets.QLabel(self.opt1_page)
        self.output0.setGeometry(QtCore.QRect(230, 470, 281, 41))
        self.output0.setFont(button_font)
        self.output0.setAutoFillBackground(True)
        self.output0.setFrameShape(QtWidgets.QFrame.Box)
        self.output0.setFrameShadow(QtWidgets.QFrame.Plain)
        self.output0.setText("")
        self.output0.setObjectName("output0")

        # COPY BUTTON
        self.copy_output0 = QtWidgets.QPushButton(self.opt1_page)
        self.copy_output0.setGeometry(QtCore.QRect(520, 470, 41, 41))
        self.copy_output0.setText("")
        self.copy_output0.setObjectName("copy_output0")

        # calculate0 BUTTON
        self.calculate0 = QtWidgets.QPushButton(self.opt1_page)
        self.calculate0.setGeometry(QtCore.QRect(340, 410, 101, 41))
        self.calculate0.setFont(button_font)
        self.calculate0.setObjectName("calculate0")

        # RETURN BUTTON
        self.return_button0 = QtWidgets.QPushButton(self.opt1_page)
        self.return_button0.setGeometry(QtCore.QRect(30, 20, 41, 31))
        self.return_button0.setText("")
        self.return_button0.setObjectName("return_button0")

        # TABUNG PRESET
        self.tabung_preset = QtWidgets.QComboBox(self.opt1_page)
        self.tabung_preset.setGeometry(QtCore.QRect(240, 150, 321, 41))
        self.tabung_preset.setMaxVisibleItems(4)
        preset_font = QtGui.QFont()
        preset_font.setFamily("Quicksand")
        preset_font.setPointSize(12)
        preset_font.setBold(True)
        preset_font.setWeight(75)
        self.tabung_preset.setFont(preset_font)
        self.tabung_preset.setObjectName("tabung_preset")
        self.tabung_preset.addItem("")
        self.tabung_preset.addItem("")
        self.tabung_preset.addItem("")
        self.tabung_preset.addItem("")
        self.tabung_preset.addItem("")
        self.tabung_preset.addItem("")
        self.tabung_preset.addItem("")
        self.tabung_preset.addItem("")
        self.tabung_preset.addItem("")
        self.tabung_preset.addItem("")

        # CALCULATOR TITLE
        self.tabung_opt_label = QtWidgets.QLabel(self.opt1_page)
        self.tabung_opt_label.setGeometry(QtCore.QRect(260, 90, 281, 41))
        self.tabung_opt_label.setFont(title_font)
        self.tabung_opt_label.setObjectName("tabung_opt_label")

        self.sub_label0 = QtWidgets.QLabel(self.opt1_page)
        self.sub_label0.setGeometry(QtCore.QRect(350, 210, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.sub_label0.setFont(font)
        self.sub_label0.setObjectName("sub_label0")

        ######################
        ###### PRESET 0 ######
        ######################
        self.opt1_preset0 = QtWidgets.QWidget()
        self.opt1_preset0.setObjectName("opt1_preset0")

        # PI LABEL
        self.pi_label0 = QtWidgets.QLabel(self.opt1_preset0)
        self.pi_label0.setGeometry(QtCore.QRect(165, 247, 71, 31))
        self.pi_label0.setFont(label_font)
        self.pi_label0.setObjectName("pi_label0")

        # PI VALUE
        self.pi_value0 = QtWidgets.QLabel(self.opt1_preset0)
        self.pi_value0.setGeometry(QtCore.QRect(200, 255, 81, 21))
        self.pi_value0.setFont(label_font)
        self.pi_value0.setFrameShape(QtWidgets.QFrame.Panel)
        self.pi_value0.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pi_value0.setText("")
        self.pi_value0.setObjectName("pi_value0")

        # r LABEL
        self.r_label0 = QtWidgets.QLabel(self.opt1_preset0)
        self.r_label0.setGeometry(QtCore.QRect(490, 250, 81, 21))
        self.r_label0.setFont(label_font)
        self.r_label0.setText("")
        self.r_label0.setObjectName("r_label0")

        # r VALUE
        self.r_value0 = QtWidgets.QSpinBox(self.opt1_preset0)
        self.r_value0.setGeometry(QtCore.QRect(530, 255, 121, 26))
        self.r_value0.setFont(label_font)
        # self.r_value0.setText("")
        self.r_value0.setObjectName("r_value0")
        # self.r_value0.setValidator(self.onlyInt)

        self.opt1_preset_page.addWidget(self.opt1_preset0)

        ######################
        ###### PRESET 1 ######
        ######################
        self.opt1_preset1 = QtWidgets.QWidget()
        self.opt1_preset1.setObjectName("opt1_preset1")

        # DIKETAHUI
        self.tracker1 = QtWidgets.QLabel(self.opt1_preset1)
        self.tracker1.setGeometry(QtCore.QRect(350, 210, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tracker1.setFont(font)
        self.tracker1.setObjectName("tracker1")

        # PI LABEL
        self.pi_label1 = QtWidgets.QLabel(self.opt1_preset1)
        self.pi_label1.setGeometry(QtCore.QRect(165, 247, 71, 31))
        self.pi_label1.setFont(label_font)
        self.pi_label1.setObjectName("pi_label1")

        # PI VALUE
        self.pi_value1 = QtWidgets.QLabel(self.opt1_preset1)
        self.pi_value1.setGeometry(QtCore.QRect(200, 255, 81, 21))
        self.pi_value1.setFont(label_font)
        self.pi_value1.setFrameShape(QtWidgets.QFrame.Panel)
        self.pi_value1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pi_value1.setText("")
        self.pi_value1.setObjectName("pi_value1")

        # r LABEL
        self.r_label1 = QtWidgets.QLabel(self.opt1_preset1)
        self.r_label1.setGeometry(QtCore.QRect(490, 250, 81, 21))
        self.r_label1.setFont(label_font)
        self.r_label1.setText("")
        self.r_label1.setObjectName("r_label1")

        # r VALUE
        self.r_value1 = QtWidgets.QSpinBox(self.opt1_preset1)
        self.r_value1.setGeometry(QtCore.QRect(530, 255, 121, 26))
        self.r_value1.setFont(label_font)
        # self.r_value1.setText("")
        self.r_value1.setObjectName("r_value1")
        # self.r_value1.setValidator(self.onlyInt)

        # t LABEL
        self.t_label1 = QtWidgets.QLabel(self.opt1_preset1)
        self.t_label1.setGeometry(QtCore.QRect(490, 276, 81, 21))
        self.t_label1.setFont(label_font)
        self.t_label1.setText("")
        self.t_label1.setObjectName("t_label1")

        # t VALUE
        self.t_value1 = QtWidgets.QSpinBox(self.opt1_preset1)
        self.t_value1.setGeometry(QtCore.QRect(530, 286, 121, 26))
        self.t_value1.setFont(label_font)
        self.t_value1.setObjectName("t_value1")

        self.opt1_preset_page.addWidget(self.opt1_preset1)

        ######################
        ###### PRESET 2 ######
        ######################
        self.opt1_preset2 = QtWidgets.QWidget()
        self.opt1_preset2.setObjectName("opt1_preset2")

        # PI LABEL
        self.pi_label2 = QtWidgets.QLabel(self.opt1_preset2)
        self.pi_label2.setGeometry(QtCore.QRect(165, 247, 71, 31))
        self.pi_label2.setFont(label_font)
        self.pi_label2.setObjectName("pi_label2")

        # PI VALUE
        self.pi_value2 = QtWidgets.QLabel(self.opt1_preset2)
        self.pi_value2.setGeometry(QtCore.QRect(200, 255, 81, 21))
        self.pi_value2.setFont(label_font)
        self.pi_value2.setFrameShape(QtWidgets.QFrame.Panel)
        self.pi_value2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pi_value2.setText("")
        self.pi_value2.setObjectName("pi_value2")

        # r LABEL
        self.r_label2 = QtWidgets.QLabel(self.opt1_preset2)
        self.r_label2.setGeometry(QtCore.QRect(490, 250, 81, 21))
        self.r_label2.setFont(label_font)
        self.r_label2.setText("")
        self.r_label2.setObjectName("r_label2")

        # r VALUE
        self.r_value2 = QtWidgets.QSpinBox(self.opt1_preset2)
        self.r_value2.setGeometry(QtCore.QRect(530, 255, 121, 26))
        self.r_value2.setFont(label_font)
        # self.r_value2.setText("")
        self.r_value2.setObjectName("r_value2")
        # self.r_value2.setValidator(self.onlyInt)

        # t LABEL
        self.t_label2 = QtWidgets.QLabel(self.opt1_preset2)
        self.t_label2.setGeometry(QtCore.QRect(490, 276, 81, 21))
        self.t_label2.setFont(label_font)
        self.t_label2.setText("")
        self.t_label2.setObjectName("t_label2")

        # t VALUE
        self.t_value2 = QtWidgets.QSpinBox(self.opt1_preset2)
        self.t_value2.setGeometry(QtCore.QRect(530, 286, 121, 26))
        self.t_value2.setFont(label_font)
        self.t_value2.setObjectName("t_value2")

        self.opt1_preset_page.addWidget(self.opt1_preset2)

        ######################
        ###### PRESET 3 ######
        ######################
        self.opt1_preset3 = QtWidgets.QWidget()
        self.opt1_preset3.setObjectName("opt1_preset3")

        # PI LABEL
        self.pi_label3 = QtWidgets.QLabel(self.opt1_preset3)
        self.pi_label3.setGeometry(QtCore.QRect(165, 247, 71, 31))
        self.pi_label3.setFont(label_font)
        self.pi_label3.setObjectName("pi_label3")

        # PI VALUE
        self.pi_value3 = QtWidgets.QLabel(self.opt1_preset3)
        self.pi_value3.setGeometry(QtCore.QRect(200, 255, 81, 21))
        self.pi_value3.setFont(label_font)
        self.pi_value3.setFrameShape(QtWidgets.QFrame.Panel)
        self.pi_value3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pi_value3.setText("")
        self.pi_value3.setObjectName("pi_value3")

        # r LABEL
        self.r_label3 = QtWidgets.QLabel(self.opt1_preset3)
        self.r_label3.setGeometry(QtCore.QRect(490, 250, 81, 21))
        self.r_label3.setFont(label_font)
        self.r_label3.setText("")
        self.r_label3.setObjectName("r_label3")

        # r VALUE
        self.r_value3 = QtWidgets.QSpinBox(self.opt1_preset3)
        self.r_value3.setGeometry(QtCore.QRect(530, 255, 121, 26))
        self.r_value3.setFont(label_font)
        # self.r_value3.setText("")
        self.r_value3.setObjectName("r_value3")
        # self.r_value3.setValidator(self.onlyInt)

        # t LABEL
        self.t_label3 = QtWidgets.QLabel(self.opt1_preset3)
        self.t_label3.setGeometry(QtCore.QRect(490, 276, 81, 21))
        self.t_label3.setFont(label_font)
        self.t_label3.setText("")
        self.t_label3.setObjectName("t_label3")

        # t VALUE
        self.t_value3 = QtWidgets.QSpinBox(self.opt1_preset3)
        self.t_value3.setGeometry(QtCore.QRect(530, 286, 121, 26))
        self.t_value3.setFont(label_font)
        self.t_value3.setObjectName("t_value3")

        self.opt1_preset_page.addWidget(self.opt1_preset3)

        self.kalkulator_page.addWidget(self.opt1_page)

        # CENTRAL WIDGETS
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 493, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.kalkulator_page.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Kalkulator Bangun Ruang"))
        self.title1.setText(_translate(
            "MainWindow", "KALKULATOR BANGUN RUANG"))
        self.tabung_opt.setText(_translate("MainWindow", "TABUNG"))
        self.kerucut_opt.setText(_translate("MainWindow", "KERUCUT"))
        self.ball_opt.setText(_translate("MainWindow", "BOLA"))
        self.tabung_preset.setItemText(0, _translate(
            "MainWindow", "LUAS PERMUKAAN LINGKARAN"))
        self.tabung_preset.setItemText(1, _translate(
            "MainWindow", "LUAS SELIMUT TABUNG"))
        self.tabung_preset.setItemText(2, _translate(
            "MainWindow", "LUAS PERMUKAAN TABUNG"))
        self.tabung_preset.setItemText(
            3, _translate("MainWindow", "VOLUME TABUNG"))
        self.tabung_preset.setItemText(4, _translate(
            "MainWindow", "TINGGI DENGAN LUAS SELIMUT TABUNG"))
        self.tabung_preset.setItemText(5, _translate(
            "MainWindow", "TINGGI DENGAN LUAS PERMUKAAN TABUNG"))
        self.tabung_preset.setItemText(6, _translate(
            "MainWindow", "TINGGI DENGAN VOLUME TABUNG"))
        self.tabung_preset.setItemText(7, _translate(
            "MainWindow", "JARI-JARI DENGAN LUAS SELIMUT TABUNG"))
        self.tabung_preset.setItemText(8, _translate(
            "MainWindow", "JARI-JARI DENGAN LUAS PERMUKAAN TABUNG"))
        self.tabung_preset.setItemText(9, _translate(
            "MainWindow", "JARI-JARI DENGAN VOLUME TABUNG"))
        self.tabung_opt_label.setText(_translate(
            "MainWindow", "PERHITUNGAN TABUNG"))
        self.sub_label0.setText(_translate("MainWindow", "DIKETAHUI"))
        self.pi_label0.setText(_translate("MainWindow", "π ="))
        self.pi_label1.setText(_translate("MainWindow", "π ="))
        self.pi_label2.setText(_translate("MainWindow", "π ="))
        self.pi_label3.setText(_translate("MainWindow", "π ="))
        self.r_label0.setText(_translate("MainWindow", "r ="))
        self.r_label1.setText(_translate("MainWindow", "r ="))
        self.r_label2.setText(_translate("MainWindow", "r = "))
        self.r_label3.setText(_translate("MainWindow", "r = "))
        self.t_label1.setText(_translate("MainWindow", "t = "))
        self.t_label2.setText(_translate("MainWindow", "t = "))
        self.t_label3.setText(_translate("MainWindow", "t = "))
        self.calculate0.setText(_translate("MainWindow", "HITUNG"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    sys.exit(app.exec_())

# π
