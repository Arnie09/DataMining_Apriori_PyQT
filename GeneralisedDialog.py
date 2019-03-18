from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
from Apriori_core import apriori
from FP_Growth_Core import FP_Tree

class GeneralisedWindow(object):

    columnheader=[]

    def toQuit(self):
        self.MainWindow.close()

    def OpenFile(self):
        self.name = QtWidgets.QFileDialog.getOpenFileName(self.MainWindow, "Select File", "", "*.xlsx *.csv")
        self.path=self.name[0]
        self.extension = self.path[self.path.index("."):]
        if(self.extension == '.xlsx'):
            self.localdb=pd.read_excel(self.path)
        else:
            self.localdb = pd.read_csv(self.path)
        self.columnheader=list(self.localdb.columns.values)
        print(self.columnheader)
        self.ProductNameHeader.addItems(self.columnheader)
        self.InvoiceHeader.addItems(self.columnheader)

        self.ShowPath.setText(self.path)
        print(self.path)

    def run(self):
        print(self.AlgorithmPicker.currentText())
        if(self.AlgorithmPicker.currentText() == "Apriori Algorithm"):
            '''do apriori work'''
            self.AprioriInstance = apriori(address=self.path,min=int(self.Min.text()),invNo=self.InvoiceHeader.currentText(),productCode=self.ProductNameHeader.currentText())
            self.a=1
            self.b=0
            self.AprioriInstance.finalRules[1]="No rules to display for the first list!"
            self.showListApriori(self.AprioriInstance.allLs[self.a])
            print(self.a)


            if(self.a == 1):
                self.rulesGenerator.setEnabled(False)
            else:
                self.rulesGenerator.setEnabled(True)
                self.nextListBtn.setEnabled(True)

        elif(self.AlgorithmPicker.currentText() == "FP Growth Algorithm"):
            '''do fp growth work'''
            self.fpInstance = FP_Tree(address=self.path,min=int(self.Min.text()),invNo=self.InvoiceHeader.currentText(),productCode=self.ProductNameHeader.currentText())
            self.fpInstance.display()
            self.fpInstance.displayRules()
            self.showListFP(self.fpInstance.finalList)
            self.showRulesFP(self.fpInstance.finalRules)

    '''function to showList of apriori'''
    def showListApriori(self,dict):

        if(self.a <= len(self.AprioriInstance.allLs)-1):
            self.a+=1
            self.b+=1
        self.outputList.clear()
        for elements in dict:
            dispString = str(elements)+" : "+str(dict[elements])
            self.outputList.append(dispString)

    '''function to show rules of apriori'''
    def showRulesApriori(self,dict):

        print(self.a,self.b)
        self.outputRules.clear()
        for elements in dict:
            dispString = str(elements)
            self.outputRules.append(dispString)

    '''function to show list of fpgrowth'''
    def showListFP(self,listsFP):
        self.outputList.clear()
        for elements in listsFP:
            individual_list = str(elements)
            self.outputList.append(individual_list)

    '''function to show rules of FP'''
    def showRulesFP(self,rules):
        self.outputRules.clear()
        for i in rules:
            individual_rule = str(i[0]+'=>'+i[1]+":"+str(round(i[2]))+"%")
            self.outputRules.append(individual_rule)

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1097, 885)
        MainWindow.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.532, y1:0, x2:0.538, y2:1, stop:0 rgba(119, 119, 119, 255), stop:1 rgba(255, 255, 255, 255))\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 1, 1, 1)
        self.InvoiceHeader = QtWidgets.QComboBox(self.centralwidget)
        self.InvoiceHeader.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.InvoiceHeader.setObjectName("InvoiceHeader")
        self.gridLayout.addWidget(self.InvoiceHeader, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 10, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 10, 1, 1, 1)
        self.Min = QtWidgets.QLineEdit(self.centralwidget)
        self.Min.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Min.setObjectName("Min")
        self.gridLayout.addWidget(self.Min, 7, 1, 1, 1)
        self.outputRules = QtWidgets.QTextBrowser(self.centralwidget)
        self.outputRules.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.outputRules.setObjectName("outputRules")
        self.gridLayout.addWidget(self.outputRules, 11, 2, 1, 1)

        self.Run = QtWidgets.QPushButton(self.centralwidget)
        self.Run.setStyleSheet("background-color: rgb(80, 80, 80);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.Run.setObjectName("Run")
        self.Run.clicked.connect(self.run)#running the algorithm

        self.gridLayout.addWidget(self.Run, 7, 2, 1, 1)
        self.nextListBtn = QtWidgets.QPushButton(self.centralwidget)
        self.nextListBtn.setStyleSheet("background-color: rgb(80, 80, 80);\n"
"color: rgb(255,255,255);")
        self.nextListBtn.setObjectName("nextListBtn")
        self.gridLayout.addWidget(self.nextListBtn, 12, 1, 1, 1)
        self.rulesGenerator = QtWidgets.QPushButton(self.centralwidget)
        self.rulesGenerator.setMaximumSize(QtCore.QSize(527, 16777215))
        self.rulesGenerator.setStyleSheet("background-color: rgb(80, 80, 80);\n"
"color: rgb(255,255,255);")
        self.rulesGenerator.setObjectName("rulesGenerator")
        self.gridLayout.addWidget(self.rulesGenerator, 12, 2, 1, 1)
        self.ShowPath = QtWidgets.QLineEdit(self.centralwidget)
        self.ShowPath.setObjectName("ShowPath")
        self.gridLayout.addWidget(self.ShowPath, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("font: 75 9pt \"Yu Gothic UI Semibold\";\n"
"selection-color: rgb(85, 0, 255);")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.outputList = QtWidgets.QTextBrowser(self.centralwidget)
        self.outputList.setStyleSheet("background-color: rgb(200, 200, 200);\n"
"")
        self.outputList.setObjectName("outputList")
        self.gridLayout.addWidget(self.outputList, 11, 1, 1, 1)
        self.ProductNameHeader = QtWidgets.QComboBox(self.centralwidget)
        self.ProductNameHeader.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ProductNameHeader.setObjectName("ProductNameHeader")
        self.gridLayout.addWidget(self.ProductNameHeader, 5, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 9, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 9, 1, 1, 1)

        self.nextListBtn.setEnabled(False)
        self.rulesGenerator.setEnabled(False)
        '''connecting the buttons'''
        self.nextListBtn.clicked.connect(lambda:self.showListApriori(self.AprioriInstance.allLs[self.a]))
        self.rulesGenerator.clicked.connect(lambda:self.showRulesApriori(self.AprioriInstance.finalRules[self.b]))

        '''listing the algorithms in the drop down menu '''
        self.AlgorithmPicker = QtWidgets.QComboBox(self.centralwidget)
        self.AlgorithmPicker.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.AlgorithmPicker.setObjectName("AlgorithmPicker")
        self.gridLayout.addWidget(self.AlgorithmPicker, 3, 2, 1, 1)
        self.AlgorithmPicker.addItem("Apriori Algorithm")
        self.AlgorithmPicker.addItem("FP Growth Algorithm")
        '''add more algorithms in the way above'''

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        '''menubar part'''
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1097, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(self.toQuit)

        self.actionTo_open_an_xlsx_file = QtWidgets.QAction(MainWindow)
        self.actionTo_open_an_xlsx_file.setObjectName("actionTo_open_an_xlsx_file")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.triggered.connect(self.OpenFile)

        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Apriori"))
        self.label_5.setText(_translate("MainWindow", "Minimum confidence:"))
        self.label_3.setText(_translate("MainWindow", "Transaction Number"))
        self.label_7.setText(_translate("MainWindow", "Rules :"))
        self.label_6.setText(_translate("MainWindow", "Lists :"))
        self.Run.setText(_translate("MainWindow", "Run"))
        self.nextListBtn.setText(_translate("MainWindow", "Next List"))
        self.rulesGenerator.setText(_translate("MainWindow", "Corresponding Rules"))
        self.label_2.setText(_translate("MainWindow", "You have Entered :"))
        self.label_4.setText(_translate("MainWindow", "Transaction Description"))
        self.label.setText(_translate("MainWindow", "Algorithm To Use :"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionTo_open_an_xlsx_file.setText(_translate("MainWindow", "to open an xlsx file"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GeneralisedWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
