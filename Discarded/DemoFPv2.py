from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from FPTreeDisplay import FP_Tree
import os
import sys
from time import sleep

class Ui_FPDemo(object):

    def callFP(self):
        self.transactions = {}
        self.transactions[1] = self.Transaction_1.text().split(",")
        self.transactions[2] = self.Transaction_2.text().split(",")
        self.transactions[3] = self.Transaction_3.text().split(",")
        self.transactions[4] = self.Transaction_4.text().split(",")
        print(self.transactions)
        self.mini = int(self.label_10.text())
        print(self.mini)
        self.FPobject = FP_Tree(min = self.mini,transactions = self.transactions)
        sleep(1)
        self.showPictures()

    def showPictures(self):
        print('yo yo')
        pixmap1 = QtGui.QPixmap(os.getcwd()+'\images\graph1.png')
        self.label_5.setPixmap(pixmap1)
        pixmap2 = QtGui.QPixmap(os.getcwd()+'\images\graph2.png')
        self.label_6.setPixmap(pixmap2)
        pixmap3 = QtGui.QPixmap(os.getcwd()+'\images\graph3.png')
        self.label_7.setPixmap(pixmap3)
        pixmap4 = QtGui.QPixmap(os.getcwd()+'\images\graph4.png')
        self.label_8.setPixmap(pixmap4)

        self.label_5.resize(pixmap1.width(),pixmap1.height())
        self.label_6.resize(pixmap2.width(),pixmap2.height())
        self.label_7.resize(pixmap3.width(),pixmap3.height())
        self.label_8.resize(pixmap4.width(),pixmap4.height())

        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()

    def setupUi(self, FPDemo):
        FPDemo.setObjectName("FPDemo")
        FPDemo.resize(1100, 1000)
        FPDemo.setStyleSheet("background-image: url(:/newPrefix/bcnd_fp.jpg);")
        self.centralwidget = QtWidgets.QWidget(FPDemo)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(11, 11, 233, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Transaction_1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Transaction_1.setObjectName("Transaction_1")
        self.gridLayout.addWidget(self.Transaction_1, 0, 1, 1, 1)
        self.Transaction_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Transaction_4.setObjectName("Transaction_4")
        self.gridLayout.addWidget(self.Transaction_4, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.Transaction_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Transaction_3.setObjectName("Transaction_3")
        self.gridLayout.addWidget(self.Transaction_3, 3, 1, 1, 1)
        self.Transaction_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Transaction_2.setObjectName("Transaction_2")
        self.gridLayout.addWidget(self.Transaction_2, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.FPButton = QtWidgets.QPushButton(self.centralwidget)
        self.FPButton.setGeometry(QtCore.QRect(10, 190, 93, 28))
        self.FPButton.setObjectName("FPButton")
        self.FPButton.clicked.connect(self.callFP)
        #self.FPButton.clicked.connect(self.showPictures)

        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(10, 160, 160, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 140, 55, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(190, 160, 55, 16))
        self.label_10.setObjectName("label_10")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(10, 160, 160, 22))

        '''setting max and min od slider'''
        self.horizontalSlider_2.setMinimum(1)
        self.horizontalSlider_2.setMaximum(4)

        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(360, 30, 280, 320))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(750, 20, 280, 320))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(360, 500, 280, 320))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(750, 500, 280, 320))
        self.label_8.setObjectName("label_8")
        FPDemo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FPDemo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1059, 26))
        self.menubar.setObjectName("menubar")
        FPDemo.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FPDemo)
        self.statusbar.setObjectName("statusbar")
        FPDemo.setStatusBar(self.statusbar)

        self.retranslateUi(FPDemo)
        self.horizontalSlider_2.valueChanged['int'].connect(self.label_10.setNum)
        QtCore.QMetaObject.connectSlotsByName(FPDemo)

    def retranslateUi(self, FPDemo):
        _translate = QtCore.QCoreApplication.translate
        FPDemo.setWindowTitle(_translate("FPDemo", "FPDemo"))
        self.Transaction_1.setText(_translate("FPDemo", "a,b,c,d"))
        self.Transaction_4.setText(_translate("FPDemo", "c,d"))
        self.label_3.setText(_translate("FPDemo", "Transaction 3 :"))
        self.label_2.setText(_translate("FPDemo", "Transaction 1 :"))
        self.label.setText(_translate("FPDemo", "Transaction 2 :"))
        self.Transaction_3.setText(_translate("FPDemo", "a,d"))
        self.Transaction_2.setText(_translate("FPDemo", "a,b,c"))
        self.label_4.setText(_translate("FPDemo", "Transaction 4 :"))
        self.FPButton.setText(_translate("FPDemo", "Run FP"))
        self.label_9.setText(_translate("FPDemo", "Min :"))
        self.label_10.setText(_translate("FPDemo", "1"))