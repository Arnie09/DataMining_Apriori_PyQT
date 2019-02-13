from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

import random


class Demo_MainWindow(object):

    def plot(self):
        ''' plot some random stuff '''
        # random data
        data = [random.random() for i in range(10)]

        # instead of ax.hold(False)
        self.figure.clear()

        # create an axis
        ax = self.figure.add_subplot(111,position=[0.10, 0.10, 0.5, 0.5])

        # discards the old graph
        # ax.hold(False) # deprecated, see above

        # plot data
        ax.plot(data, '*-')

        # refresh canvas
        self.canvas.draw()

    def setupUi(self, MainWindow):
        print("Here")
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


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
        self.button = QtWidgets.QPushButton('Plot')
        self.button.clicked.connect(self.plot)


        # set the layout

        self.layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.layout.setGeometry(QtCore.QRect(10,10,400,400))
        self.layout.addWidget(self.toolbar,1)
        self.layout.addWidget(self.canvas,1)
        self.layout.addWidget(self.button,1)
        #self.FigureCanvas.setGeometry(QtCore.QRect(20, 20, 431,511))

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(650, 30, 301, 301))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
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

        self.gridLayout.addWidget(self.Transaction_1, 0, 1, 1, 1)

        self.Transaction_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Transaction_2.setObjectName("Transaction_2")

        self.gridLayout.addWidget(self.Transaction_2, 2, 1, 1, 1)

        self.Transaction_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Transaction_3.setObjectName("Transaction_3")

        self.gridLayout.addWidget(self.Transaction_3, 3, 1, 1, 1)

        self.Transaction_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Transaction_4.setObjectName("Transaction_4")

        self.gridLayout.addWidget(self.Transaction_4, 4, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(650, 310, 301, 221))
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

        self.gridLayout_2.addWidget(self.ListOutput, 1, 0, 1, 1)

        self.RulesOutput = QtWidgets.QTextBrowser(self.gridLayoutWidget_2)
        self.RulesOutput.setObjectName("RulesOutput")

        self.gridLayout_2.addWidget(self.RulesOutput, 1, 1, 1, 1)

        self.generateList = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.generateList.setObjectName("generateList")

        self.gridLayout_2.addWidget(self.generateList, 2, 0, 1, 1)

        self.generateRules = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.generateRules.setObjectName("generateRules")

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
