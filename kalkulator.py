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


button_stylesheet = ("""
        background-color: #006308;
        border-radius: 5px;
        border-color: #006308;
        border-width: 2px;
    """)


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
        self.title1.setGeometry(QtCore.QRect(200, 190, 365, 41))
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
        icon = QtGui.QIcon()
        icon.addFile("H:\Icons\copy-32x32")
        self.copy_output0.setIcon(icon)
        self.copy_output0.setStyleSheet(button_stylesheet)
        self.copy_output0.setText("")
        self.copy_output0.setObjectName("copy_output0")

        # CALCULATE BUTTON
        self.calculate0 = QtWidgets.QPushButton(self.opt1_page)
        self.calculate0.setGeometry(QtCore.QRect(340, 410, 101, 41))
        self.calculate0.setStyleSheet(button_stylesheet)
        self.calculate0.setFont(button_font)
        self.calculate0.setObjectName("calculate0")

        # RETURN BUTTON
        self.return_button0 = QtWidgets.QPushButton(self.opt1_page)
        self.return_button0.setGeometry(QtCore.QRect(30, 20, 41, 31))
        icon = QtGui.QIcon()
        icon.addFile("H:\Icons\Return_32x32")
        self.return_button0.setIcon(icon)
        self.return_button0.setStyleSheet(button_stylesheet)
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

        # KERUCUT PAGE
        self.opt2_page = QtWidgets.QWidget()
        self.opt2_page.setObjectName("opt2_page")

        self.opt2_preset_page = QtWidgets.QStackedWidget(self.opt2_page)
        self.opt2_preset_page.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.opt2_preset_page.setObjectName("opt2_preset_page")

        # OUTPUT
        self.output1 = QtWidgets.QLabel(self.opt2_page)
        self.output1.setGeometry(QtCore.QRect(230, 470, 281, 41))
        self.output1.setFont(button_font)
        self.output1.setAutoFillBackground(True)
        self.output1.setFrameShape(QtWidgets.QFrame.Box)
        self.output1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.output1.setText("")
        self.output1.setObjectName("output1")

        # COPY BUTTON
        self.copy_output1 = QtWidgets.QPushButton(self.opt2_page)
        self.copy_output1.setGeometry(QtCore.QRect(520, 470, 41, 41))
        icon = QtGui.QIcon()
        icon.addFile("H:\Icons\copy-32x32")
        self.copy_output1.setIcon(icon)
        self.copy_output1.setStyleSheet(button_stylesheet)
        self.copy_output1.setText("")
        self.copy_output1.setObjectName("copy_output1")

        # CALCULATE BUTTON
        self.calculate1 = QtWidgets.QPushButton(self.opt2_page)
        self.calculate1.setGeometry(QtCore.QRect(340, 410, 101, 41))
        self.calculate1.setStyleSheet(button_stylesheet)
        self.calculate1.setFont(button_font)
        self.calculate1.setObjectName("calculate1")

        # RETURN BUTTON
        self.return_button1 = QtWidgets.QPushButton(self.opt2_page)
        self.return_button1.setGeometry(QtCore.QRect(30, 20, 41, 31))
        icon = QtGui.QIcon()
        icon.addFile("H:\Icons\Return_32x32")
        self.return_button1.setIcon(icon)
        self.return_button1.setStyleSheet(button_stylesheet)
        self.return_button1.setText("")
        self.return_button1.setObjectName("return_button1")

        # KERUCUT PRESET
        self.kerucut_preset = QtWidgets.QComboBox(self.opt2_page)
        self.kerucut_preset.setGeometry(QtCore.QRect(210, 150, 381, 41))
        self.kerucut_preset.setMaxVisibleItems(4)
        preset_font = QtGui.QFont()
        preset_font.setFamily("Quicksand")
        preset_font.setPointSize(12)
        preset_font.setBold(True)
        preset_font.setWeight(75)
        self.kerucut_preset.setFont(preset_font)
        self.kerucut_preset.setObjectName("kerucut_preset")
        self.kerucut_preset.addItem("")
        self.kerucut_preset.addItem("")
        self.kerucut_preset.addItem("")
        self.kerucut_preset.addItem("")
        self.kerucut_preset.addItem("")
        self.kerucut_preset.addItem("")
        # self.kerucut_preset.addItem("")
        # self.kerucut_preset.addItem("")
        # self.kerucut_preset.addItem("")
        # self.kerucut_preset.addItem("")

        # CALCULATOR TITLE
        self.kerucut_opt_label = QtWidgets.QLabel(self.opt2_page)
        self.kerucut_opt_label.setGeometry(QtCore.QRect(260, 90, 281, 41))
        self.kerucut_opt_label.setFont(title_font)
        self.kerucut_opt_label.setObjectName("kerucut_opt_label")

        self.sub_label1 = QtWidgets.QLabel(self.opt2_page)
        self.sub_label1.setGeometry(QtCore.QRect(350, 210, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.sub_label1.setFont(font)
        self.sub_label1.setObjectName("sub_label1")

        # DEFINING KERUCUT PRESET PAGE
        self.opt2_preset0 = QtWidgets.QWidget()
        self.opt2_preset0.setObjectName("opt2_preset0")
        self.opt2_preset1 = QtWidgets.QWidget()
        self.opt2_preset1.setObjectName("opt2_preset1")
        self.opt2_preset2 = QtWidgets.QWidget()
        self.opt2_preset2.setObjectName("opt2_preset2")
        self.opt2_preset3 = QtWidgets.QWidget()
        self.opt2_preset3.setObjectName("opt2_preset3")
        self.opt2_preset4 = QtWidgets.QWidget()
        self.opt2_preset4.setObjectName("opt2_preset4")
        self.opt2_preset5 = QtWidgets.QWidget()
        self.opt2_preset5.setObjectName("opt2_preset5")
        self.opt2_preset6 = QtWidgets.QWidget()
        self.opt2_preset6.setObjectName("opt2_preset6")
        self.opt2_preset7 = QtWidgets.QWidget()
        self.opt2_preset7.setObjectName("opt2_preset7")
        self.opt2_preset8 = QtWidgets.QWidget()
        self.opt2_preset8.setObjectName("opt2_preset8")
        self.opt2_preset9 = QtWidgets.QWidget()
        self.opt2_preset9.setObjectName("opt2_preset9")

        # DEFINING KERUCUT PI LABEL
        # Setting up kerucut pi value label
        self.pi_label10 = QtWidgets.QLabel(self.opt2_preset0)
        self.pi_label11 = QtWidgets.QLabel(self.opt2_preset1)
        self.pi_label12 = QtWidgets.QLabel(self.opt2_preset2)
        self.pi_label13 = QtWidgets.QLabel(self.opt2_preset3)
        self.pi_label14 = QtWidgets.QLabel(self.opt2_preset4)
        self.pi_label15 = QtWidgets.QLabel(self.opt2_preset5)
        self.pi_label16 = QtWidgets.QLabel(self.opt2_preset6)
        self.pi_label17 = QtWidgets.QLabel(self.opt2_preset7)
        self.pi_label18 = QtWidgets.QLabel(self.opt2_preset8)
        self.pi_label19 = QtWidgets.QLabel(self.opt2_preset9)

        # Setting kerucut pi label geometry
        self.pi_label10.setGeometry(QtCore.QRect(165, 247, 71, 31))
        self.pi_label11.setGeometry(QtCore.QRect(165, 247, 71, 31))
        self.pi_label12.setGeometry(QtCore.QRect(165, 247, 71, 31))
        self.pi_label13.setGeometry(QtCore.QRect(165, 247, 71, 31))
        self.pi_label14.setGeometry(QtCore.QRect(165, 247, 71, 31))
        self.pi_label15.setGeometry(QtCore.QRect(165, 247, 71, 31))
        self.pi_label16.setGeometry(QtCore.QRect(165, 247, 71, 31))
        self.pi_label17.setGeometry(QtCore.QRect(165, 247, 71, 31))
        self.pi_label18.setGeometry(QtCore.QRect(165, 247, 71, 31))
        self.pi_label19.setGeometry(QtCore.QRect(165, 247, 71, 31))

        # Setting kerucut pi label font
        self.pi_label10.setFont(label_font)
        self.pi_label11.setFont(label_font)
        self.pi_label12.setFont(label_font)
        self.pi_label13.setFont(label_font)
        self.pi_label14.setFont(label_font)
        self.pi_label15.setFont(label_font)
        self.pi_label16.setFont(label_font)
        self.pi_label17.setFont(label_font)
        self.pi_label18.setFont(label_font)
        self.pi_label19.setFont(label_font)

        # Setting kerucut pi label name
        self.pi_label10.setObjectName("pi_label10")
        self.pi_label11.setObjectName("pi_label11")
        self.pi_label12.setObjectName("pi_label12")
        self.pi_label13.setObjectName("pi_label13")
        self.pi_label14.setObjectName("pi_label14")
        self.pi_label15.setObjectName("pi_label15")
        self.pi_label16.setObjectName("pi_label16")
        self.pi_label17.setObjectName("pi_label17")
        self.pi_label18.setObjectName("pi_label18")
        self.pi_label19.setObjectName("pi_label19")

        # DEFINING KERUCUT PI VALUE LABEL
        # Setting up pi value label
        self.pi_value10 = QtWidgets.QLabel(self.opt2_preset0)
        self.pi_value11 = QtWidgets.QLabel(self.opt2_preset1)
        self.pi_value12 = QtWidgets.QLabel(self.opt2_preset2)
        self.pi_value13 = QtWidgets.QLabel(self.opt2_preset3)
        self.pi_value14 = QtWidgets.QLabel(self.opt2_preset4)
        self.pi_value15 = QtWidgets.QLabel(self.opt2_preset5)
        self.pi_value16 = QtWidgets.QLabel(self.opt2_preset6)
        self.pi_value17 = QtWidgets.QLabel(self.opt2_preset7)
        self.pi_value18 = QtWidgets.QLabel(self.opt2_preset8)
        self.pi_value19 = QtWidgets.QLabel(self.opt2_preset9)

        # Setting kerucut pi value geometry
        self.pi_value10.setGeometry(QtCore.QRect(200, 255, 81, 21))
        self.pi_value11.setGeometry(QtCore.QRect(200, 255, 81, 21))
        self.pi_value12.setGeometry(QtCore.QRect(200, 255, 81, 21))
        self.pi_value13.setGeometry(QtCore.QRect(200, 255, 81, 21))
        self.pi_value14.setGeometry(QtCore.QRect(200, 255, 81, 21))
        self.pi_value15.setGeometry(QtCore.QRect(200, 255, 81, 21))
        self.pi_value16.setGeometry(QtCore.QRect(200, 255, 81, 21))
        self.pi_value17.setGeometry(QtCore.QRect(200, 255, 81, 21))
        self.pi_value18.setGeometry(QtCore.QRect(200, 255, 81, 21))
        self.pi_value19.setGeometry(QtCore.QRect(200, 255, 81, 21))

        # Setting kerucut pi value font
        self.pi_value10.setFont(label_font)
        self.pi_value11.setFont(label_font)
        self.pi_value12.setFont(label_font)
        self.pi_value13.setFont(label_font)
        self.pi_value14.setFont(label_font)
        self.pi_value15.setFont(label_font)
        self.pi_value16.setFont(label_font)
        self.pi_value17.setFont(label_font)
        self.pi_value18.setFont(label_font)
        self.pi_value19.setFont(label_font)

        # Setting kerucut pi value border
        self.pi_value10.setFrameShape(QtWidgets.QFrame.Panel)
        self.pi_value11.setFrameShape(QtWidgets.QFrame.Panel)
        self.pi_value12.setFrameShape(QtWidgets.QFrame.Panel)
        self.pi_value13.setFrameShape(QtWidgets.QFrame.Panel)
        self.pi_value14.setFrameShape(QtWidgets.QFrame.Panel)
        self.pi_value15.setFrameShape(QtWidgets.QFrame.Panel)
        self.pi_value16.setFrameShape(QtWidgets.QFrame.Panel)
        self.pi_value17.setFrameShape(QtWidgets.QFrame.Panel)
        self.pi_value18.setFrameShape(QtWidgets.QFrame.Panel)
        self.pi_value19.setFrameShape(QtWidgets.QFrame.Panel)

        # Setting kerucut pi value border type
        self.pi_value10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pi_value11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pi_value12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pi_value13.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pi_value14.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pi_value15.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pi_value16.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pi_value17.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pi_value18.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pi_value19.setFrameShadow(QtWidgets.QFrame.Plain)

        # Setting kerucut pi value object name
        self.pi_value10.setObjectName("pi_value10")
        self.pi_value11.setObjectName("pi_value11")
        self.pi_value12.setObjectName("pi_value12")
        self.pi_value13.setObjectName("pi_value13")
        self.pi_value14.setObjectName("pi_value14")
        self.pi_value15.setObjectName("pi_value15")
        self.pi_value16.setObjectName("pi_value16")
        self.pi_value17.setObjectName("pi_value17")
        self.pi_value18.setObjectName("pi_value18")
        self.pi_value19.setObjectName("pi_value19")

        # DEFINING KERUCUT R LABEL VALUE
        # Setting up kerucut r label
        self.r_label10 = QtWidgets.QLabel(self.opt2_preset0)
        self.r_label11 = QtWidgets.QLabel(self.opt2_preset1)
        self.r_label12 = QtWidgets.QLabel(self.opt2_preset2)
        self.r_label13 = QtWidgets.QLabel(self.opt2_preset3)
        self.r_label14 = QtWidgets.QLabel(self.opt2_preset4)
        self.r_label15 = QtWidgets.QLabel(self.opt2_preset5)
        self.r_label16 = QtWidgets.QLabel(self.opt2_preset6)
        self.r_label17 = QtWidgets.QLabel(self.opt2_preset7)
        self.r_label18 = QtWidgets.QLabel(self.opt2_preset8)
        self.r_label19 = QtWidgets.QLabel(self.opt2_preset9)

        # Setting kerucut r label geometry
        self.r_label10.setGeometry(QtCore.QRect(490, 245, 121, 35))
        self.r_label11.setGeometry(QtCore.QRect(490, 245, 121, 35))
        self.r_label12.setGeometry(QtCore.QRect(490, 245, 121, 35))
        self.r_label13.setGeometry(QtCore.QRect(490, 245, 121, 35))
        self.r_label14.setGeometry(QtCore.QRect(490, 245, 121, 35))
        self.r_label15.setGeometry(QtCore.QRect(490, 245, 121, 35))
        self.r_label16.setGeometry(QtCore.QRect(490, 245, 121, 35))
        self.r_label17.setGeometry(QtCore.QRect(395, 240, 215, 35))
        self.r_label18.setGeometry(QtCore.QRect(395, 240, 215, 35))
        self.r_label19.setGeometry(QtCore.QRect(395, 240, 215, 35))

        # Setting kerucut r label font
        self.r_label10.setFont(label_font)
        self.r_label11.setFont(label_font)
        self.r_label12.setFont(label_font)
        self.r_label13.setFont(label_font)
        self.r_label14.setFont(label_font)
        self.r_label15.setFont(label_font)
        self.r_label16.setFont(label_font)
        self.r_label17.setFont(label_font)
        self.r_label18.setFont(label_font)
        self.r_label19.setFont(label_font)

        # Setting kerucut r label name
        self.r_label10.setObjectName("r_label10")
        self.r_label11.setObjectName("r_label11")
        self.r_label12.setObjectName("r_label12")
        self.r_label13.setObjectName("r_label13")
        self.r_label14.setObjectName("r_label14")
        self.r_label15.setObjectName("r_label15")
        self.r_label16.setObjectName("r_label16")
        self.r_label17.setObjectName("r_label17")
        self.r_label18.setObjectName("r_label18")
        self.r_label19.setObjectName("r_label19")

        # DEFINING KERUCUT R VALUE INPUT
        # Setting up kerucut r value input
        self.r_value10 = QtWidgets.QLineEdit(self.opt2_preset0)
        self.r_value11 = QtWidgets.QLineEdit(self.opt2_preset1)
        self.r_value12 = QtWidgets.QLineEdit(self.opt2_preset2)
        self.r_value13 = QtWidgets.QLineEdit(self.opt2_preset3)
        self.r_value14 = QtWidgets.QLineEdit(self.opt2_preset4)
        self.r_value15 = QtWidgets.QLineEdit(self.opt2_preset5)
        self.r_value16 = QtWidgets.QLineEdit(self.opt2_preset6)
        self.r_value17 = QtWidgets.QLineEdit(self.opt2_preset7)
        self.r_value18 = QtWidgets.QLineEdit(self.opt2_preset8)
        self.r_value19 = QtWidgets.QLineEdit(self.opt2_preset9)

        # Setting kerucut r value input geometry
        self.r_value10.setGeometry(QtCore.QRect(530, 245, 121, 35))
        self.r_value11.setGeometry(QtCore.QRect(530, 245, 121, 35))
        self.r_value12.setGeometry(QtCore.QRect(530, 245, 121, 35))
        self.r_value13.setGeometry(QtCore.QRect(530, 245, 121, 35))
        self.r_value14.setGeometry(QtCore.QRect(530, 245, 121, 35))
        self.r_value15.setGeometry(QtCore.QRect(530, 245, 121, 35))
        self.r_value16.setGeometry(QtCore.QRect(530, 245, 121, 35))
        self.r_value17.setGeometry(QtCore.QRect(530, 245, 121, 35))
        self.r_value18.setGeometry(QtCore.QRect(530, 245, 121, 35))
        self.r_value19.setGeometry(QtCore.QRect(530, 245, 121, 35))

        # Setting kerucut r value input font
        self.r_value10.setFont(label_font)
        self.r_value11.setFont(label_font)
        self.r_value12.setFont(label_font)
        self.r_value13.setFont(label_font)
        self.r_value14.setFont(label_font)
        self.r_value15.setFont(label_font)
        self.r_value16.setFont(label_font)
        self.r_value17.setFont(label_font)
        self.r_value18.setFont(label_font)
        self.r_value19.setFont(label_font)

        # Setting kerucut r value input object name
        self.r_value10.setObjectName("r_value10")
        self.r_value11.setObjectName("r_value11")
        self.r_value12.setObjectName("r_value12")
        self.r_value13.setObjectName("r_value13")
        self.r_value14.setObjectName("r_value14")
        self.r_value15.setObjectName("r_value15")
        self.r_value16.setObjectName("r_value16")
        self.r_value17.setObjectName("r_value17")
        self.r_value18.setObjectName("r_value18")
        self.r_value19.setObjectName("r_value19")

        # Setting kerucut r value input validator
        self.r_value10.setValidator(self.onlyInt)
        self.r_value11.setValidator(self.onlyInt)
        self.r_value12.setValidator(self.onlyInt)
        self.r_value13.setValidator(self.onlyInt)
        self.r_value14.setValidator(self.onlyInt)
        self.r_value15.setValidator(self.onlyInt)
        self.r_value16.setValidator(self.onlyInt)
        self.r_value17.setValidator(self.onlyInt)
        self.r_value18.setValidator(self.onlyInt)
        self.r_value19.setValidator(self.onlyInt)

        # DEFINING KERUCUT T VALUE LABEL
        # Setting kerucut t value label
        self.t_label11 = QtWidgets.QLabel(self.opt2_preset1)
        self.t_label12 = QtWidgets.QLabel(self.opt2_preset2)
        self.t_label13 = QtWidgets.QLabel(self.opt2_preset3)
        self.t_label14 = QtWidgets.QLabel(self.opt2_preset4)
        self.t_label15 = QtWidgets.QLabel(self.opt2_preset5)
        self.t_label16 = QtWidgets.QLabel(self.opt2_preset6)
        self.t_label17 = QtWidgets.QLabel(self.opt2_preset7)
        self.t_label18 = QtWidgets.QLabel(self.opt2_preset8)
        self.t_label19 = QtWidgets.QLabel(self.opt2_preset9)

        # Setting kerucut t value label geometry
        self.t_label11.setGeometry(QtCore.QRect(490, 290, 200, 35))
        self.t_label12.setGeometry(QtCore.QRect(490, 290, 200, 35))
        self.t_label13.setGeometry(QtCore.QRect(490, 290, 200, 35))
        self.t_label14.setGeometry(QtCore.QRect(490, 290, 200, 35))
        self.t_label15.setGeometry(QtCore.QRect(490, 290, 200, 35))
        self.t_label16.setGeometry(QtCore.QRect(395, 290, 215, 35))
        self.t_label17.setGeometry(QtCore.QRect(395, 290, 215, 35))
        self.t_label18.setGeometry(QtCore.QRect(395, 290, 215, 35))
        self.t_label19.setGeometry(QtCore.QRect(490, 290, 200, 35))

        # Setting kerucut t value label font
        self.t_label11.setFont(label_font)
        self.t_label12.setFont(label_font)
        self.t_label13.setFont(label_font)
        self.t_label14.setFont(label_font)
        self.t_label15.setFont(label_font)
        self.t_label16.setFont(label_font)
        self.t_label17.setFont(label_font)
        self.t_label18.setFont(label_font)
        self.t_label19.setFont(label_font)

        # Setting kerucut t value label object name
        self.t_label11.setObjectName("t_label11")
        self.t_label12.setObjectName("t_label12")
        self.t_label13.setObjectName("t_label13")
        self.t_label14.setObjectName("t_label14")
        self.t_label15.setObjectName("t_label15")
        self.t_label16.setObjectName("t_label16")
        self.t_label17.setObjectName("t_label17")
        self.t_label18.setObjectName("t_label18")
        self.t_label19.setObjectName("t_label19")

        # DEFINING KERUCUT T VALUE INPUT
        # Setting kerucut t value input
        self.t_value11 = QtWidgets.QLineEdit(self.opt2_preset1)
        self.t_value12 = QtWidgets.QLineEdit(self.opt2_preset2)
        self.t_value13 = QtWidgets.QLineEdit(self.opt2_preset3)
        self.t_value14 = QtWidgets.QLineEdit(self.opt2_preset4)
        self.t_value15 = QtWidgets.QLineEdit(self.opt2_preset5)
        self.t_value16 = QtWidgets.QLineEdit(self.opt2_preset6)
        self.t_value17 = QtWidgets.QLineEdit(self.opt2_preset7)
        self.t_value18 = QtWidgets.QLineEdit(self.opt2_preset8)
        self.t_value19 = QtWidgets.QLineEdit(self.opt2_preset9)

        # Setting kerucut t value input geometry
        self.t_value11.setGeometry(QtCore.QRect(530, 292, 121, 35))
        self.t_value12.setGeometry(QtCore.QRect(530, 292, 121, 35))
        self.t_value13.setGeometry(QtCore.QRect(530, 292, 121, 35))
        self.t_value14.setGeometry(QtCore.QRect(530, 292, 121, 35))
        self.t_value15.setGeometry(QtCore.QRect(530, 292, 121, 35))
        self.t_value16.setGeometry(QtCore.QRect(530, 292, 121, 35))
        self.t_value17.setGeometry(QtCore.QRect(530, 292, 121, 35))
        self.t_value18.setGeometry(QtCore.QRect(530, 292, 121, 35))
        self.t_value19.setGeometry(QtCore.QRect(530, 292, 121, 35))

        # Setting kerucut t value input font
        self.t_value11.setFont(label_font)
        self.t_value12.setFont(label_font)
        self.t_value13.setFont(label_font)
        self.t_value14.setFont(label_font)
        self.t_value15.setFont(label_font)
        self.t_value16.setFont(label_font)
        self.t_value17.setFont(label_font)
        self.t_value18.setFont(label_font)
        self.t_value19.setFont(label_font)

        # Setting kerucut t value input object name
        self.t_value11.setObjectName("t_value11")
        self.t_value12.setObjectName("t_value12")
        self.t_value13.setObjectName("t_value13")
        self.t_value14.setObjectName("t_value14")
        self.t_value15.setObjectName("t_value15")
        self.t_value16.setObjectName("t_value16")
        self.t_value17.setObjectName("t_value17")
        self.t_value18.setObjectName("t_value18")
        self.t_value19.setObjectName("t_value19")

        # Setting kerucut t value input validator
        self.t_value11.setValidator(self.onlyInt)
        self.t_value12.setValidator(self.onlyInt)
        self.t_value13.setValidator(self.onlyInt)
        self.t_value14.setValidator(self.onlyInt)
        self.t_value15.setValidator(self.onlyInt)
        self.t_value16.setValidator(self.onlyInt)
        self.t_value17.setValidator(self.onlyInt)
        self.t_value18.setValidator(self.onlyInt)
        self.t_value19.setValidator(self.onlyInt)

        # DEFINING KERUCUT S VALUE LABEL
        # Setting up kerucut s value label
        self.s_label13 = QtWidgets.QLabel(self.opt2_preset3)

        # Setting kerucut s value label geometry
        self.s_label13.setGeometry(QtCore.QRect(490, 335, 200, 35))

        # Setting kerucut s value label font
        self.s_label13.setFont(label_font)

        # Setting kerucut s value label object name
        self.s_label13.setObjectName("s_label13")

        # DEFINING KERUCUT S VALUE INPUT
        # Setting up kerucut s value input
        self.s_value13 = QtWidgets.QLineEdit(self.opt2_preset3)

        # Setting kerucut s value input geometry
        self.s_value13.setGeometry(QtCore.QRect(530, 332, 121, 35))

        # Setting kerucut s value input font
        self.s_value13.setFont(label_font)

        # Setting kerucut s value input object name
        self.s_value13.setObjectName("s_value13")

        # Setting kerucut s value input validator
        self.s_value13.setValidator(self.onlyInt)

        # ADDING KERUCUT PRESET PAGE
        self.opt2_preset_page.addWidget(self.opt2_preset0)
        self.opt2_preset_page.addWidget(self.opt2_preset1)
        self.opt2_preset_page.addWidget(self.opt2_preset2)
        self.opt2_preset_page.addWidget(self.opt2_preset3)
        self.opt2_preset_page.addWidget(self.opt2_preset4)
        self.opt2_preset_page.addWidget(self.opt2_preset5)
        self.opt2_preset_page.addWidget(self.opt2_preset6)
        self.opt2_preset_page.addWidget(self.opt2_preset7)
        self.opt2_preset_page.addWidget(self.opt2_preset8)
        self.opt2_preset_page.addWidget(self.opt2_preset9)

        self.kalkulator_page.addWidget(self.opt2_page)

        # BOLA PAGE
        self.opt3_page = QtWidgets.QWidget()
        self.opt3_page.setObjectName("opt3_page")

        self.opt3_preset_page = QtWidgets.QStackedWidget(self.opt3_page)
        self.opt3_preset_page.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.opt3_preset_page.setObjectName("opt3_preset_page")

        # OUTPUT
        self.output2 = QtWidgets.QLabel(self.opt3_page)
        self.output2.setGeometry(QtCore.QRect(230, 470, 281, 41))
        self.output2.setFont(button_font)
        self.output2.setAutoFillBackground(True)
        self.output2.setFrameShape(QtWidgets.QFrame.Box)
        self.output2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.output2.setText("")
        self.output2.setObjectName("output2")

        # COPY BUTTON
        self.copy_output2 = QtWidgets.QPushButton(self.opt3_page)
        self.copy_output2.setGeometry(QtCore.QRect(520, 470, 41, 41))
        icon = QtGui.QIcon()
        icon.addFile("H:\Icons\copy-32x32")
        self.copy_output2.setIcon(icon)
        self.copy_output2.setStyleSheet(button_stylesheet)
        self.copy_output2.setText("")
        self.copy_output2.setObjectName("copy_output2")

        # CALCULATE BUTTON
        self.calculate2 = QtWidgets.QPushButton(self.opt3_page)
        self.calculate2.setGeometry(QtCore.QRect(340, 410, 101, 41))
        self.calculate2.setStyleSheet(button_stylesheet)
        self.calculate2.setFont(button_font)
        self.calculate2.setObjectName("calculate2")

        # RETURN BUTTON
        self.return_button2 = QtWidgets.QPushButton(self.opt3_page)
        self.return_button2.setGeometry(QtCore.QRect(30, 20, 41, 31))
        icon = QtGui.QIcon()
        icon.addFile("H:\Icons\Return_32x32")
        self.return_button2.setIcon(icon)
        self.return_button2.setStyleSheet(button_stylesheet)
        self.return_button2.setText("")
        self.return_button2.setObjectName("return_button2")

        # BOLA PRESET
        self.bola_preset = QtWidgets.QComboBox(self.opt3_page)
        self.bola_preset.setGeometry(QtCore.QRect(210, 150, 381, 41))
        self.bola_preset.setMaxVisibleItems(4)
        preset_font = QtGui.QFont()
        preset_font.setFamily("Quicksand")
        preset_font.setPointSize(12)
        preset_font.setBold(True)
        preset_font.setWeight(75)
        self.bola_preset.setFont(preset_font)
        self.bola_preset.setObjectName("kerucut_preset")
        self.bola_preset.addItem("")
        self.bola_preset.addItem("")
        self.bola_preset.addItem("")
        self.bola_preset.addItem("")
        # self.bola_preset.addItem("")
        # self.bola_preset.addItem("")
        # self.bola_preset.addItem("")
        # self.bola_preset.addItem("")
        # self.bola_preset.addItem("")
        # self.bola_preset.addItem("")

        # CALCULATOR TITLE
        self.bola_opt_label = QtWidgets.QLabel(self.opt3_page)
        self.bola_opt_label.setGeometry(QtCore.QRect(260, 90, 281, 41))
        self.bola_opt_label.setFont(title_font)
        self.bola_opt_label.setObjectName("bola_opt_label")

        self.sub_label2 = QtWidgets.QLabel(self.opt3_page)
        self.sub_label2.setGeometry(QtCore.QRect(350, 210, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.sub_label2.setFont(font)
        self.sub_label2.setObjectName("sub_label0")

        # DEFINING BOLA PRESET PAGE
        self.opt3_preset0 = QtWidgets.QWidget()
        self.opt3_preset0.setObjectName("opt3_preset0")
        self.opt3_preset1 = QtWidgets.QWidget()
        self.opt3_preset1.setObjectName("opt3_preset1")
        self.opt3_preset2 = QtWidgets.QWidget()
        self.opt3_preset2.setObjectName("opt3_preset2")
        self.opt3_preset3 = QtWidgets.QWidget()
        self.opt3_preset3.setObjectName("opt3_preset3")
        self.opt3_preset4 = QtWidgets.QWidget()
        self.opt3_preset4.setObjectName("opt3_preset4")
        self.opt3_preset5 = QtWidgets.QWidget()
        self.opt3_preset5.setObjectName("opt3_preset5")
        self.opt3_preset6 = QtWidgets.QWidget()
        self.opt3_preset6.setObjectName("opt2_preset6")
        self.opt3_preset7 = QtWidgets.QWidget()
        self.opt3_preset7.setObjectName("opt3_preset7")
        self.opt3_preset8 = QtWidgets.QWidget()
        self.opt3_preset8.setObjectName("opt3_preset8")
        self.opt3_preset9 = QtWidgets.QWidget()
        self.opt3_preset9.setObjectName("opt3_preset9")

        # DEFINING KERUCUT PI LABEL
        # Setting up kerucut pi value label
        self.pi_label20 = QtWidgets.QLabel(self.opt3_preset0)
        self.pi_label21 = QtWidgets.QLabel(self.opt3_preset1)
        self.pi_label22 = QtWidgets.QLabel(self.opt3_preset2)
        self.pi_label23 = QtWidgets.QLabel(self.opt3_preset3)
        self.pi_label24 = QtWidgets.QLabel(self.opt3_preset4)
        self.pi_label25 = QtWidgets.QLabel(self.opt3_preset5)
        self.pi_label26 = QtWidgets.QLabel(self.opt3_preset6)
        self.pi_label27 = QtWidgets.QLabel(self.opt3_preset7)
        self.pi_label28 = QtWidgets.QLabel(self.opt3_preset8)
        self.pi_label29 = QtWidgets.QLabel(self.opt3_preset9)

        # Setting kerucut pi label geometry
        self.pi_label20.setGeometry(QtCore.QRect(165, 247, 71, 31))
        self.pi_label21.setGeometry(QtCore.QRect(165, 247, 71, 31))
        self.pi_label22.setGeometry(QtCore.QRect(165, 247, 71, 31))
        self.pi_label23.setGeometry(QtCore.QRect(165, 247, 71, 31))
        self.pi_label24.setGeometry(QtCore.QRect(165, 247, 71, 31))
        self.pi_label25.setGeometry(QtCore.QRect(165, 247, 71, 31))
        self.pi_label26.setGeometry(QtCore.QRect(165, 247, 71, 31))
        self.pi_label27.setGeometry(QtCore.QRect(165, 247, 71, 31))
        self.pi_label28.setGeometry(QtCore.QRect(165, 247, 71, 31))
        self.pi_label29.setGeometry(QtCore.QRect(165, 247, 71, 31))

        # Setting kerucut pi label font
        self.pi_label20.setFont(label_font)
        self.pi_label21.setFont(label_font)
        self.pi_label22.setFont(label_font)
        self.pi_label23.setFont(label_font)
        self.pi_label24.setFont(label_font)
        self.pi_label25.setFont(label_font)
        self.pi_label26.setFont(label_font)
        self.pi_label27.setFont(label_font)
        self.pi_label28.setFont(label_font)
        self.pi_label29.setFont(label_font)

        # Setting kerucut pi label name
        self.pi_label20.setObjectName("pi_label20")
        self.pi_label21.setObjectName("pi_label21")
        self.pi_label22.setObjectName("pi_label22")
        self.pi_label23.setObjectName("pi_label23")
        self.pi_label24.setObjectName("pi_label24")
        self.pi_label25.setObjectName("pi_label25")
        self.pi_label26.setObjectName("pi_label26")
        self.pi_label27.setObjectName("pi_label27")
        self.pi_label28.setObjectName("pi_label28")
        self.pi_label29.setObjectName("pi_label29")

        # DEFINING KERUCUT PI VALUE LABEL
        # Setting up pi value label
        self.pi_value20 = QtWidgets.QLabel(self.opt3_preset0)
        self.pi_value21 = QtWidgets.QLabel(self.opt3_preset1)
        self.pi_value22 = QtWidgets.QLabel(self.opt3_preset2)
        self.pi_value23 = QtWidgets.QLabel(self.opt3_preset3)
        self.pi_value24 = QtWidgets.QLabel(self.opt3_preset4)
        self.pi_value25 = QtWidgets.QLabel(self.opt3_preset5)
        self.pi_value26 = QtWidgets.QLabel(self.opt3_preset6)
        self.pi_value27 = QtWidgets.QLabel(self.opt3_preset7)
        self.pi_value28 = QtWidgets.QLabel(self.opt3_preset8)
        self.pi_value29 = QtWidgets.QLabel(self.opt3_preset9)

        # Setting kerucut pi value geometry
        self.pi_value20.setGeometry(QtCore.QRect(200, 255, 81, 21))
        self.pi_value21.setGeometry(QtCore.QRect(200, 255, 81, 21))
        self.pi_value22.setGeometry(QtCore.QRect(200, 255, 81, 21))
        self.pi_value23.setGeometry(QtCore.QRect(200, 255, 81, 21))
        self.pi_value24.setGeometry(QtCore.QRect(200, 255, 81, 21))
        self.pi_value25.setGeometry(QtCore.QRect(200, 255, 81, 21))
        self.pi_value26.setGeometry(QtCore.QRect(200, 255, 81, 21))
        self.pi_value27.setGeometry(QtCore.QRect(200, 255, 81, 21))
        self.pi_value28.setGeometry(QtCore.QRect(200, 255, 81, 21))
        self.pi_value29.setGeometry(QtCore.QRect(200, 255, 81, 21))

        # Setting kerucut pi value font
        self.pi_value20.setFont(label_font)
        self.pi_value21.setFont(label_font)
        self.pi_value22.setFont(label_font)
        self.pi_value23.setFont(label_font)
        self.pi_value24.setFont(label_font)
        self.pi_value25.setFont(label_font)
        self.pi_value26.setFont(label_font)
        self.pi_value27.setFont(label_font)
        self.pi_value28.setFont(label_font)
        self.pi_value29.setFont(label_font)

        # Setting kerucut pi value border
        self.pi_value20.setFrameShape(QtWidgets.QFrame.Panel)
        self.pi_value21.setFrameShape(QtWidgets.QFrame.Panel)
        self.pi_value22.setFrameShape(QtWidgets.QFrame.Panel)
        self.pi_value23.setFrameShape(QtWidgets.QFrame.Panel)
        self.pi_value24.setFrameShape(QtWidgets.QFrame.Panel)
        self.pi_value25.setFrameShape(QtWidgets.QFrame.Panel)
        self.pi_value26.setFrameShape(QtWidgets.QFrame.Panel)
        self.pi_value27.setFrameShape(QtWidgets.QFrame.Panel)
        self.pi_value28.setFrameShape(QtWidgets.QFrame.Panel)
        self.pi_value29.setFrameShape(QtWidgets.QFrame.Panel)

        # Setting kerucut pi value border type
        self.pi_value20.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pi_value21.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pi_value22.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pi_value23.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pi_value24.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pi_value25.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pi_value26.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pi_value27.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pi_value28.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pi_value29.setFrameShadow(QtWidgets.QFrame.Plain)

        # Setting kerucut pi value object name
        self.pi_value20.setObjectName("pi_value20")
        self.pi_value21.setObjectName("pi_value21")
        self.pi_value22.setObjectName("pi_value22")
        self.pi_value23.setObjectName("pi_value23")
        self.pi_value24.setObjectName("pi_value24")
        self.pi_value25.setObjectName("pi_value25")
        self.pi_value26.setObjectName("pi_value26")
        self.pi_value27.setObjectName("pi_value27")
        self.pi_value28.setObjectName("pi_value28")
        self.pi_value29.setObjectName("pi_value29")

        # DEFINING KERUCUT R LABEL VALUE
        # Setting up kerucut r label
        self.r_label20 = QtWidgets.QLabel(self.opt3_preset0)
        self.r_label21 = QtWidgets.QLabel(self.opt3_preset1)
        self.r_label22 = QtWidgets.QLabel(self.opt3_preset2)
        self.r_label23 = QtWidgets.QLabel(self.opt3_preset3)
        self.r_label24 = QtWidgets.QLabel(self.opt3_preset4)
        self.r_label25 = QtWidgets.QLabel(self.opt3_preset5)
        self.r_label26 = QtWidgets.QLabel(self.opt3_preset6)
        self.r_label27 = QtWidgets.QLabel(self.opt3_preset7)
        self.r_label28 = QtWidgets.QLabel(self.opt3_preset8)
        self.r_label29 = QtWidgets.QLabel(self.opt3_preset9)

        # Setting kerucut r label geometry
        self.r_label20.setGeometry(QtCore.QRect(490, 245, 121, 35))
        self.r_label21.setGeometry(QtCore.QRect(490, 245, 121, 35))
        self.r_label22.setGeometry(QtCore.QRect(490, 245, 121, 35))
        self.r_label23.setGeometry(QtCore.QRect(490, 245, 121, 35))
        self.r_label24.setGeometry(QtCore.QRect(490, 245, 121, 35))
        self.r_label25.setGeometry(QtCore.QRect(490, 245, 121, 35))
        self.r_label26.setGeometry(QtCore.QRect(490, 245, 121, 35))
        self.r_label27.setGeometry(QtCore.QRect(395, 240, 215, 35))
        self.r_label28.setGeometry(QtCore.QRect(395, 240, 215, 35))
        self.r_label29.setGeometry(QtCore.QRect(395, 240, 215, 35))

        # Setting kerucut r label font
        self.r_label20.setFont(label_font)
        self.r_label21.setFont(label_font)
        self.r_label22.setFont(label_font)
        self.r_label23.setFont(label_font)
        self.r_label24.setFont(label_font)
        self.r_label25.setFont(label_font)
        self.r_label26.setFont(label_font)
        self.r_label27.setFont(label_font)
        self.r_label28.setFont(label_font)
        self.r_label29.setFont(label_font)

        # Setting kerucut r label name
        self.r_label20.setObjectName("r_label20")
        self.r_label21.setObjectName("r_label21")
        self.r_label22.setObjectName("r_label22")
        self.r_label23.setObjectName("r_label23")
        self.r_label24.setObjectName("r_label24")
        self.r_label25.setObjectName("r_label25")
        self.r_label26.setObjectName("r_label26")
        self.r_label27.setObjectName("r_label27")
        self.r_label28.setObjectName("r_label28")
        self.r_label29.setObjectName("r_label29")

        # DEFINING KERUCUT R VALUE INPUT
        # Setting up kerucut r value input
        self.r_value20 = QtWidgets.QLineEdit(self.opt3_preset0)
        self.r_value21 = QtWidgets.QLineEdit(self.opt3_preset1)
        self.r_value22 = QtWidgets.QLineEdit(self.opt3_preset2)
        self.r_value23 = QtWidgets.QLineEdit(self.opt3_preset3)
        self.r_value24 = QtWidgets.QLineEdit(self.opt3_preset4)
        self.r_value25 = QtWidgets.QLineEdit(self.opt3_preset5)
        self.r_value26 = QtWidgets.QLineEdit(self.opt3_preset6)
        self.r_value27 = QtWidgets.QLineEdit(self.opt3_preset7)
        self.r_value28 = QtWidgets.QLineEdit(self.opt3_preset8)
        self.r_value29 = QtWidgets.QLineEdit(self.opt3_preset9)

        # Setting kerucut r value input geometry
        self.r_value20.setGeometry(QtCore.QRect(530, 245, 121, 35))
        self.r_value21.setGeometry(QtCore.QRect(530, 245, 121, 35))
        self.r_value22.setGeometry(QtCore.QRect(530, 245, 121, 35))
        self.r_value23.setGeometry(QtCore.QRect(530, 245, 121, 35))
        self.r_value24.setGeometry(QtCore.QRect(530, 245, 121, 35))
        self.r_value25.setGeometry(QtCore.QRect(530, 245, 121, 35))
        self.r_value26.setGeometry(QtCore.QRect(530, 245, 121, 35))
        self.r_value27.setGeometry(QtCore.QRect(530, 245, 121, 35))
        self.r_value28.setGeometry(QtCore.QRect(530, 245, 121, 35))
        self.r_value29.setGeometry(QtCore.QRect(530, 245, 121, 35))

        # Setting kerucut r value input font
        self.r_value20.setFont(label_font)
        self.r_value21.setFont(label_font)
        self.r_value22.setFont(label_font)
        self.r_value23.setFont(label_font)
        self.r_value24.setFont(label_font)
        self.r_value25.setFont(label_font)
        self.r_value26.setFont(label_font)
        self.r_value27.setFont(label_font)
        self.r_value28.setFont(label_font)
        self.r_value29.setFont(label_font)

        # Setting kerucut r value input object name
        self.r_value20.setObjectName("r_value10")
        self.r_value21.setObjectName("r_value11")
        self.r_value22.setObjectName("r_value12")
        self.r_value23.setObjectName("r_value13")
        self.r_value24.setObjectName("r_value14")
        self.r_value25.setObjectName("r_value15")
        self.r_value26.setObjectName("r_value16")
        self.r_value27.setObjectName("r_value17")
        self.r_value28.setObjectName("r_value18")
        self.r_value29.setObjectName("r_value19")

        # Setting kerucut r value input validator
        self.r_value20.setValidator(self.onlyInt)
        self.r_value21.setValidator(self.onlyInt)
        self.r_value22.setValidator(self.onlyInt)
        self.r_value23.setValidator(self.onlyInt)
        self.r_value24.setValidator(self.onlyInt)
        self.r_value25.setValidator(self.onlyInt)
        self.r_value26.setValidator(self.onlyInt)
        self.r_value27.setValidator(self.onlyInt)
        self.r_value28.setValidator(self.onlyInt)
        self.r_value29.setValidator(self.onlyInt)

        # # DEFINING BOLA T VALUE LABEL
        # # Setting bola t value label
        # self.t_label21 = QtWidgets.QLabel(self.opt3_preset1)
        # self.t_label22 = QtWidgets.QLabel(self.opt3_preset2)
        # self.t_label23 = QtWidgets.QLabel(self.opt3_preset3)
        # self.t_label24 = QtWidgets.QLabel(self.opt3_preset4)
        # self.t_label25 = QtWidgets.QLabel(self.opt3_preset5)
        # self.t_label26 = QtWidgets.QLabel(self.opt3_preset6)
        # self.t_label27 = QtWidgets.QLabel(self.opt3_preset7)
        # self.t_label28 = QtWidgets.QLabel(self.opt3_preset8)
        # self.t_label29 = QtWidgets.QLabel(self.opt3_preset9)

        # # Setting bola t value label geometry
        # self.t_label21.setGeometry(QtCore.QRect(490, 290, 200, 35))
        # self.t_label22.setGeometry(QtCore.QRect(490, 290, 200, 35))
        # self.t_label23.setGeometry(QtCore.QRect(490, 290, 200, 35))
        # self.t_label24.setGeometry(QtCore.QRect(490, 290, 200, 35))
        # self.t_label25.setGeometry(QtCore.QRect(490, 290, 200, 35))
        # self.t_label26.setGeometry(QtCore.QRect(395, 290, 215, 35))
        # self.t_label27.setGeometry(QtCore.QRect(395, 290, 215, 35))
        # self.t_label28.setGeometry(QtCore.QRect(395, 290, 215, 35))
        # self.t_label29.setGeometry(QtCore.QRect(490, 290, 200, 35))

        # # Setting bola t value label font
        # self.t_label21.setFont(label_font)
        # self.t_label22.setFont(label_font)
        # self.t_label23.setFont(label_font)
        # self.t_label24.setFont(label_font)
        # self.t_label25.setFont(label_font)
        # self.t_label26.setFont(label_font)
        # self.t_label27.setFont(label_font)
        # self.t_label28.setFont(label_font)
        # self.t_label29.setFont(label_font)

        # # Setting bola t value label object name
        # self.t_label21.setObjectName("t_label21")
        # self.t_label22.setObjectName("t_label22")
        # self.t_label23.setObjectName("t_label23")
        # self.t_label24.setObjectName("t_label24")
        # self.t_label25.setObjectName("t_label25")
        # self.t_label26.setObjectName("t_label26")
        # self.t_label27.setObjectName("t_label27")
        # self.t_label28.setObjectName("t_label28")
        # self.t_label29.setObjectName("t_label29")

        # # DEFINING KERUCUT T VALUE INPUT
        # # Setting bola t value input
        # self.t_value21 = QtWidgets.QLineEdit(self.opt3_preset1)
        # self.t_value22 = QtWidgets.QLineEdit(self.opt3_preset2)
        # self.t_value23 = QtWidgets.QLineEdit(self.opt3_preset3)
        # self.t_value24 = QtWidgets.QLineEdit(self.opt3_preset4)
        # self.t_value25 = QtWidgets.QLineEdit(self.opt3_preset5)
        # self.t_value26 = QtWidgets.QLineEdit(self.opt3_preset6)
        # self.t_value27 = QtWidgets.QLineEdit(self.opt3_preset7)
        # self.t_value28 = QtWidgets.QLineEdit(self.opt3_preset8)
        # self.t_value29 = QtWidgets.QLineEdit(self.opt3_preset9)

        # # Setting bola t value input geometry
        # self.t_value21.setGeometry(QtCore.QRect(530, 292, 121, 35))
        # self.t_value22.setGeometry(QtCore.QRect(530, 292, 121, 35))
        # self.t_value23.setGeometry(QtCore.QRect(530, 292, 121, 35))
        # self.t_value24.setGeometry(QtCore.QRect(530, 292, 121, 35))
        # self.t_value25.setGeometry(QtCore.QRect(530, 292, 121, 35))
        # self.t_value26.setGeometry(QtCore.QRect(530, 292, 121, 35))
        # self.t_value27.setGeometry(QtCore.QRect(530, 292, 121, 35))
        # self.t_value28.setGeometry(QtCore.QRect(530, 292, 121, 35))
        # self.t_value29.setGeometry(QtCore.QRect(530, 292, 121, 35))

        # # Setting kerucut t value input font
        # self.t_value21.setFont(label_font)
        # self.t_value22.setFont(label_font)
        # self.t_value23.setFont(label_font)
        # self.t_value24.setFont(label_font)
        # self.t_value25.setFont(label_font)
        # self.t_value26.setFont(label_font)
        # self.t_value27.setFont(label_font)
        # self.t_value28.setFont(label_font)
        # self.t_value29.setFont(label_font)

        # # Setting bola t value input object name
        # self.t_value21.setObjectName("t_value21")
        # self.t_value22.setObjectName("t_value22")
        # self.t_value23.setObjectName("t_value23")
        # self.t_value24.setObjectName("t_value24")
        # self.t_value25.setObjectName("t_value25")
        # self.t_value26.setObjectName("t_value26")
        # self.t_value27.setObjectName("t_value27")
        # self.t_value28.setObjectName("t_value28")
        # self.t_value29.setObjectName("t_value29")

        # # Setting bola t value input validator
        # self.t_value21.setValidator(self.onlyInt)
        # self.t_value22.setValidator(self.onlyInt)
        # self.t_value23.setValidator(self.onlyInt)
        # self.t_value24.setValidator(self.onlyInt)
        # self.t_value25.setValidator(self.onlyInt)
        # self.t_value26.setValidator(self.onlyInt)
        # self.t_value27.setValidator(self.onlyInt)
        # self.t_value28.setValidator(self.onlyInt)
        # self.t_value29.setValidator(self.onlyInt)

        self.opt3_preset_page.addWidget(self.opt3_preset0)
        self.opt3_preset_page.addWidget(self.opt3_preset1)
        self.opt3_preset_page.addWidget(self.opt3_preset2)
        self.opt3_preset_page.addWidget(self.opt3_preset3)
        self.opt3_preset_page.addWidget(self.opt3_preset4)
        self.opt3_preset_page.addWidget(self.opt3_preset5)
        self.opt3_preset_page.addWidget(self.opt3_preset6)
        self.opt3_preset_page.addWidget(self.opt3_preset7)
        self.opt3_preset_page.addWidget(self.opt3_preset8)
        self.opt3_preset_page.addWidget(self.opt3_preset9)

        self.kalkulator_page.addWidget(self.opt3_page)

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
        self.kalkulator_page.setCurrentIndex(0)
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

        self.kerucut_preset.setItemText(0, _translate(
            "MainWindow", "LUAS PERMUKAAN LINGKARAN"))
        self.kerucut_preset.setItemText(
            1, _translate("MainWindow", "LUAS SELIMUT KERUCUT 1"))
        self.kerucut_preset.setItemText(2, _translate(
            "MainWindow", "LUAS SELIMUT KERUCUT 2"))
        self.kerucut_preset.setItemText(
            3, _translate("MainWindow", "LUAS PERMUKAAN KERUCUT 1"))
        self.kerucut_preset.setItemText(
            4, _translate("MainWindow", "LUAS PERMUKAAN KERUCUT 2"))
        self.kerucut_preset.setItemText(
            5, _translate("MainWindow", "VOLUME KERUCUT"))
        # self.kerucut_preset.setItemText(6, _translate(
        #     "MainWindow", "TINGGI DENGAN LUAS SELIMUT KERUCUT"))
        # self.kerucut_preset.setItemText(7, _translate(
        #     "MainWindow", "TINGGI DENGAN LUAS PERMUKAAN KERUCUT"))
        # self.kerucut_preset.setItemText(8, _translate(
        #     "MainWindow", "TINGGI DENGAN VOLUME KERUCUT"))
        # self.kerucut_preset.setItemText(9, _translate(
        #     "MainWindow", "JARI-JARI DENGAN LUAS SELIMUT KERUCUT"))
        # self.kerucut_preset.setItemText(10, _translate(
        #     "MainWindow", "JARI-JARI DENGAN LUAS PERMUKAAN KERUCUT"))
        # self.kerucut_preset.setItemText(11, _translate(
        #     "MainWindow", "JARI-JARI DENGAN VOLUME KERUCUT"))
        self.kerucut_opt_label.setText(
            _translate("MainWindow", "PERHITUNGAN KERUCUT"))

        self.bola_preset.setItemText(0, _translate(
            "MainWindow", "LUAS PERMUKAAN LINGKARAN"))
        self.bola_preset.setItemText(1, _translate(
            "MainWindow", "LUAS PERMUKAAN BOLA"))
        self.bola_preset.setItemText(
            2, _translate("MainWindow", "KELILING BOLA"))
        self.bola_preset.setItemText(
            3, _translate("MainWindow", "VOLUME BOLA"))
        self.bola_opt_label.setText(_translate("MainWindow", "PERHITUNGAN BOLA"))

        self.sub_label0.setText(_translate("MainWindow", "DIKETAHUI"))
        self.sub_label1.setText(_translate("MainWindow", "DIKETAHUI"))

        # TABUNG PI LABEL
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

        # TABUNG R LABEL
        self.r_label0.setText(_translate("MainWindow", "r ="))
        self.r_label1.setText(_translate("MainWindow", "r ="))
        self.r_label2.setText(_translate("MainWindow", "r ="))
        self.r_label3.setText(_translate("MainWindow", "r ="))
        self.r_label4.setText(_translate("MainWindow", "r ="))
        self.r_label5.setText(_translate("MainWindow", "r ="))
        self.r_label6.setText(_translate("MainWindow", "r ="))
        self.r_label7.setText(_translate("MainWindow", "ls_tabung ="))
        self.r_label8.setText(_translate("MainWindow", "lp_tabung ="))
        self.r_label9.setText(_translate("MainWindow", "v_tabung ="))

        # TABUNG T LABEL
        self.t_label1.setText(_translate("MainWindow", "t ="))
        self.t_label2.setText(_translate("MainWindow", "t ="))
        self.t_label3.setText(_translate("MainWindow", "t ="))
        self.t_label4.setText(_translate("MainWindow", "ls_tabung ="))
        self.t_label5.setText(_translate("MainWindow", "lp_tabung ="))
        self.t_label6.setText(_translate("MainWindow", "v_tabung ="))
        self.t_label7.setText(_translate("MainWindow", "t ="))
        self.t_label8.setText(_translate("MainWindow", "t ="))
        self.t_label9.setText(_translate("MainWindow", "t ="))

        # KERUCUT PI LABEL
        self.pi_label10.setText(_translate("MainWindow", "π ="))
        self.pi_label11.setText(_translate("MainWindow", "π ="))
        self.pi_label12.setText(_translate("MainWindow", "π ="))
        self.pi_label13.setText(_translate("MainWindow", "π ="))
        self.pi_label14.setText(_translate("MainWindow", "π ="))
        self.pi_label15.setText(_translate("MainWindow", "π ="))
        self.pi_label16.setText(_translate("MainWindow", "π ="))
        self.pi_label17.setText(_translate("MainWindow", "π ="))
        self.pi_label18.setText(_translate("MainWindow", "π ="))
        self.pi_label19.setText(_translate("MainWindow", "π ="))

        # KERUCUT R LABEL
        self.r_label10.setText(_translate("MainWindow", "r ="))
        self.r_label11.setText(_translate("MainWindow", "q ="))
        self.r_label12.setText(_translate("MainWindow", "r ="))
        self.r_label13.setText(_translate("MainWindow", "r ="))
        self.r_label14.setText(_translate("MainWindow", "r ="))
        self.r_label15.setText(_translate("MainWindow", "r ="))
        self.r_label16.setText(_translate("MainWindow", "r ="))
        self.r_label17.setText(_translate("MainWindow", "ls_kerucut ="))
        self.r_label18.setText(_translate("MainWindow", "lp_kerucut ="))
        self.r_label19.setText(_translate("MainWindow", "v_kerucut ="))

        # KERUCUT T LABEL
        self.t_label11.setText(_translate("MainWindow", "s ="))
        self.t_label12.setText(_translate("MainWindow", "s ="))
        self.t_label13.setText(_translate("MainWindow", "q ="))
        self.t_label14.setText(_translate("MainWindow", "s ="))
        self.t_label15.setText(_translate("MainWindow", "t ="))
        self.t_label16.setText(_translate("MainWindow", "ls_kerucut ="))
        self.t_label17.setText(_translate("MainWindow", "lp_kerucut ="))
        self.t_label18.setText(_translate("MainWindow", "v_kerucut ="))
        self.t_label19.setText(_translate("MainWindow", "t ="))
        # self.t_label20.setText(_translate("MainWindow", "t ="))
        # self.t_label21.setText(_translate("MainWindow", "t ="))

        # KERUCUT S LABEL
        self.s_label13.setText(_translate("MainWindow", "s ="))

        # BOLA PI LABEL
        self.pi_label20.setText(_translate("MainWindow", "π ="))
        self.pi_label21.setText(_translate("MainWindow", "π ="))
        self.pi_label22.setText(_translate("MainWindow", "π ="))
        self.pi_label23.setText(_translate("MainWindow", "π ="))
        self.pi_label24.setText(_translate("MainWindow", "π ="))
        self.pi_label25.setText(_translate("MainWindow", "π ="))
        self.pi_label26.setText(_translate("MainWindow", "π ="))
        self.pi_label27.setText(_translate("MainWindow", "π ="))
        self.pi_label28.setText(_translate("MainWindow", "π ="))
        self.pi_label29.setText(_translate("MainWindow", "π ="))

        # BOLA R LABEL
        self.r_label20.setText(_translate("MainWindow", "r ="))
        self.r_label21.setText(_translate("MainWindow", "r ="))
        self.r_label22.setText(_translate("MainWindow", "r ="))
        self.r_label23.setText(_translate("MainWindow", "r ="))
        self.r_label24.setText(_translate("MainWindow", "r ="))
        self.r_label25.setText(_translate("MainWindow", "r ="))
        self.r_label26.setText(_translate("MainWindow", "r ="))
        self.r_label27.setText(_translate("MainWindow", "ls_kerucut ="))
        self.r_label28.setText(_translate("MainWindow", "lp_kerucut ="))
        self.r_label29.setText(_translate("MainWindow", "v_kerucut ="))

        # BOLA T LABEL
        # self.t_label21.setText(_translate("MainWindow", "s ="))
        # self.t_label22.setText(_translate("MainWindow", "s ="))
        # self.t_label23.setText(_translate("MainWindow", "q ="))
        # self.t_label24.setText(_translate("MainWindow", "s ="))
        # self.t_label25.setText(_translate("MainWindow", "t ="))
        # self.t_label26.setText(_translate("MainWindow", "ls_kerucut ="))
        # self.t_label27.setText(_translate("MainWindow", "lp_kerucut ="))
        # self.t_label28.setText(_translate("MainWindow", "v_kerucut ="))
        # self.t_label29.setText(_translate("MainWindow", "t ="))

        self.calculate0.setText(_translate("MainWindow", "HITUNG"))
        self.calculate1.setText(_translate("MainWindow", "HITUNG"))
        self.calculate2.setText(_translate("MainWindow", "HITUNG"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    sys.exit(app.exec_())

# π
