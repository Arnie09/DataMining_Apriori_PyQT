from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import tkinter
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from Apriori_core_demo import apriori

import random


class Demo_MainWindow(object):
    def __init__(self):
        self.data = []
        self.labels = []


    def methodGenerateList(self):
        #setting up apriori details
        self.transactions = {}
        self.transactions[1] = self.Transaction_1.text().split(",")
        self.transactions[2] = self.Transaction_2.text().split(",")
        self.transactions[3] = self.Transaction_3.text().split(",")
        self.transactions[4] = self.Transaction_4.text().split(",")
        self.min = 1
        self.dispString = ""
        self.dispString2 = ""
        self.a=1
        self.b=0
        self.itemlist = ['a','b','c','d']

        self.AprioriInstance = apriori(min = self.min , transactions = self.transactions , productlist = self.itemlist)
        self.AprioriInstance.finalRules[1]="No rules to display for the first list!"
        if(self.a == 1):
            self.showList(self.AprioriInstance.allLs[self.a])
        print(self.a)
        print("Hello")

        if(self.a == 1):
            self.generateRules.setEnabled(False)
        else:
            self.generateRules.setEnabled(True)

    def showRules(self,dict):
        self.data = []
        print(self.a,self.b)

        self.RulesOutput.clear()
        for elements in dict:
            self.dispString = str(elements)
            self.RulesOutput.append(self.dispString)

    def showList(self,dict):
        self.data = []
        self.labels = []
        if(self.a <= len(self.AprioriInstance.allLs)-1):
            self.a+=1
            self.b+=1

        # if(self.b == 6):
        #     self.b+=1

        self.ListOutput.clear()
        for elements in dict:
            self.dispString2 = str(elements)+" : "+str(dict[elements])
            self.data.append(dict[elements])
            self.labels.append(elements)
            self.ListOutput.append(self.dispString2)
        self.plot()

    def plot(self):
        ''' plot the data '''
        # random data
        #data = [random.random() for i in range(10)]
        print(self.data)
        print(self.labels)
        x = []
        # instead of ax.hold(False)
        self.figure.clear()
        for i in range(len(self.labels)):
            x.append(i)
        # create an axis
        ax = self.figure.add_subplot(111,position=[0.10, 0.10, 0.8, 0.7])

        # discards the old graph
        # ax.hold(False) # deprecated, see above
        ax.set_xticks(x)
        ax.set_xticklabels(self.labels)

        # plot data
        ax.plot(self.data, '*-')

        # refresh canvas
        self.canvas.draw()

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.532, y1:0, x2:0.538, y2:1, stop:0 rgba(119, 119, 119, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #FOR FIXING UP THE GRAPH IN MainWindow
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 600, 600))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget")

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(650, 30, 301, 301))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")


        #code for the matplotlib part(bsically stuff copied from stack overflow :) )
         # a figure instance to plot on
        self.figure = Figure(figsize=(1, 1),dpi=100)

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)


        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self.MainWindow)

        # Just some button connected to `plot` method



        # set the layout

        self.layout = QtWidgets.QVBoxLayout(self.gridLayoutWidget_3)
        self.layout.setGeometry(QtCore.QRect(10,10,100,100))
        self.layout.addWidget(self.toolbar,1)
        self.layout.addWidget(self.canvas,1)

        #self.FigureCanvas.setGeometry(QtCore.QRect(20, 20, 431,511))


        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)




        self.Transaction_1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Transaction_1.setObjectName("Transaction_1")
        self.Transaction_1.setText("a,b,c,d")
        self.Transaction_1.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.Transaction_1, 0, 1, 1, 1)

        self.Transaction_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Transaction_2.setObjectName("Transaction_2")
        self.Transaction_2.setText("a,b,c")
        self.Transaction_2.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.Transaction_2, 2, 1, 1, 1)

        self.Transaction_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Transaction_3.setObjectName("Transaction_3")
        self.Transaction_3.setText("b,c")
        self.Transaction_3.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.Transaction_3, 3, 1, 1, 1)

        self.Transaction_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Transaction_4.setObjectName("Transaction_4")
        self.Transaction_4.setText("d,b")
        self.Transaction_4.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.Transaction_4, 4, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(650, 350, 301, 221))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 1, 1, 1)

        self.ListOutput = QtWidgets.QTextBrowser(self.gridLayoutWidget_2)
        self.ListOutput.setObjectName("ListOutput")
        self.ListOutput.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.ListOutput, 1, 0, 1, 1)

        self.RulesOutput = QtWidgets.QTextBrowser(self.gridLayoutWidget_2)
        self.RulesOutput.setObjectName("RulesOutput")
        self.RulesOutput.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.RulesOutput, 1, 1, 1, 1)

        self.generateList = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.generateList.setObjectName("generateList")

        self.gridLayout_2.addWidget(self.generateList, 2, 0, 1, 1)

        self.generateRules = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.generateRules.setObjectName("generateRules")

        self.AprioriButton = QtWidgets.QPushButton(self.centralwidget)
        self.AprioriButton.setGeometry(QtCore.QRect(650, 310, 301, 28))
        self.AprioriButton.setObjectName("AprioriButton")
        self.AprioriButton.clicked.connect(self.methodGenerateList)
        self.AprioriButton.setStyleSheet("background: rbg(0,0,0); color: rgb(255,255,255)")

        self.generateList.clicked.connect(lambda:self.showList(self.AprioriInstance.allLs[self.a]))
        self.generateRules.clicked.connect(lambda:self.showRules(self.AprioriInstance.finalRules[self.b]))

        self.gridLayout_2.addWidget(self.generateRules, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Demo"))
        self.label_2.setText(_translate("MainWindow", "Transaction 1 :"))
        self.label_3.setText(_translate("MainWindow", "Transaction 3 :"))
        self.label_4.setText(_translate("MainWindow", "Transaction 4 :"))
        self.label.setText(_translate("MainWindow", "Transaction 2 :"))
        self.label_5.setText(_translate("MainWindow", "List :"))
        self.label_6.setText(_translate("MainWindow", "Corresponding rules :"))
        self.generateList.setText(_translate("MainWindow", "Show list"))
        self.generateRules.setText(_translate("MainWindow", "Show Rules"))
        self.AprioriButton.setText(_translate("MainWindow", "Run Apriori"))
