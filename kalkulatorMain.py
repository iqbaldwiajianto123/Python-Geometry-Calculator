
# Back End For Kalkulator.py

import sys
import pyperclip
from array import array as arr
from kalkulator import *
from fungsiBangunRuang import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow


class Program(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_ui = OptionWindow()
        self.main_ui.setupUi(self)
        self.test_variable = int()
        self.calc_page = int()
        self.obj1_value = int()
        self.obj2_value = int()
        self.obj3_value = int()
        self.obj1s_value = str()
        self.obj2s_value = str()
        self.one_param = bool()
        self.two_param = bool()
        self.output_int = int()
        self.output_str = str()
        self.var_holder1 = {}
        self.var_holder2 = {}
        self.var_holder3 = {}

        # initialize option button
        self.main_ui.tabung_opt.clicked.connect(
            lambda: self.main_ui.kalkulator_page.setCurrentIndex(1))
        self.main_ui.kerucut_opt.clicked.connect(
            lambda: self.main_ui.kalkulator_page.setCurrentIndex(2))
        self.main_ui.ball_opt.clicked.connect(
            lambda: self.main_ui.kalkulator_page.setCurrentIndex(3))
        self.main_ui.return_button0.clicked.connect(
            lambda: self.main_ui.kalkulator_page.setCurrentIndex(0))

        # # initialize user input
        # self.main_ui.r_value0.valueChanged.connect(self.on_sbr_value_change)
        # self.main_ui.r_value1.valueChanged.connect(self.on_sbr_value_change)
        # self.main_ui.r_value2.valueChanged.connect(self.on_sbr_value_change)
        # self.main_ui.r_value3.valueChanged.connect(self.on_sbr_value_change)

        # self.main_ui.t_value1.valueChanged.connect(self.on_sbt_value_change)
        # self.main_ui.t_value2.valueChanged.connect(self.on_sbt_value_change)
        # self.main_ui.t_value3.valueChanged.connect(self.on_sbt_value_change)

        # initialize r value user input
        self.main_ui.r_value0.textChanged.connect(self.on_sbr_value_change)
        self.main_ui.r_value1.textChanged.connect(self.on_sbr_value_change)
        self.main_ui.r_value2.textChanged.connect(self.on_sbr_value_change)
        self.main_ui.r_value3.textChanged.connect(self.on_sbr_value_change)

        self.main_ui.r_value4.textChanged.connect(self.on_sbr_value_change)
        self.main_ui.r_value5.textChanged.connect(self.on_sbr_value_change)
        self.main_ui.r_value6.textChanged.connect(self.on_sbr_value_change)

        # intialize t value user input
        self.main_ui.t_value1.textChanged.connect(self.on_sbt_value_change)
        self.main_ui.t_value2.textChanged.connect(self.on_sbt_value_change)
        self.main_ui.t_value3.textChanged.connect(self.on_sbt_value_change)

        self.main_ui.t_value4.textChanged.connect(self.on_sbt_value_change)
        self.main_ui.t_value5.textChanged.connect(self.on_sbt_value_change)
        self.main_ui.t_value6.textChanged.connect(self.on_sbt_value_change)

        # initialize luas selimut value user input
        self.main_ui.r_value7.textChanged.connect(self.on_sbr_value_change)
        self.main_ui.r_value7.textChanged.connect(self.on_sbt_value_change)

        # initialize luas permukaan value user input
        self.main_ui.r_value8.textChanged.connect(self.on_sbr_value_change)
        self.main_ui.t_value8.textChanged.connect(self.on_sbt_value_change)

        # initialize volume value user input
        self.main_ui.t_value9.textChanged.connect(self.on_sbr_value_change)
        self.main_ui.t_value9.textChanged.connect(self.on_sbt_value_change)

        # initialize calculate buttons
        self.main_ui.calculate0.clicked.connect(self.calc_checked)

        # intialize copy button
        self.main_ui.copy_output0.clicked.connect(self.copy_button)

        # initialize on preset update
        self.main_ui.tabung_preset.currentIndexChanged.connect(
            self.on_opt1_preset_change)
        self.main_ui.tabung_preset.currentIndexChanged.connect(
            self.calc_method_track)

        # initialize event filter
        QtWidgets.qApp.installEventFilter(self)

    # defining on tabung preset change
    def on_opt1_preset_change(self, value):
        self.main_ui.opt1_preset_page.setCurrentIndex(value)
        # print(f"changed preset index to {value}")

    # defining copy button
    def copy_button(self):
        pyperclip.copy(self.output_str)

    # defining what calculate button need to do when it clicked
    def calc_checked(self):
        print("clicked")
        # print(self.calc_page)
        self.c_page = self.calc_page
        if self.obj1_value > 0:
            if self.obj2_value > 0:
                self.calc_method_2(self.c_page)
            else:
                self.calc_method_1(self.c_page)
            print(f"c_page contain index {self.c_page}")
        else:
            print("sbr_value are less than 0")
        print(self.obj1_value)
        print(self.obj2_value)

    # defining get spinbox r value
    def on_sbr_value_change(self, value):
        self.obj1s_value = value
        self.obj1_value = int(self.obj1s_value)
        x_type = type(self.obj1_value)
        print(f"sbr_value = {self.obj1_value} is {x_type}")
        return self.obj1_value

    # defining get spinbox t value
    def on_sbt_value_change(self, value):
        self.obj2s_value = value
        self.obj2_value = int(self.obj2s_value)
        x_type = type(self.obj1_value)
        print(f"sbt_value = {self.obj2_value} is {x_type}")
        return self.obj2_value

    # defining where calculate button located on the preset index
    def calc_method_track(self, value):
        self.calc_page = value
        return self.calc_page

    # defining calling a key based from index preset for 1 parameter functions
    def calc_method_1(self, key_function):
        self.var_holder_1 = {
            0: br.luas_permukaan_lingkaran(r=self.obj1_value),
        }
        self.output_int = self.var_holder_1.get(
            key_function, lambda: "Invalid")
        self.output_str = str(self.output_int)

        # intialize user output
        self.main_ui.output0.setText(self.output_str)

        print(self.output_str)

    # defining calling key based from index preset for 2 parameters functions
    def calc_method_2(self, key_function):
        self.var_holder_2 = {
            1: br.luas_selimut_tabung(r=self.obj1_value, t=self.obj2_value),
            2: br.luas_permukaan_tabung(r=self.obj1_value, t=self.obj2_value),
            3: br.volume_tabung(r=self.obj1_value, t=self.obj2_value),
            4: abr.tinggi_dengan_ls_tabung(r=self.obj1_value, ls_tabung=self.obj2_value),
            5: abr.tinggi_dengan_lp_tabung(r=self.obj1_value, lp_tabung=self.obj2_value),
            6: abr.tinggi_dengan_volume_tabung(r=self.obj1_value, v_tabung=self.obj2_value),
            7: abr.jari_jari_dengan_ls_tabung(t=self.obj2_value, ls_tabung=self.obj1_value),
            8: abr.jari_jari_dengan_lp_tabung(t=self.obj2_value, lp_tabung=self.obj2_value),
            9: abr.jari_jari_dengan_volume_tabung(t=self.obj2_value, v_tabung=self.obj2_value),
        }
        self.output_int = self.var_holder_2.get(
            key_function, lambda: "Invalid")
        self.output_str = str(self.output_int)

        # intialize user output
        self.main_ui.output0.setText(self.output_str)

        print(self.output_str)

    # defining system exception
    def log_uncaught_exceptions(self, ex_cls, ex, tb):
        text = '{}: {}:\n'.format(ex_cls.__name__, ex)
        import traceback
        text += ''.join(traceback.format_tb(tb))

        print(text)
        self.main_ui.QMessageBox.critical(None, 'Error', text)
        quit()

    sys.excepthook = log_uncaught_exceptions

    # defining keypressed events
    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.KeyPress:

            if event.key() == QtCore.Qt.Key_Escape:
                self.main_ui.kalkulator_page.setCurrentIndex(0)
            if event.key() == QtCore.Qt.Key_Enter:
                self.main_ui.calculate0.click()

        return super().eventFilter(obj, event)


if __name__ == '__main__':
    my_app = QtWidgets.QApplication(sys.argv)
    my_prog = Program()
    my_prog.show()
    sys.exit(my_app.exec_())
