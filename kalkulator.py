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
        self.tabung_preset.setGeometry(QtCore.QRect(210, 150, 381, 41))
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
        self.r_label0.setGeometry(QtCore.QRect(490, 240, 81, 35))
        self.r_label0.setFont(label_font)
        self.r_label0.setText("")
        self.r_label0.setObjectName("r_label0")

        # r VALUE
        self.r_value0 = QtWidgets.QLineEdit(self.opt1_preset0)
        self.r_value0.setGeometry(QtCore.QRect(530, 245, 121, 35))
        self.r_value0.setFont(label_font)
        self.r_value0.setObjectName("r_value0")
        self.r_value0.setValidator(self.onlyInt)

        # self.r_value0 = QtWidgets.QSpinBox(self.opt1_preset0)
        # self.r_value0.setGeometry(QtCore.QRect(530, 245, 121, 35))
        # self.r_value0.setFont(label_font)
        # # self.r_value0.setText("")
        # self.r_value0.setObjectName("r_value0")
        # # self.r_value0.setValidator(self.onlyInt)

        self.opt1_preset_page.addWidget(self.opt1_preset0)

        ######################
        ###### PRESET 1 ######
        ######################
        self.opt1_preset1 = QtWidgets.QWidget()
        self.opt1_preset1.setObjectName("opt1_preset1")

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
        self.r_label1.setGeometry(QtCore.QRect(490, 240, 81, 35))
        self.r_label1.setFont(label_font)
        self.r_label1.setText("")
        self.r_label1.setObjectName("r_label1")

        # r VALUE
        self.r_value1 = QtWidgets.QLineEdit(self.opt1_preset1)
        self.r_value1.setGeometry(QtCore.QRect(530, 245, 121, 35))
        self.r_value1.setFont(label_font)
        self.r_value1.setObjectName("r_value1")
        self.r_value1.setValidator(self.onlyInt)

        # self.r_value1 = QtWidgets.QSpinBox(self.opt1_preset1)
        # self.r_value1.setGeometry(QtCore.QRect(530, 245, 121, 35))
        # self.r_value1.setFont(label_font)
        # # self.r_value1.setText("")
        # self.r_value1.setObjectName("r_value1")
        # # self.r_value1.setValidator(self.onlyInt)

        # t LABEL
        self.t_label1 = QtWidgets.QLabel(self.opt1_preset1)
        self.t_label1.setGeometry(QtCore.QRect(490, 290, 81, 35))
        self.t_label1.setFont(label_font)
        self.t_label1.setText("")
        self.t_label1.setObjectName("t_label1")

        # t VALUE
        self.t_value1 = QtWidgets.QLineEdit(self.opt1_preset1)
        self.t_value1.setGeometry(QtCore.QRect(530, 292, 121, 35))
        self.t_value1.setFont(label_font)
        self.t_value1.setObjectName("t_value1")
        self.t_value1.setValidator(self.onlyInt)

        # self.t_value1 = QtWidgets.QSpinBox(self.opt1_preset1)
        # self.t_value1.setGeometry(QtCore.QRect(530, 292, 121, 35))
        # self.t_value1.setFont(label_font)
        # self.t_value1.setObjectName("t_value1")

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
        self.r_label2.setGeometry(QtCore.QRect(490, 240, 81, 35))
        self.r_label2.setFont(label_font)
        self.r_label2.setText("")
        self.r_label2.setObjectName("r_label2")

        # r VALUE
        self.r_value2 = QtWidgets.QLineEdit(self.opt1_preset2)
        self.r_value2.setGeometry(QtCore.QRect(530, 245, 121, 35))
        self.r_value2.setFont(label_font)
        self.r_value2.setObjectName("r_value2")
        self.r_value2.setValidator(self.onlyInt)

        # self.r_value2 = QtWidgets.QSpinBox(self.opt1_preset2)
        # self.r_value2.setGeometry(QtCore.QRect(530, 245, 121, 35))
        # self.r_value2.setFont(label_font)
        # # self.r_value2.setText("")
        # self.r_value2.setObjectName("r_value2")
        # # self.r_value2.setValidator(self.onlyInt)

        # t LABEL
        self.t_label2 = QtWidgets.QLabel(self.opt1_preset2)
        self.t_label2.setGeometry(QtCore.QRect(490, 290, 81, 35))
        self.t_label2.setFont(label_font)
        self.t_label2.setText("")
        self.t_label2.setObjectName("t_label2")

        # t VALUE
        self.t_value2 = QtWidgets.QLineEdit(self.opt1_preset2)
        self.t_value2.setGeometry(QtCore.QRect(530, 292, 121, 35))
        self.t_value2.setFont(label_font)
        self.t_value2.setObjectName("t_value2")
        self.t_value2.setValidator(self.onlyInt)

        # self.t_value2 = QtWidgets.QSpinBox(self.opt1_preset2)
        # self.t_value2.setGeometry(QtCore.QRect(530, 292, 121, 35))
        # self.t_value2.setFont(label_font)
        # self.t_value2.setObjectName("t_value2")

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
        self.r_label3.setGeometry(QtCore.QRect(490, 240, 81, 35))
        self.r_label3.setFont(label_font)
        self.r_label3.setText("")
        self.r_label3.setObjectName("r_label3")

        # r VALUE
        self.r_value3 = QtWidgets.QLineEdit(self.opt1_preset3)
        self.r_value3.setGeometry(QtCore.QRect(530, 245, 121, 35))
        self.r_value3.setFont(label_font)
        self.r_value3.setObjectName("r_value3")
        self.r_value3.setValidator(self.onlyInt)

        # self.r_value3 = QtWidgets.QSpinBox(self.opt1_preset3)
        # self.r_value3.setGeometry(QtCore.QRect(530, 245, 121, 35))
        # self.r_value3.setFont(label_font)
        # # self.r_value3.setText("")
        # self.r_value3.setObjectName("r_value3")
        # # self.r_value3.setValidator(self.onlyInt)

        # t LABEL
        self.t_label3 = QtWidgets.QLabel(self.opt1_preset3)
        self.t_label3.setGeometry(QtCore.QRect(490, 290, 81, 35))
        self.t_label3.setFont(label_font)
        self.t_label3.setText("")
        self.t_label3.setObjectName("t_label3")

        # t VALUE
        self.t_value3 = QtWidgets.QLineEdit(self.opt1_preset3)
        self.t_value3.setGeometry(QtCore.QRect(530, 292, 121, 35))
        self.t_value3.setFont(label_font)
        self.t_value3.setObjectName("t_value3")
        self.t_value3.setValidator(self.onlyInt)

        # self.t_value3 = QtWidgets.QSpinBox(self.opt1_preset3)
        # self.t_value3.setGeometry(QtCore.QRect(530, 292, 121, 35))
        # self.t_value3.setFont(label_font)
        # self.t_value3.setObjectName("t_value3")

        self.opt1_preset_page.addWidget(self.opt1_preset3)

        ######################
        ###### PRESET 4 ######
        ######################
        self.opt1_preset4 = QtWidgets.QWidget()
        self.opt1_preset4.setObjectName("opt1_preset4")

        # PI LABEL
        self.pi_label4 = QtWidgets.QLabel(self.opt1_preset4)
        self.pi_label4.setGeometry(QtCore.QRect(165, 247, 71, 31))
        self.pi_label4.setFont(label_font)
        self.pi_label4.setObjectName("pi_label")

        # PI VALUE
        self.pi_value4 = QtWidgets.QLabel(self.opt1_preset4)
        self.pi_value4.setGeometry(QtCore.QRect(200, 255, 81, 21))
        self.pi_value4.setFont(label_font)
        self.pi_value4.setFrameShape(QtWidgets.QFrame.Panel)
        self.pi_value4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pi_value4.setText("")
        self.pi_value4.setObjectName("pi_value")

        # r LABEL
        self.r_label4 = QtWidgets.QLabel(self.opt1_preset4)
        self.r_label4.setGeometry(QtCore.QRect(490, 240, 81, 35))
        self.r_label4.setFont(label_font)
        self.r_label4.setText("")
        self.r_label4.setObjectName("r_label")

        # r VALUE
        self.r_value4 = QtWidgets.QLineEdit(self.opt1_preset4)
        self.r_value4.setGeometry(QtCore.QRect(530, 245, 121, 35))
        self.r_value4.setFont(label_font)
        self.r_value4.setObjectName("r_value")
        self.r_value4.setValidator(self.onlyInt)

        # self.r_value4 = QtWidgets.QSpinBox(self.opt1_preset4)
        # self.r_value4.setGeometry(QtCore.QRect(530, 245, 121, 35))
        # self.r_value4.setFont(label_font)
        # # self.r_value4.setText("")
        # self.r_value4.setObjectName("r_value")
        # # self.r_value4.setValidator(self.onlyInt)

        # t LABEL
        self.t_label4 = QtWidgets.QLabel(self.opt1_preset4)
        self.t_label4.setGeometry(QtCore.QRect(395, 290, 215, 35))
        self.t_label4.setFont(label_font)
        self.t_label4.setText("")
        self.t_label4.setObjectName("t_label")

        # t VALUE
        self.t_value4 = QtWidgets.QLineEdit(self.opt1_preset4)
        self.t_value4.setGeometry(QtCore.QRect(530, 292, 121, 35))
        self.t_value4.setFont(label_font)
        self.t_value4.setObjectName("t_value")
        self.t_value4.setValidator(self.onlyInt)

        # self.t_value4 = QtWidgets.QDoubleSpinBox(self.opt1_preset4)
        # self.t_value4.setGeometry(QtCore.QRect(530, 292, 121, 35))
        # self.t_value4.setFont(label_font)
        # self.t_value4.setObjectName("t_value")

        self.opt1_preset_page.addWidget(self.opt1_preset4)

        ######################
        ###### PRESET 5 ######
        ######################
        self.opt1_preset5 = QtWidgets.QWidget()
        self.opt1_preset5.setObjectName("opt1_preset5")

        # PI LABEL
        self.pi_label5 = QtWidgets.QLabel(self.opt1_preset5)
        self.pi_label5.setGeometry(QtCore.QRect(165, 247, 71, 31))
        self.pi_label5.setFont(label_font)
        self.pi_label5.setObjectName("pi_label5")

        # PI VALUE
        self.pi_value5 = QtWidgets.QLabel(self.opt1_preset5)
        self.pi_value5.setGeometry(QtCore.QRect(200, 255, 81, 21))
        self.pi_value5.setFont(label_font)
        self.pi_value5.setFrameShape(QtWidgets.QFrame.Panel)
        self.pi_value5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pi_value5.setText("")
        self.pi_value5.setObjectName("pi_value5")

        # r LABEL
        self.r_label5 = QtWidgets.QLabel(self.opt1_preset5)
        self.r_label5.setGeometry(QtCore.QRect(490, 240, 81, 35))
        self.r_label5.setFont(label_font)
        self.r_label5.setText("")
        self.r_label5.setObjectName("r_label5")

        # r VALUE
        self.r_value5 = QtWidgets.QLineEdit(self.opt1_preset5)
        self.r_value5.setGeometry(QtCore.QRect(530, 245, 121, 35))
        self.r_value5.setFont(label_font)
        self.r_value5.setObjectName("r_value5")
        self.r_value5.setValidator(self.onlyInt)

        # self.r_value5 = QtWidgets.QSpinBox(self.opt1_preset5)
        # self.r_value5.setGeometry(QtCore.QRect(530, 245, 121, 35))
        # self.r_value5.setFont(label_font)
        # # self.r_value5.setText("")
        # self.r_value5.setObjectName("r_value5")
        # # self.r_value5.setValidator(self.onlyInt)

        # t LABEL
        self.t_label5 = QtWidgets.QLabel(self.opt1_preset5)
        self.t_label5.setGeometry(QtCore.QRect(395, 290, 215, 35))
        self.t_label5.setFont(label_font)
        self.t_label5.setText("")
        self.t_label5.setObjectName("t_label5")

        # t VALUE
        self.t_value5 = QtWidgets.QLineEdit(self.opt1_preset5)
        self.t_value5.setGeometry(QtCore.QRect(530, 292, 121, 35))
        self.t_value5.setFont(label_font)
        self.t_value5.setObjectName("t_value5")
        self.t_value5.setValidator(self.onlyInt)

        # self.t_value5 = QtWidgets.QDoubleSpinBox(self.opt1_preset5)
        # self.t_value5.setGeometry(QtCore.QRect(530, 292, 121, 35))
        # self.t_value5.setFont(label_font)
        # self.t_value5.setObjectName("t_value5")

        self.opt1_preset_page.addWidget(self.opt1_preset5)

        ######################
        ###### PRESET 6 ######
        ######################
        self.opt1_preset6 = QtWidgets.QWidget()
        self.opt1_preset6.setObjectName("opt1_preset6")

        # PI LABEL
        self.pi_label6 = QtWidgets.QLabel(self.opt1_preset6)
        self.pi_label6.setGeometry(QtCore.QRect(165, 247, 71, 31))
        self.pi_label6.setFont(label_font)
        self.pi_label6.setObjectName("pi_label6")

        # PI VALUE
        self.pi_value6 = QtWidgets.QLabel(self.opt1_preset6)
        self.pi_value6.setGeometry(QtCore.QRect(200, 255, 81, 21))
        self.pi_value6.setFont(label_font)
        self.pi_value6.setFrameShape(QtWidgets.QFrame.Panel)
        self.pi_value6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pi_value6.setText("")
        self.pi_value6.setObjectName("pi_value6")

        # r LABEL
        self.r_label6 = QtWidgets.QLabel(self.opt1_preset6)
        self.r_label6.setGeometry(QtCore.QRect(490, 240, 81, 35))
        self.r_label6.setFont(label_font)
        self.r_label6.setText("")
        self.r_label6.setObjectName("r_label6")

        # r VALUE
        self.r_value6 = QtWidgets.QLineEdit(self.opt1_preset6)
        self.r_value6.setGeometry(QtCore.QRect(530, 245, 121, 35))
        self.r_value6.setFont(label_font)
        self.r_value6.setObjectName("r_value6")
        self.r_value6.setValidator(self.onlyInt)

        # self.r_value6 = QtWidgets.QSpinBox(self.opt1_preset6)
        # self.r_value6.setGeometry(QtCore.QRect(530, 245, 121, 35))
        # self.r_value6.setFont(label_font)
        # # self.r_value6.setText("")
        # self.r_value6.setObjectName("r_value6")
        # # self.r_value6.setValidator(self.onlyInt)

        # t LABEL
        self.t_label6 = QtWidgets.QLabel(self.opt1_preset6)
        self.t_label6.setGeometry(QtCore.QRect(395, 290, 215, 35))
        self.t_label6.setFont(label_font)
        self.t_label6.setText("")
        self.t_label6.setObjectName("t_label6")

        # t VALUE
        self.t_value6 = QtWidgets.QLineEdit(self.opt1_preset6)
        self.t_value6.setGeometry(QtCore.QRect(530, 292, 121, 35))
        self.t_value6.setFont(label_font)
        self.t_value6.setObjectName("t_value6")
        self.t_value6.setValidator(self.onlyInt)

        # self.t_value6 = QtWidgets.QDoubleSpinBox(self.opt1_preset6)
        # self.t_value6.setGeometry(QtCore.QRect(530, 292, 121, 35))
        # self.t_value6.setFont(label_font)
        # self.t_value6.setObjectName("t_value6")

        self.opt1_preset_page.addWidget(self.opt1_preset6)

        ######################
        ###### PRESET 7 ######
        ######################
        self.opt1_preset7 = QtWidgets.QWidget()
        self.opt1_preset7.setObjectName("opt1_preset7")

        # PI LABEL
        self.pi_label7 = QtWidgets.QLabel(self.opt1_preset7)
        self.pi_label7.setGeometry(QtCore.QRect(165, 247, 71, 31))
        self.pi_label7.setFont(label_font)
        self.pi_label7.setObjectName("pi_label7")

        # PI VALUE
        self.pi_value7 = QtWidgets.QLabel(self.opt1_preset7)
        self.pi_value7.setGeometry(QtCore.QRect(200, 255, 81, 21))
        self.pi_value7.setFont(label_font)
        self.pi_value7.setFrameShape(QtWidgets.QFrame.Panel)
        self.pi_value7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pi_value7.setText("")
        self.pi_value7.setObjectName("pi_value7")

        # r LABEL
        self.r_label7 = QtWidgets.QLabel(self.opt1_preset7)
        self.r_label7.setGeometry(QtCore.QRect(395, 240, 215, 35))
        self.r_label7.setFont(label_font)
        self.r_label7.setText("")
        self.r_label7.setObjectName("r_label7")

        # r VALUE
        self.r_value7 = QtWidgets.QLineEdit(self.opt1_preset7)
        self.r_value7.setGeometry(QtCore.QRect(530, 245, 121, 35))
        self.r_value7.setFont(label_font)
        self.r_value7.setObjectName("r_value7")
        self.r_value7.setValidator(self.onlyInt)

        # t LABEL
        self.t_label7 = QtWidgets.QLabel(self.opt1_preset7)
        self.t_label7.setGeometry(QtCore.QRect(490, 290, 200, 35))
        self.t_label7.setFont(label_font)
        self.t_label7.setText("")
        self.t_label7.setObjectName("t_label7")

        # t VALUE
        self.t_value7 = QtWidgets.QLineEdit(self.opt1_preset7)
        self.t_value7.setGeometry(QtCore.QRect(530, 292, 121, 35))
        self.t_value7.setFont(label_font)
        self.t_value7.setObjectName("t_value7")
        self.t_value7.setValidator(self.onlyInt)

        # self.t_value7 = QtWidgets.QSpinBox(self.opt1_preset7)
        # self.t_value7.setGeometry(QtCore.QRect(530, 292, 121, 35))
        # self.t_value7.setFont(label_font)
        # self.t_value7.setObjectName("t_value7")

        self.opt1_preset_page.addWidget(self.opt1_preset7)

        ######################
        ###### PRESET 8 ######
        ######################
        self.opt1_preset8 = QtWidgets.QWidget()
        self.opt1_preset8.setObjectName("opt1_preset8")

        # PI LABEL
        self.pi_label8 = QtWidgets.QLabel(self.opt1_preset8)
        self.pi_label8.setGeometry(QtCore.QRect(165, 247, 71, 31))
        self.pi_label8.setFont(label_font)
        self.pi_label8.setObjectName("pi_label8")

        # PI VALUE
        self.pi_value8 = QtWidgets.QLabel(self.opt1_preset8)
        self.pi_value8.setGeometry(QtCore.QRect(200, 255, 81, 21))
        self.pi_value8.setFont(label_font)
        self.pi_value8.setFrameShape(QtWidgets.QFrame.Panel)
        self.pi_value8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pi_value8.setText("")
        self.pi_value8.setObjectName("pi_value8")

        # r LABEL
        self.r_label8 = QtWidgets.QLabel(self.opt1_preset8)
        self.r_label8.setGeometry(QtCore.QRect(395, 240, 215, 35))
        self.r_label8.setFont(label_font)
        self.r_label8.setText("")
        self.r_label8.setObjectName("r_label8")

        # r VALUE
        self.r_value8 = QtWidgets.QLineEdit(self.opt1_preset8)
        self.r_value8.setGeometry(QtCore.QRect(530, 245, 121, 35))
        self.r_value8.setFont(label_font)
        self.r_value8.setObjectName("r_value8")
        self.r_value8.setValidator(self.onlyInt)

        # t LABEL
        self.t_label8 = QtWidgets.QLabel(self.opt1_preset8)
        self.t_label8.setGeometry(QtCore.QRect(490, 290, 200, 35))
        self.t_label8.setFont(label_font)
        self.t_label8.setText("")
        self.t_label8.setObjectName("t_label8")

        # t VALUE
        self.t_value8 = QtWidgets.QLineEdit(self.opt1_preset8)
        self.t_value8.setGeometry(QtCore.QRect(530, 292, 121, 35))
        self.t_value8.setFont(label_font)
        self.t_value8.setObjectName("t_value8")
        self.t_value8.setValidator(self.onlyInt)

        # self.t_value8 = QtWidgets.QSpinBox(self.opt1_preset8)
        # self.t_value8.setGeometry(QtCore.QRect(530, 292, 121, 35))
        # self.t_value8.setFont(label_font)
        # self.t_value8.setObjectName("t_value8")

        self.opt1_preset_page.addWidget(self.opt1_preset8)

        ######################
        ###### PRESET 9 ######
        ######################
        self.opt1_preset9 = QtWidgets.QWidget()
        self.opt1_preset9.setObjectName("opt1_preset9")

        # PI LABEL
        self.pi_label9 = QtWidgets.QLabel(self.opt1_preset9)
        self.pi_label9.setGeometry(QtCore.QRect(165, 247, 71, 31))
        self.pi_label9.setFont(label_font)
        self.pi_label9.setObjectName("pi_label")

        # PI VALUE
        self.pi_value9 = QtWidgets.QLabel(self.opt1_preset9)
        self.pi_value9.setGeometry(QtCore.QRect(200, 255, 81, 21))
        self.pi_value9.setFont(label_font)
        self.pi_value9.setFrameShape(QtWidgets.QFrame.Panel)
        self.pi_value9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pi_value9.setText("")
        self.pi_value9.setObjectName("pi_value9")

        # r LABEL
        self.r_label9 = QtWidgets.QLabel(self.opt1_preset9)
        self.r_label9.setGeometry(QtCore.QRect(395, 240, 215, 35))
        self.r_label9.setFont(label_font)
        self.r_label9.setText("")
        self.r_label9.setObjectName("r_label9")

        # r VALUE
        self.r_value9 = QtWidgets.QLineEdit(self.opt1_preset9)
        self.r_value9.setGeometry(QtCore.QRect(530, 245, 121, 35))
        self.r_value9.setFont(label_font)
        self.r_value9.setObjectName("r_value9")
        self.r_value9.setValidator(self.onlyInt)

        # t LABEL
        self.t_label9 = QtWidgets.QLabel(self.opt1_preset9)
        self.t_label9.setGeometry(QtCore.QRect(490, 290, 200, 35))
        self.t_label9.setFont(label_font)
        self.t_label9.setText("")
        self.t_label9.setObjectName("t_label9")

        # t VALUE
        self.t_value9 = QtWidgets.QLineEdit(self.opt1_preset9)
        self.t_value9.setGeometry(QtCore.QRect(530, 292, 121, 35))
        self.t_value9.setFont(label_font)
        self.t_value9.setObjectName("t_value9")
        self.t_value9.setValidator(self.onlyInt)

        # self.t_value9 = QtWidgets.QSpinBox(self.opt1_preset9)
        # self.t_value9.setGeometry(QtCore.QRect(530, 292, 121, 35))
        # self.t_value9.setFont(label_font)
        # self.t_value9.setObjectName("t_value9")

        self.opt1_preset_page.addWidget(self.opt1_preset9)

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
        self.pi_label4.setText(_translate("MainWindow", "π ="))
        self.pi_label5.setText(_translate("MainWindow", "π ="))
        self.pi_label6.setText(_translate("MainWindow", "π ="))
        self.pi_label7.setText(_translate("MainWindow", "π ="))
        self.pi_label8.setText(_translate("MainWindow", "π ="))
        self.pi_label9.setText(_translate("MainWindow", "π ="))

        self.r_label0.setText(_translate("MainWindow", "r ="))
        self.r_label1.setText(_translate("MainWindow", "r ="))
        self.r_label2.setText(_translate("MainWindow", "r = "))
        self.r_label3.setText(_translate("MainWindow", "r = "))
        self.r_label4.setText(_translate("MainWindow", "r ="))
        self.r_label5.setText(_translate("MainWindow", "r = "))
        self.r_label6.setText(_translate("MainWindow", "r = "))
        self.r_label7.setText(_translate("MainWindow", "ls_tabung = "))
        self.r_label8.setText(_translate("MainWindow", "lp_tabung = "))
        self.r_label9.setText(_translate("MainWindow", "v_tabung = "))

        self.t_label1.setText(_translate("MainWindow", "t = "))
        self.t_label2.setText(_translate("MainWindow", "t = "))
        self.t_label3.setText(_translate("MainWindow", "t = "))
        self.t_label4.setText(_translate("MainWindow", "ls_tabung = "))
        self.t_label5.setText(_translate("MainWindow", "lp_tabung = "))
        self.t_label6.setText(_translate("MainWindow", "v_tabung = "))
        self.t_label7.setText(_translate("MainWindow", "t = "))
        self.t_label8.setText(_translate("MainWindow", "t = "))
        self.t_label9.setText(_translate("MainWindow", "t = "))
        self.calculate0.setText(_translate("MainWindow", "HITUNG"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    sys.exit(app.exec_())

# π
