# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FPDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1095, 892)
        MainWindow.setStyleSheet("background:qradialgradient(spread:pad, cx:0.261343, cy:0.477, radius:0.884, fx:0.5, fy:0.5, stop:0 rgba(249, 255, 130, 255), stop:1 rgba(255, 255, 255, 255))\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 10, 2, 1, 1)
        self.outputList = QtWidgets.QTextBrowser(self.centralwidget)
        self.outputList.setStyleSheet("background-color: rgb(244, 255, 121);\n"
"\n"
"")
        self.outputList.setObjectName("outputList")
        self.gridLayout.addWidget(self.outputList, 11, 1, 1, 1)
        self.InvoiceHeader = QtWidgets.QComboBox(self.centralwidget)
        self.InvoiceHeader.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.InvoiceHeader.setObjectName("InvoiceHeader")
        self.gridLayout.addWidget(self.InvoiceHeader, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 9, 2, 1, 1)
        self.Min = QtWidgets.QLineEdit(self.centralwidget)
        self.Min.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Min.setObjectName("Min")
        self.gridLayout.addWidget(self.Min, 7, 1, 1, 1)
        self.ShowPath = QtWidgets.QLineEdit(self.centralwidget)
        self.ShowPath.setObjectName("ShowPath")
        self.gridLayout.addWidget(self.ShowPath, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("font: 75 9pt \"Yu Gothic UI Semibold\";\n"
"selection-color: rgb(85, 0, 255);")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 10, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 1, 1, 1)
        self.outputRules = QtWidgets.QTextBrowser(self.centralwidget)
        self.outputRules.setStyleSheet("background-color: rgb(244, 255, 121);")
        self.outputRules.setObjectName("outputRules")
        self.gridLayout.addWidget(self.outputRules, 11, 2, 1, 1)
        self.Run = QtWidgets.QPushButton(self.centralwidget)
        self.Run.setStyleSheet("\n"
"background-color: rgb(255, 85, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(170, 255, 255);")
        self.Run.setObjectName("Run")
        self.gridLayout.addWidget(self.Run, 7, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        self.ProductNameHeader = QtWidgets.QComboBox(self.centralwidget)
        self.ProductNameHeader.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ProductNameHeader.setObjectName("ProductNameHeader")
        self.gridLayout.addWidget(self.ProductNameHeader, 5, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 9, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1095, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOpen = QtWidgets.QMenu(self.menuFile)
        self.menuOpen.setObjectName("menuOpen")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionTo_open_an_xlsx_file = QtWidgets.QAction(MainWindow)
        self.actionTo_open_an_xlsx_file.setObjectName("actionTo_open_an_xlsx_file")
        self.menuFile.addAction(self.menuOpen.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FP Growth"))
        self.label_7.setText(_translate("MainWindow", "Rules :"))
        self.label_2.setText(_translate("MainWindow", "You have Entered :"))
        self.label_6.setText(_translate("MainWindow", "Lists :"))
        self.label_5.setText(_translate("MainWindow", "Minimum confidence:"))
        self.Run.setText(_translate("MainWindow", "Run"))
        self.label_3.setText(_translate("MainWindow", "Invoice Number"))
        self.label_4.setText(_translate("MainWindow", "ProductName"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOpen.setTitle(_translate("MainWindow", "Open"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionTo_open_an_xlsx_file.setText(_translate("MainWindow", "to open an xlsx file"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

