
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
        self.k_page = int()
        self.obj1_value = float()
        self.obj2_value = float()
        self.obj3_value = int()
        self.obj1s_value = str()
        self.obj2s_value = str()
        self.obj3s_value = str()
        self.one_param = bool()
        self.two_param = bool()
        self.output_int = int()
        self.output_str = str()
        self.var_holder1a = dict()
        self.var_holder2a = dict()
        self.var_holder3a = dict()
        self.var_holder1b = dict()
        self.var_holder2b = dict()
        self.var_holder3b = dict()
        print(f"kalkulator index page is {self.k_page}")

        # initialize option button
        self.main_ui.tabung_opt.clicked.connect(
            self.on_kalkulator_page_change1)
        self.main_ui.kerucut_opt.clicked.connect(
            self.on_kalkulator_page_change2)
        self.main_ui.ball_opt.clicked.connect(
            self.on_kalkulator_page_change3)

        # initialize return button
        self.main_ui.return_button0.clicked.connect(
            self.on_kalkulator_page_change0)
        self.main_ui.return_button1.clicked.connect(
            self.on_kalkulator_page_change0)
        self.main_ui.return_button2.clicked.connect(
            self.on_kalkulator_page_change0)

        # initialize on kalkulator page change
        # self.main_ui.kalkulator_page.currentChanged.connect(
        #     self.on_kalkulator_page_change)

        ############################## TABUNG ##############################
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
        self.main_ui.t_value7.textChanged.connect(self.on_sbt_value_change)

        # initialize luas permukaan value user input
        self.main_ui.r_value8.textChanged.connect(self.on_sbr_value_change)
        self.main_ui.t_value8.textChanged.connect(self.on_sbt_value_change)

        # initialize volume value user input
        self.main_ui.r_value9.textChanged.connect(self.on_sbr_value_change)
        self.main_ui.t_value9.textChanged.connect(self.on_sbt_value_change)
        ############################## END T ##############################

        ############################## KERUCUT ##############################
        # initialize r value user input
        self.main_ui.r_value10.textChanged.connect(self.on_sbr_value_change)
        self.main_ui.r_value12.textChanged.connect(self.on_sbr_value_change)
        self.main_ui.r_value13.textChanged.connect(self.on_sbr_value_change)

        self.main_ui.r_value14.textChanged.connect(self.on_sbr_value_change)
        self.main_ui.r_value15.textChanged.connect(self.on_sbr_value_change)
        self.main_ui.r_value16.textChanged.connect(self.on_sbr_value_change)

        # initialize q value user input
        self.main_ui.r_value11.textChanged.connect(self.on_sbr_value_change)
        self.main_ui.s_value13.textChanged.connect(self.on_sbq_value_change)

        # # intialize s value user input
        self.main_ui.t_value11.textChanged.connect(self.on_sbt_value_change)
        self.main_ui.t_value12.textChanged.connect(self.on_sbt_value_change)
        self.main_ui.t_value13.textChanged.connect(self.on_sbt_value_change)

        self.main_ui.t_value14.textChanged.connect(self.on_sbt_value_change)

        # initialize t value user input
        self.main_ui.t_value15.textChanged.connect(self.on_sbt_value_change)
        self.main_ui.t_value16.textChanged.connect(self.on_sbt_value_change)

        # # initialize luas selimut value user input
        self.main_ui.r_value17.textChanged.connect(self.on_sbr_value_change)
        self.main_ui.t_value17.textChanged.connect(self.on_sbt_value_change)

        # # initialize luas permukaan value user input
        self.main_ui.r_value18.textChanged.connect(self.on_sbr_value_change)
        self.main_ui.t_value18.textChanged.connect(self.on_sbt_value_change)

        # # initialize volume value user input
        self.main_ui.r_value19.textChanged.connect(self.on_sbr_value_change)
        self.main_ui.t_value19.textChanged.connect(self.on_sbt_value_change)
        ############################## END KE ##############################

        ############################### BOLA ###############################
        # initialize user r value input
        self.main_ui.r_value20.textChanged.connect(self.on_sbr_value_change)
        self.main_ui.r_value21.textChanged.connect(self.on_sbr_value_change)
        self.main_ui.r_value22.textChanged.connect(self.on_sbr_value_change)
        self.main_ui.r_value23.textChanged.connect(self.on_sbr_value_change)
        # self.main_ui.r_value20.textChanged.connect(self.on_sbr_value_change)
        # self.main_ui.r_value20.textChanged.connect(self.on_sbr_value_change)
        # self.main_ui.r_value20.textChanged.connect(self.on_sbr_value_change)
        # self.main_ui.r_value20.textChanged.connect(self.on_sbr_value_change)
        # self.main_ui.r_value20.textChanged.connect(self.on_sbr_value_change)
        # self.main_ui.r_value20.textChanged.connect(self.on_sbr_value_change)

        ############################## END KE ##############################

        # initialize calculate buttons
        self.main_ui.calculate0.clicked.connect(self.calc_checked)
        self.main_ui.calculate1.clicked.connect(self.calc_checked)
        self.main_ui.calculate2.clicked.connect(self.calc_checked)

        # intialize copy button
        self.main_ui.copy_output0.clicked.connect(self.copy_button)
        self.main_ui.copy_output1.clicked.connect(self.copy_button)
        self.main_ui.copy_output2.clicked.connect(self.copy_button)

        # initialize on preset update
        # tabung preset update
        self.main_ui.tabung_preset.currentIndexChanged.connect(
            self.on_opt1_preset_change)
        self.main_ui.tabung_preset.currentIndexChanged.connect(
            self.calc_method_track)

        # kerucut preset update
        self.main_ui.kerucut_preset.currentIndexChanged.connect(
            self.on_opt2_preset_change)
        self.main_ui.kerucut_preset.currentIndexChanged.connect(
            self.calc_method_track)

        # bola preset update
        self.main_ui.bola_preset.currentIndexChanged.connect(
            self.on_opt3_preset_change)
        self.main_ui.bola_preset.currentIndexChanged.connect(
            self.calc_method_track)

        # initialize event filter
        QtWidgets.qApp.installEventFilter(self)

    # defining on tabung preset change
    def on_opt1_preset_change(self, value):
        self.main_ui.opt1_preset_page.setCurrentIndex(value)

    # defining on kerucut preset change
    def on_opt2_preset_change(self, value):
        self.main_ui.opt2_preset_page.setCurrentIndex(value)

    # defining on bola preset change
    def on_opt3_preset_change(self, value):
        self.main_ui.opt3_preset_page.setCurrentIndex(value)

    # defining copy button
    def copy_button(self):
        pyperclip.copy(self.output_str)

    # defining what calculate button need to do when it clicked
    def calc_checked(self):
        # QtWidgets.QMessageBox.question(
        #     self, "page", f"kalkulator page index is {self.k_page}")
        print("clicked")
        # print(self.calc_page)
        self.c_page = self.calc_page
        if self.obj1_value > 0:
            if self.obj2_value > 0:
                if self.obj3_value > 0:
                    self.calc_method_3(self.c_page)
                self.calc_method_2(self.c_page)
            else:
                self.calc_method_1(self.c_page)
            print(f"c_page contain index {self.c_page}")
            print(f"k_page contain index {self.k_page}")
        else:
            QtWidgets.QMessageBox.question(
                self, "No Value", "No Value hasn't been input")
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
        x_type = type(self.obj2_value)
        print(f"sbt_value = {self.obj2_value} is {x_type}")
        return self.obj2_value

    # defining get spinbox t value
    def on_sbq_value_change(self, value):
        self.obj3s_value = value
        self.obj3_value = int(self.obj3s_value)
        x_type = type(self.obj3_value)
        print(f"sbt_value = {self.obj3_value} is {x_type}")
        return self.obj3_value

    # defining where calculate button located on the preset index
    def calc_method_track(self, value):
        self.calc_page = value
        return self.calc_page

    # defining calling a key based from index preset for 1 parameter functions
    def calc_method_1(self, key_function):
        self.obj2_value = 0
        self.obj3_value = 0
        if self.k_page == 1 or self.k_page == 2:
            self.var_holder_1 = {
                0: br.luas_permukaan_lingkaran(r=self.obj1_value),
            }
        if self.k_page == 3:
            self.var_holder_1 = {
                0: br.luas_permukaan_lingkaran(r=self.obj1_value),
                1: br.luas_permukaan_bola(r=self.obj1_value),
                2: br.keliling_bola(r=self.obj1_value),
                3: br.volume_bola(r=self.obj1_value)
            }
        self.output_int = self.var_holder_1.get(
            key_function, lambda: "Invalid")
        self.output_str = str(self.output_int)

        # intialize user output
        if self.k_page == 1:
            self.main_ui.output0.setText(self.output_str)
        elif self.k_page == 2:
            self.main_ui.output1.setText(self.output_str)
        elif self.k_page == 3:
            self.main_ui.output2.setText(self.output_str)
        else:
            print("Unknown index")

        # print(self.output_str)

    # defining calling key based from index preset for 2 parameters functions
    def calc_method_2(self, key_function):
        if self.k_page == 1:
            self.var_holder_2 = {
                1: br.luas_selimut_tabung(r=self.obj1_value, t=self.obj2_value),
                2: br.luas_permukaan_tabung(r=self.obj1_value, t=self.obj2_value),
                3: br.volume_tabung(r=self.obj1_value, t=self.obj2_value),
                4: abr.tinggi_dengan_ls_tabung(r=self.obj1_value, ls_tabung=self.obj2_value),
                5: abr.tinggi_dengan_lp_tabung(r=self.obj1_value, lp_tabung=self.obj2_value),
                6: abr.tinggi_dengan_volume_tabung(r=self.obj1_value, v_tabung=self.obj2_value),
                7: abr.jari_jari_dengan_ls_tabung(t=self.obj2_value, ls_tabung=self.obj1_value),
                8: abr.jari_jari_dengan_lp_tabung(t=self.obj2_value, lp_tabung=self.obj1_value),
                9: abr.jari_jari_dengan_volume_tabung(t=self.obj2_value, v_tabung=self.obj1_value),
            }
        elif self.k_page == 2:
            self.var_holder_2 = {
                1: br.luas_selimut_kerucut_1(q=self.obj1_value, s=self.obj2_value),
                2: br.luas_selimut_kerucut_2(r=self.obj1_value, s=self.obj2_value),
                4: br.luas_permukaan_kerucut_2(r=self.obj1_value, s=self.obj2_value),
                5: br.volume_kerucut(r=self.obj1_value, t=self.obj2_value)
            }
        else:
            print("No known dict contain 1/3 parameters functions")
        self.output_int = self.var_holder_2.get(
            key_function, lambda: "Invalid")
        self.output_str = str(self.output_int)

        # intialize user output
        if self.k_page == 1:
            self.main_ui.output0.setText(self.output_str)
        elif self.k_page == 2:
            self.main_ui.output1.setText(self.output_str)
        else:
            print(f"{self.k_page} is Uknown index")

        # print(self.output_str)

   # defining calling key based from index preset for 3 parameters functions
    def calc_method_3(self, key_function):
        if self.k_page == 2:
            self.var_holder_3 = {
                3: br.luas_permukaan_kerucut_1(r=self.obj1_value, q=self.obj3_value, s=self.obj2_value)
            }
        else:
            print("No known dict contain 1/2 parameters functions")
        self.output_int = self.var_holder_3.get(
            key_function, lambda: "Invalid")
        self.output_str = str(self.output_int)

        # intialize user output
        self.main_ui.output1.setText(self.output_str)

        # print(self.output_str)

    # defining on kalkulator page change
    def on_kalkulator_page_change0(self):
        VALUE = 0
        self.k_page = VALUE
        self.main_ui.kalkulator_page.setCurrentIndex(VALUE)
        return self.k_page

    # defining on kalkulator page change
    def on_kalkulator_page_change1(self):
        VALUE = 1
        self.k_page = VALUE
        self.main_ui.kalkulator_page.setCurrentIndex(VALUE)
        return self.k_page

    # defining on kalkulator page change
    def on_kalkulator_page_change2(self):
        VALUE = 2
        self.k_page = VALUE
        self.main_ui.kalkulator_page.setCurrentIndex(VALUE)
        return self.k_page

    # defining on kalkulator page change
    def on_kalkulator_page_change3(self):
        VALUE = 3
        self.k_page = VALUE
        self.main_ui.kalkulator_page.setCurrentIndex(VALUE)
        return self.k_page

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
