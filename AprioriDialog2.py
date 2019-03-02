# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AprioriDialog2.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
import pandas as pd
from Apriori_core import apriori
from PyQt5 import QtCore, QtGui, QtWidgets

class Apriori_Window(object):

    columnheader=[]

    def toQuit(self):
        self.MainWindow.close()

    def OpenFile(self):
        self.name = QtWidgets.QFileDialog.getOpenFileName()
        self.path=self.name[0]
        self.localdb=pd.read_excel(self.path)
        self.columnheader=list(self.localdb.columns.values)
        print(self.columnheader)
        self.ProductNameHeader.addItems(self.columnheader)
        self.InvoiceHeader.addItems(self.columnheader)

        self.ShowPath.setText(self.path)
        print(self.path)

    def run_apriori(self):
        self.AprioriInstance = apriori(address=self.path,min=int(self.Min.text()),invNo=self.InvoiceHeader.currentText(),productCode=self.ProductNameHeader.currentText())
        self.a=1
        self.b=0
        self.AprioriInstance.finalRules[1]="No rules to display for the first list!"
        self.showList(self.AprioriInstance.allLs[self.a])
        print(self.a)


        if(self.a == 1):
            self.rulesGenerator.setEnabled(False)
        else:
            self.rulesGenerator.setEnabled(True)

    def showRules(self,dict):

        print(self.a,self.b)

        self.outputRules.clear()
        for elements in dict:
            dispString = str(elements)
            self.outputRules.append(dispString)

    def showList(self,dict):

        if(self.a <= len(self.AprioriInstance.allLs)-1):
            self.a+=1
            self.b+=1

        # if(self.b == 6):
        #     self.b+=1

        self.outputList.clear()
        for elements in dict:
            dispString = str(elements)+" : "+str(dict[elements])
            self.outputList.append(dispString)

    def setupUi(self, MainWindow):
        self.MainWindow=MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1095, 892)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(63, 190, 220, 255), stop:1 rgba(255, 255, 255, 255))\n"
"")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.rulesGenerator = QtWidgets.QPushButton(self.centralwidget)
        self.rulesGenerator.setMaximumSize(QtCore.QSize(527, 16777215))
        self.rulesGenerator.setObjectName("rulesGenerator")
        self.rulesGenerator.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.gridLayout.addWidget(self.rulesGenerator, 12, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 9, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 10, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 9, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 10, 2, 1, 1)

        self.Run = QtWidgets.QPushButton(self.centralwidget)
        self.Run.setObjectName("Run")
        self.gridLayout.addWidget(self.Run, 7, 3, 1, 1)
        self.Run.clicked.connect(self.run_apriori)
        self.Run.setStyleSheet("background-color: rgb(38, 23, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(170, 255, 255);")

        self.Min = QtWidgets.QLineEdit(self.centralwidget)
        self.Min.setObjectName("Min")
        self.Min.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gridLayout.addWidget(self.Min, 7, 2, 1, 1)


        self.outputRules = QtWidgets.QTextBrowser(self.centralwidget)
        self.outputRules.setObjectName("outputRules")
        self.outputRules.setStyleSheet("background-color: rgb(0, 255, 255);")

        self.gridLayout.addWidget(self.outputRules, 11, 3, 1, 1)
        self.outputList = QtWidgets.QTextBrowser(self.centralwidget)
        self.outputList.setObjectName("outputList")
        self.outputList.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"")
        self.gridLayout.addWidget(self.outputList, 11, 2, 1, 1)
        self.nextListBtn = QtWidgets.QPushButton(self.centralwidget)
        self.nextListBtn.setObjectName("nextListBtn")
        self.nextListBtn.setStyleSheet("background-color: rgb(0, 170, 255);")

        self.gridLayout.addWidget(self.nextListBtn, 12, 2, 1, 1)
        self.ProductNameHeader = QtWidgets.QComboBox(self.centralwidget)
        self.ProductNameHeader.setObjectName("ProductNameHeader")
        self.ProductNameHeader.addItem('')
        self.ProductNameHeader.setStyleSheet("background-color: rgb(255, 255, 255);")


        self.gridLayout.addWidget(self.ProductNameHeader, 5, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("font: 75 9pt \"Yu Gothic UI Semibold\";\n"
"selection-color: rgb(85, 0, 255);")
        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)
        self.InvoiceHeader = QtWidgets.QComboBox(self.centralwidget)
        self.InvoiceHeader.setObjectName("InvoiceHeader")
        self.InvoiceHeader.addItem('')
        self.InvoiceHeader.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.nextListBtn.clicked.connect(lambda:self.showList(self.AprioriInstance.allLs[self.a]))
        self.rulesGenerator.clicked.connect(lambda:self.showRules(self.AprioriInstance.finalRules[self.b]))


        self.gridLayout.addWidget(self.InvoiceHeader, 3, 2, 1, 1)

        self.ShowPath = QtWidgets.QLabel(self.centralwidget)
        self.ShowPath.setObjectName("ShowPath")


        self.gridLayout.addWidget(self.ShowPath, 1, 3, 1, 1)
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
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.triggered.connect(self.OpenFile)

        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(self.toQuit)


        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Apriori"))
        self.rulesGenerator.setText(_translate("MainWindow", "Corresponding Rules"))
        self.label_5.setText(_translate("MainWindow", "Minimum confidence:"))
        self.label_7.setText(_translate("MainWindow", "Rules :"))
        self.label_4.setText(_translate("MainWindow", "ProductName"))
        self.label_3.setText(_translate("MainWindow", "Invoice Number"))
        self.label_6.setText(_translate("MainWindow", "Lists :"))
        self.Run.setText(_translate("MainWindow", "Run"))
        self.nextListBtn.setText(_translate("MainWindow", "Next List"))
        self.label_2.setText(_translate("MainWindow", "You have Entered :"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
