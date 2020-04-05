
# Back End For Kalkulator.py

import sys
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
        self.var_holder = {}

        # initialize option button
        self.main_ui.tabung_opt.clicked.connect(
            lambda: self.main_ui.kalkulator_page.setCurrentIndex(1))
        self.main_ui.kerucut_opt.clicked.connect(
            lambda: self.main_ui.kalkulator_page.setCurrentIndex(2))
        self.main_ui.ball_opt.clicked.connect(
            lambda: self.main_ui.kalkulator_page.setCurrentIndex(3))
        self.main_ui.return_button0.clicked.connect(
            lambda: self.main_ui.kalkulator_page.setCurrentIndex(0))

        # initialize calculate buttons
        self.main_ui.calculate0.setDisabled(False)
        # self.main_ui.r_value0.valueChanged.connect()
        self.main_ui.calculate0.clicked.connect(self.calc_checked)

        # initialize on preset update
        self.main_ui.tabung_preset.currentIndexChanged.connect(
            self.on_opt1_preset_change)
        self.main_ui.tabung_preset.currentIndexChanged.connect(
            self.calc_method_track)

        # initialize event filter
        QtWidgets.qApp.installEventFilter(self)

        # functions dict
        # self.var_holder = {
        #     0: "br.luas_permukaan_lingkaran(r)",
        #     1: "br.luas_selimut_tabung(r, t)",
        #     2: "br.luas_permukaan_tabung(r, t)",
        #     3: "br.volume_tabung(r, t)",
        # }

        self.r_value_holder = {
            0: self.main_ui.r_value0,
            1: self.main_ui.r_value1,
        }

        self.t_value_holder = {
            "a_2_1": self.main_ui.t_value1,
            "a_2_2": self.main_ui.t_value2,
        }

        # self.r_var.arr("i")

        # self.var_holder = {
        #     0: br.luas_permukaan_lingkaran(r=self.main_ui.r_value0),
        #     1: br.luas_selimut_tabung(r=self.main_ui.r_value1, t=self.main_ui.t_value1),
        #     2: br.luas_permukaan_tabung(r=self.main_ui.r_value2, t=self.main_ui.t_value2),
        #     3: br.volume_tabung(r=self.main_ui.r_value3, t=self.main_ui.t_value3)
        # }

    def input_filter(self, object, button_name):
        if len(object) > 0:
            self.button_name.setDisabled(False)

    # defining preset changer
    def on_opt1_preset_change(self, value):
        self.opt1_preseted = value
        self.main_ui.opt1_preset_page.setCurrentIndex(value)
        print(f"changed preset index to {value}")

    # defining what calculate button when it checked
    def calc_checked(self):
        print("clicked")

        print(self.calc_page)
        self.c_page = self.calc_page
        print(f"calc button on {self.c_page}")
        self.var_holder = {
            0: br.luas_permukaan_lingkaran(r=self.main_ui.r_value0),
            1: br.luas_selimut_tabung(r=self.main_ui.r_value1, t=self.main_ui.t_value1),
            2: br.luas_permukaan_tabung(r=self.main_ui.r_value2, t=self.main_ui.t_value2),
            3: br.volume_tabung(r=self.main_ui.r_value3, t=self.main_ui.t_value3)
        }
        self.calc_method(self.c_page)

    # defining track where calculate button on the index
    def calc_method_track(self, value):
        self.calc_page = value
        print(self.calc_page)
        return self.calc_page

    # defining wether key is valid
    def valid_key(self, calc_page1):
        self.calc_page1 = calc_page1
        try:
            if self.calc_page1 in self.var_holder:
                print(f"calc button is on {self.calc_page1} page")
                return True
            else:
                print(f"{self.calc_page1} is unknown preset")
                return False
        except:
            return False

    # defining calling a key based from validated key
    def calc_method(self, r):
        x = self.var_holder.get(r, lambda: "Invalid")
        print(x)

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


"""     self.var_holder = {
        0: "br.luas_permukaan_lingkaran(r)",
        1: "br.luas_selimut_tabung(r, t)",
        2: "br.luas_permukaan_tabung(r, t)",
        3: "br.volume_tabung(r, t)",
    } """


"""     self.var_holder = {
        0: br.luas_permukaan_lingkaran(r),
        1: br.luas_selimut_tabung(r, t),
        2: br.luas_permukaan_tabung(r, t),
        3: br.volume_tabung(r, t)
    } """


if __name__ == '__main__':
    my_app = QtWidgets.QApplication(sys.argv)
    my_prog = Program()
    my_prog.show()
    sys.exit(my_app.exec_())
