import sys
import json

import os
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QApplication, QFileDialog, QPushButton, \
    QWidget, QAction, QTabWidget, QVBoxLayout, QHBoxLayout, QErrorMessage,QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtWidgets

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 tabs'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.table_widget1 = MyTableWidget(self)
        self.table_widget2 = MyTableWidget(self)
        self.table_widget3 = MyTableWidget(self)
        self.table_widget4 = MyTableWidget(self)
        self.setCentralWidget(self.table_widget1)
        self.setCentralWidget(self.table_widget2)
        self.setCentralWidget(self.table_widget3)
        self.setCentralWidget(self.table_widget4)

        self.show()


class MyTableWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tabs.resize(300, 200)

        # Add tabs
        self.tabs.addTab(self.tab1, "FinPlate")
        self.tabs.addTab(self.tab2, "TensionMember")
        self.tabs.addTab(self.tab3, "BCEndPlate")
        self.tabs.addTab(self.tab4, "CleatAngle")

        # Create first tab
        self.tab1.layout = QHBoxLayout(self)
        self.pushButton1 = QPushButton("Load Inputs")
        self.tab1.layout.addWidget(self.pushButton1)
        self.tab1.setLayout(self.tab1.layout)
        self.pushButton1.move(100, 50)
        self.pushButton1.clicked.connect(self.on_click_button1)
        self.pushButton = QPushButton("Validate")
        self.tab1.layout.addWidget(self.pushButton)
        self.tab1.setLayout(self.tab1.layout)
        self.pushButton.move(190, 50)
        self.pushButton.clicked.connect(self.get_column_data1)
        self.pushButton2 = QPushButton("Submit")
        self.tab1.layout.addWidget(self.pushButton2)
        self.tab1.setLayout(self.tab1.layout)
        self.pushButton2.move(280, 50)
        self.pushButton2.clicked.connect(self.save_text1)
        self.tab1.setLayout(self.tab1.layout)
        self.table_widget1 = QTableWidget(self)
        self.table_widget1.setRowCount(15)
        self.table_widget1.setColumnCount(7)
        self.table_widget1.setHorizontalHeaderLabels(
            ['ID', 'Connection Type', 'Axial Load', 'Shear Load', 'Bolt Diameter', 'Bolt Grade', 'Plate thickness'])
        self.tab1.layout.addWidget(self.table_widget1)
        self.tab1.setLayout(self.tab1.layout)

        self.tab2.layout = QHBoxLayout(self)
        self.pushButton3 = QPushButton("Load Inputs1")
        self.tab2.layout.addWidget(self.pushButton3)
        self.tab2.setLayout(self.tab2.layout)
        self.pushButton3.move(100, 50)
        self.pushButton3.clicked.connect(self.on_click_button2)
        self.pushButton4 = QPushButton("Validate1")
        self.tab2.layout.addWidget(self.pushButton4)
        self.tab2.setLayout(self.tab2.layout)
        self.pushButton4.move(190, 50)
        self.pushButton4.clicked.connect(self.get_column_data2)
        self.pushButton5 = QPushButton("Submit1")
        self.tab2.layout.addWidget(self.pushButton5)
        self.tab2.setLayout(self.tab2.layout)
        self.pushButton5.move(280, 50)
        self.pushButton5.clicked.connect(self.save_text2)
        self.tab2.setLayout(self.tab2.layout)
        self.table_widget2 = QTableWidget(self)
        self.table_widget2.setRowCount(15)
        self.table_widget2.setColumnCount(5)
        self.table_widget2.setHorizontalHeaderLabels(
            ['ID', 'Member Length', 'Tensile Load', 'Support Condition at End 1', 'Support Condition at End 2'])
        self.tab2.layout.addWidget(self.table_widget2)
        self.tab2.setLayout(self.tab2.layout)

        self.tab3.layout = QHBoxLayout(self)
        self.pushButton6 = QPushButton("Load Inputs")
        self.tab3.layout.addWidget(self.pushButton6)
        self.tab3.setLayout(self.tab3.layout)
        self.pushButton6.move(100, 50)
        self.pushButton6.clicked.connect(self.on_click_button3)
        self.pushButton7 = QPushButton("Validate")
        self.tab3.layout.addWidget(self.pushButton7)
        self.tab3.setLayout(self.tab3.layout)
        self.pushButton7.move(190, 50)
        self.pushButton7.clicked.connect(self.get_column_data3)
        self.pushButton8 = QPushButton("Submit")
        self.tab3.layout.addWidget(self.pushButton8)
        self.tab3.setLayout(self.tab2.layout)
        self.pushButton8.move(280, 50)
        self.pushButton8.clicked.connect(self.save_text3)
        self.tab3.setLayout(self.tab3.layout)
        self.table_widget3 = QTableWidget(self)
        self.table_widget3.setRowCount(15)
        self.table_widget3.setColumnCount(8)
        self.table_widget3.setHorizontalHeaderLabels(
            ['ID', 'Connection Type', 'Shear Load', 'Axial Load', 'Moment Load', 'Bolt Diameter', 'Bolt Grade',
             'Plate thickness'])
        self.tab3.layout.addWidget(self.table_widget3)
        self.tab3.setLayout(self.tab3.layout)

        self.tab4.layout = QHBoxLayout(self)
        self.pushButton9 = QPushButton("Load Inputs")
        self.tab4.layout.addWidget(self.pushButton9)
        self.tab4.setLayout(self.tab4.layout)
        self.pushButton9.move(100, 50)
        self.pushButton9.clicked.connect(self.on_click_button4)
        self.pushButton10 = QPushButton("Validate")
        self.tab4.layout.addWidget(self.pushButton10)
        self.tab4.setLayout(self.tab4.layout)
        self.pushButton10.move(190, 50)
        self.pushButton10.clicked.connect(self.get_column_data4)
        self.pushButton11 = QPushButton("Submit")
        self.tab4.layout.addWidget(self.pushButton11)
        self.tab4.setLayout(self.tab4.layout)
        self.pushButton11.move(280, 50)
        self.pushButton11.clicked.connect(self.save_text4)
        self.tab4.setLayout(self.tab4.layout)
        self.table_widget4 = QTableWidget(self)
        self.table_widget4.setRowCount(15)
        self.table_widget4.setColumnCount(6)
        self.table_widget4.setHorizontalHeaderLabels(
            ['ID', 'Angle Leg 1', 'Angle Leg 2', 'Angle Thickness' 'Shear Load', 'Bolt Diameter', 'Bolt Grade'])
        self.tab4.layout.addWidget(self.table_widget4)
        self.tab4.setLayout(self.tab4.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    @pyqtSlot()
    def on_click_button1(self):
        # print("Hello")
        path = QFileDialog.getOpenFileName(self, 'Open CSV', os.getenv('HOME'), 'CSV(*.csv)')
        print(path)
        if (path[0] != ""):
            infile = open(path[0], "r")
            lines = infile.readlines()
            infile.close()
            self.table_widget1.setRowCount(len(lines))
            print("lines   ", lines)
            for i in range(0, len(lines)):
                tokens = lines[i].strip().split(",")
                id1 = QTableWidgetItem(tokens[0])
                conn = QTableWidgetItem(tokens[1])
                axial = QTableWidgetItem(tokens[2])
                shear = QTableWidgetItem(tokens[3])
                bolt = QTableWidgetItem(tokens[4])
                boltg = QTableWidgetItem(tokens[5])
                plate = QTableWidgetItem(tokens[6])
                self.table_widget1.setItem(i, 0, id1)
                self.table_widget1.setItem(i, 1, conn)
                self.table_widget1.setItem(i, 2, axial)
                self.table_widget1.setItem(i, 3, shear)
                self.table_widget1.setItem(i, 4, bolt)
                self.table_widget1.setItem(i, 5, boltg)
                self.table_widget1.setItem(i, 6, plate)
            self.table_widget1.resizeColumnsToContents()
    def on_click_button2(self):
        # print("Hello")
        path = QFileDialog.getOpenFileName(self, 'Open CSV', os.getenv('HOME'), 'CSV(*.csv)')
        print(path)
        if (path[0] != ""):
            infile = open(path[0], "r")
            lines = infile.readlines()
            infile.close()
            self.table_widget2.setRowCount(len(lines))
            print("lines   ", lines)
            for i in range(0, len(lines)):
                tokens = lines[i].strip().split(",")
                id1 = QTableWidgetItem(tokens[0])
                conn = QTableWidgetItem(tokens[1])
                axial = QTableWidgetItem(tokens[2])
                shear = QTableWidgetItem(tokens[3])
                bolt = QTableWidgetItem(tokens[4])
                self.table_widget2.setItem(i, 0, id1)
                self.table_widget2.setItem(i, 1, conn)
                self.table_widget2.setItem(i, 2, axial)
                self.table_widget2.setItem(i, 3, shear)
                self.table_widget2.setItem(i, 4, bolt)
            self.table_widget2.resizeColumnsToContents()
    def on_click_button3(self):
        # print("Hello")
        path = QFileDialog.getOpenFileName(self, 'Open CSV', os.getenv('HOME'), 'CSV(*.csv)')
        print(path)
        if (path[0] != ""):
            infile = open(path[0], "r")
            lines = infile.readlines()
            infile.close()
            self.table_widget3.setRowCount(len(lines))
            print("lines   ", lines)
            for i in range(0, len(lines)):
                tokens = lines[i].strip().split(",")
                id1 = QTableWidgetItem(tokens[0])
                conn = QTableWidgetItem(tokens[1])
                axial = QTableWidgetItem(tokens[2])
                shear = QTableWidgetItem(tokens[3])
                bolt = QTableWidgetItem(tokens[4])
                boltg = QTableWidgetItem(tokens[5])
                plate = QTableWidgetItem(tokens[6])
                plate1 = QTableWidgetItem(tokens[7])
                self.table_widget3.setItem(i, 0, id1)
                self.table_widget3.setItem(i, 1, conn)
                self.table_widget3.setItem(i, 2, axial)
                self.table_widget3.setItem(i, 3, shear)
                self.table_widget3.setItem(i, 4, bolt)
                self.table_widget3.setItem(i, 5, boltg)
                self.table_widget3.setItem(i, 6, plate)
                self.table_widget3.setItem(i, 7, plate1)
            self.table_widget3.resizeColumnsToContents()
    def on_click_button4(self):
        # print("Hello")
        path = QFileDialog.getOpenFileName(self, 'Open CSV', os.getenv('HOME'), 'CSV(*.csv)')
        print(path)
        if (path[0] != ""):
            infile = open(path[0], "r")
            lines = infile.readlines()
            infile.close()
            self.table_widget4.setRowCount(len(lines))
            print("lines   ", lines)
            for i in range(0, len(lines)):
                tokens = lines[i].strip().split(",")
                id1 = QTableWidgetItem(tokens[0])
                conn = QTableWidgetItem(tokens[1])
                axial = QTableWidgetItem(tokens[2])
                shear = QTableWidgetItem(tokens[3])
                bolt = QTableWidgetItem(tokens[4])
                boltg = QTableWidgetItem(tokens[5])

                self.table_widget4.setItem(i, 0, id1)
                self.table_widget4.setItem(i, 1, conn)
                self.table_widget4.setItem(i, 2, axial)
                self.table_widget4.setItem(i, 3, shear)
                self.table_widget4.setItem(i, 4, bolt)
                self.table_widget4.setItem(i, 5, boltg)

            self.table_widget4.resizeColumnsToContents()

    def get_column_data1(self):
        data = []
        data1 = []
        for k in range(self.table_widget1.rowCount()):
            data1.append(self.table_widget1.item(k, 0).text())

        # print(data1)

        def checkIfDuplicates_1(data1):
            if len(data1) == len(set(data1)):
                return False
            else:
                return True

        result = checkIfDuplicates_1(data1)

        # print(self.table_widget1.item(0, 5).text())
        column = self.table_widget1.columnCount()
        for j in range(0, column):
            for i in range(self.table_widget1.rowCount()):
                data.append(self.table_widget1.item(i, j).text())

                # print(self.table_widget1.item(0,9).text())

                def valid_number(str):
                    i = 0
                    j = len(str) - 1

                    # Handling whitespaces
                    while i < len(str) and str[i] == ' ':
                        i += 1
                    while j >= 0 and str[j] == ' ':
                        j -= 1

                    if i > j:
                        return False

                    # if string is of length 1 and the only
                    # character is not a digit
                    if (i == j and not (str[i] >= '0' and
                                        str[i] <= '9')):
                        return False

                    # If the 1st char is not '+', '-', '.' or digit
                    if (str[i] != '.' and str[i] != '+' and
                            str[i] != '-' and not (str[i] >= '0' and
                                                   str[i] <= '9')):
                        return False

                    # To check if a '.' or 'e' is found in given
                    # string.We use this flag to make sure that
                    # either of them appear only once.
                    flagDotOrE = False

                    for i in range(j + 1):

                        # If any of the char does not belong to
                        # {digit, +, -,., e}
                        if (str[i] != 'e' and str[i] != '.' and
                                str[i] != '+' and str[i] != '-' and not
                                (str[i] >= '0' and str[i] <= '9')):
                            return False

                        if str[i] == '.':

                            # check if the char e has already
                            # occured before '.' If yes, return 0
                            if flagDotOrE:
                                return False
                            if i + 1 > len(str):
                                return False
                            if (not (str[i + 1] >= '0' and
                                     str[i + 1] <= '9')):
                                return False
                        elif str[i] == 'e':

                            # set flagDotOrE = 1 when e is encountered.
                            flagDotOrE = True

                            # if there is no digit before e
                            if (not (str[i - 1] >= '0' and
                                     str[i - 1] <= '9')):
                                return False

                            # if e is the last character
                            if i + 1 > len(str):
                                return False

                            # if e is not followed by
                            # '+', '-' or a digit
                            if (str[i + 1] != '+' and str[i + 1] != '-' and
                                    (str[i + 1] >= '0' and str[i] <= '9')):
                                return False

                    # If the string skips all the
                    # above cases, it must be a numeric string
                    return True

                if not valid_number(self.table_widget1.item(i, j).text()) or result == True:

                    # print("****")
                    # print("This is a string")
                    # print(self.table_widget1.item(i, j).text())
                    # print("****")
                    # print(self.table_widget1.item(i,j).text())

                    msg = QMessageBox()
                    msg.setWindowTitle("Error")
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("Check Your Entry ")
                    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

                    x = msg.exec()
    def get_column_data2(self):
        data = []
        data1 = []
        for k in range(self.table_widget2.rowCount()):
            data1.append(self.table_widget2.item(k, 0).text())

        # print(data1)

        def checkIfDuplicates_1(data1):
            if len(data1) == len(set(data1)):
                return False
            else:
                return True

        result = checkIfDuplicates_1(data1)

        # print(self.table_widget1.item(0, 5).text())
        column = self.table_widget2.columnCount()
        for j in range(0, column):
            for i in range(self.table_widget2.rowCount()):
                data.append(self.table_widget2.item(i, j).text())

                # print(self.table_widget1.item(0,9).text())

                def valid_number(str):
                    i = 0
                    j = len(str) - 1

                    # Handling whitespaces
                    while i < len(str) and str[i] == ' ':
                        i += 1
                    while j >= 0 and str[j] == ' ':
                        j -= 1

                    if i > j:
                        return False

                    # if string is of length 1 and the only
                    # character is not a digit
                    if (i == j and not (str[i] >= '0' and
                                        str[i] <= '9')):
                        return False

                    # If the 1st char is not '+', '-', '.' or digit
                    if (str[i] != '.' and str[i] != '+' and
                            str[i] != '-' and not (str[i] >= '0' and
                                                   str[i] <= '9')):
                        return False

                    # To check if a '.' or 'e' is found in given
                    # string.We use this flag to make sure that
                    # either of them appear only once.
                    flagDotOrE = False

                    for i in range(j + 1):

                        # If any of the char does not belong to
                        # {digit, +, -,., e}
                        if (str[i] != 'e' and str[i] != '.' and
                                str[i] != '+' and str[i] != '-' and not
                                (str[i] >= '0' and str[i] <= '9')):
                            return False

                        if str[i] == '.':

                            # check if the char e has already
                            # occured before '.' If yes, return 0
                            if flagDotOrE:
                                return False
                            if i + 1 > len(str):
                                return False
                            if (not (str[i + 1] >= '0' and
                                     str[i + 1] <= '9')):
                                return False
                        elif str[i] == 'e':

                            # set flagDotOrE = 1 when e is encountered.
                            flagDotOrE = True

                            # if there is no digit before e
                            if (not (str[i - 1] >= '0' and
                                     str[i - 1] <= '9')):
                                return False

                            # if e is the last character
                            if i + 1 > len(str):
                                return False

                            # if e is not followed by
                            # '+', '-' or a digit
                            if (str[i + 1] != '+' and str[i + 1] != '-' and
                                    (str[i + 1] >= '0' and str[i] <= '9')):
                                return False

                    # If the string skips all the
                    # above cases, it must be a numeric string
                    return True

                if not valid_number(self.table_widget2.item(i, j).text()) or result == True:

                    # print("****")
                    # print("This is a string")
                    # print(self.table_widget1.item(i, j).text())
                    print("****")
                    # print(self.table_widget1.item(i,j).text())

                    msg = QMessageBox()
                    msg.setWindowTitle("Error")
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("Check Your Entry ")
                    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

                    x = msg.exec()
    def get_column_data3(self):
        data = []
        data1 = []
        for k in range(self.table_widget3.rowCount()):
            data1.append(self.table_widget3.item(k, 0).text())

        print(data1)

        def checkIfDuplicates_1(data1):
            if len(data1) == len(set(data1)):
                return False
            else:
                return True

        result = checkIfDuplicates_1(data1)

        # print(self.table_widget1.item(0, 5).text())
        column = self.table_widget3.columnCount()
        for j in range(0, column):
            for i in range(self.table_widget3.rowCount()):
                data.append(self.table_widget3.item(i, j).text())

                # print(self.table_widget1.item(0,9).text())

                def valid_number(str):
                    i = 0
                    j = len(str) - 1

                    # Handling whitespaces
                    while i < len(str) and str[i] == ' ':
                        i += 1
                    while j >= 0 and str[j] == ' ':
                        j -= 1

                    if i > j:
                        return False

                    # if string is of length 1 and the only
                    # character is not a digit
                    if (i == j and not (str[i] >= '0' and
                                        str[i] <= '9')):
                        return False

                    # If the 1st char is not '+', '-', '.' or digit
                    if (str[i] != '.' and str[i] != '+' and
                            str[i] != '-' and not (str[i] >= '0' and
                                                   str[i] <= '9')):
                        return False

                    # To check if a '.' or 'e' is found in given
                    # string.We use this flag to make sure that
                    # either of them appear only once.
                    flagDotOrE = False

                    for i in range(j + 1):

                        # If any of the char does not belong to
                        # {digit, +, -,., e}
                        if (str[i] != 'e' and str[i] != '.' and
                                str[i] != '+' and str[i] != '-' and not
                                (str[i] >= '0' and str[i] <= '9')):
                            return False

                        if str[i] == '.':

                            # check if the char e has already
                            # occured before '.' If yes, return 0
                            if flagDotOrE:
                                return False
                            if i + 1 > len(str):
                                return False
                            if (not (str[i + 1] >= '0' and
                                     str[i + 1] <= '9')):
                                return False
                        elif str[i] == 'e':

                            # set flagDotOrE = 1 when e is encountered.
                            flagDotOrE = True

                            # if there is no digit before e
                            if (not (str[i - 1] >= '0' and
                                     str[i - 1] <= '9')):
                                return False

                            # if e is the last character
                            if i + 1 > len(str):
                                return False

                            # if e is not followed by
                            # '+', '-' or a digit
                            if (str[i + 1] != '+' and str[i + 1] != '-' and
                                    (str[i + 1] >= '0' and str[i] <= '9')):
                                return False

                    # If the string skips all the
                    # above cases, it must be a numeric string
                    return True

                if not valid_number(self.table_widget3.item(i, j).text()) or result == True:

                    print("****")
                    print("This is a string")
                    # print(self.table_widget1.item(i, j).text())
                    print("****")
                    # print(self.table_widget1.item(i,j).text())

                    msg = QMessageBox()
                    msg.setWindowTitle("Error")
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("Check Your Entry ")
                    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

                    x = msg.exec()
    def get_column_data4(self):
        data = []
        data1 = []
        for k in range(self.table_widget4.rowCount()):
            data1.append(self.table_widget4.item(k, 0).text())

        print(data1)

        def checkIfDuplicates_1(data1):
            if len(data1) == len(set(data1)):
                return False
            else:
                return True

        result = checkIfDuplicates_1(data1)

        # print(self.table_widget1.item(0, 5).text())
        column = self.table_widget4.columnCount()
        for j in range(0, column):
            for i in range(self.table_widget4.rowCount()):
                data.append(self.table_widget4.item(i, j).text())

                # print(self.table_widget1.item(0,9).text())

                def valid_number(str):
                    i = 0
                    j = len(str) - 1

                    # Handling whitespaces
                    while i < len(str) and str[i] == ' ':
                        i += 1
                    while j >= 0 and str[j] == ' ':
                        j -= 1

                    if i > j:
                        return False

                    # if string is of length 1 and the only
                    # character is not a digit
                    if (i == j and not (str[i] >= '0' and
                                        str[i] <= '9')):
                        return False

                    # If the 1st char is not '+', '-', '.' or digit
                    if (str[i] != '.' and str[i] != '+' and
                            str[i] != '-' and not (str[i] >= '0' and
                                                   str[i] <= '9')):
                        return False

                    # To check if a '.' or 'e' is found in given
                    # string.We use this flag to make sure that
                    # either of them appear only once.
                    flagDotOrE = False

                    for i in range(j + 1):

                        # If any of the char does not belong to
                        # {digit, +, -,., e}
                        if (str[i] != 'e' and str[i] != '.' and
                                str[i] != '+' and str[i] != '-' and not
                                (str[i] >= '0' and str[i] <= '9')):
                            return False

                        if str[i] == '.':

                            # check if the char e has already
                            # occured before '.' If yes, return 0
                            if flagDotOrE:
                                return False
                            if i + 1 > len(str):
                                return False
                            if (not (str[i + 1] >= '0' and
                                     str[i + 1] <= '9')):
                                return False
                        elif str[i] == 'e':

                            # set flagDotOrE = 1 when e is encountered.
                            flagDotOrE = True

                            # if there is no digit before e
                            if (not (str[i - 1] >= '0' and
                                     str[i - 1] <= '9')):
                                return False

                            # if e is the last character
                            if i + 1 > len(str):
                                return False

                            # if e is not followed by
                            # '+', '-' or a digit
                            if (str[i + 1] != '+' and str[i + 1] != '-' and
                                    (str[i + 1] >= '0' and str[i] <= '9')):
                                return False

                    # If the string skips all the
                    # above cases, it must be a numeric string
                    return True

                if not valid_number(self.table_widget4.item(i, j).text()) or result == True:

                    print("****")
                    print("This is a string")
                    # print(self.table_widget1.item(i, j).text())
                    print("****")
                    # print(self.table_widget1.item(i,j).text())

                    msg = QMessageBox()
                    msg.setWindowTitle("Error")
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("Check Your Entry ")
                    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

                    x = msg.exec()
    def save_text1(self):
        test_keys = ["ID", "Connection Type", "Axial load", "Shear load", "Bolt diameter", "Bolt grade", "Plate thickness"]
        l1 = []
        column = self.table_widget1.columnCount()
        for i in range(self.table_widget1.rowCount()):
            for j in range(0, column):
                text1 = self.table_widget1.item(i, j).text()
                l1.append(text1)
            res = {}
            for key in test_keys:
                for value in l1:
                    res[key] = value
                    l1.remove(value)
                    break
            l1 = []
        # print(res)
            finalString = json.dumps(res)

            file1 = open("Fin_"+str(i)+".txt", "a")
            file1.write(finalString)
            file1.close

    def save_text2(self):
        test_keys2 = ['ID', 'Member Length', 'Tensile Load', 'Support Condition at End 1', 'Support Condition at End 2']
        l2 = []
        column = self.table_widget2.columnCount()
        for i in range(self.table_widget2.rowCount()):
            for j in range(0, column):
                text2 = self.table_widget2.item(i, j).text()
                l2.append(text2)
            res = {}
            for key in test_keys2:
                for value in l2:
                    res[key] = value
                    l2.remove(value)
                    break
            l2 = []
        # print(res)
            finalString = json.dumps(res)

            file2 = open("TensionMember_"+str(i)+".txt", "a")
            file2.write(finalString)
            file2.close

    def save_text3(self):
        test_keys =['ID', 'Connection Type', 'Shear Load', 'Axial Load', 'Moment Load', 'Bolt Diameter', 'Bolt Grade',
             'Plate thickness']
        l1 = []
        column = self.table_widget3.columnCount()
        for i in range(self.table_widget3.rowCount()):
            for j in range(0, column):
                text1 = self.table_widget3.item(i, j).text()
                l1.append(text1)
            res = {}
            for key in test_keys:
                for value in l1:
                    res[key] = value
                    l1.remove(value)
                    break
            l1 = []
            # print(res)
            finalString = json.dumps(res)

            file3 = open("BCEndPlate_" + str(i) + ".txt", "a")
            file3.write(finalString)
            file3.close
    def save_text4(self):
        test_keys = ['ID', 'Angle Leg 1', 'Angle Leg 2', 'Angle Thickness' 'Shear Load', 'Bolt Diameter', 'Bolt Grade']
        l1 = []
        column = self.table_widget4.columnCount()
        for i in range(self.table_widget4.rowCount()):
            for j in range(0, column):
                text1 = self.table_widget4.item(i, j).text()
                l1.append(text1)
            res = {}
            for key in test_keys:
                for value in l1:
                    res[key] = value
                    l1.remove(value)
                    break
            l1 = []
        # print(res)
            finalString = json.dumps(res)

            file4 = open("CleatAngle_"+str(i)+".txt", "a")
            file4.write(finalString)
            file4.close
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
