from GeneralisedDialogRevamped import GeneralisedWindow
from Demo import Demo_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from DemoFPv2 import Ui_FPDemo

class Ui_MainWindow(object):

    def RunAlgorithms(self):
        self.runAlgo = QtWidgets.QMainWindow()
        self.runAlgoUI = GeneralisedWindow()
        self.runAlgoUI.setupUi(self.runAlgo)
        self.runAlgo.show()


    def fp_demo(self):
        self.FPDemo = QtWidgets.QMainWindow()
        self.FPDemoUI = Ui_FPDemo()
        self.FPDemoUI.setupUi(self.FPDemo)
        self.FPDemo.show()

    def toQuit(self):
        sys.exit()

    def callDemo(self):
        print("hI")
        self.Demo = QtWidgets.QMainWindow()
        self.DemoUI = Demo_MainWindow()
        self.DemoUI.setupUi(self.Demo)
        self.Demo.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(625, 701)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.532, y1:0, x2:0.538, y2:1, stop:0 rgba(119, 119, 119, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        '''clicking this button will call the Information on apriori function'''
        self.InfoPushbutton = QtWidgets.QPushButton(self.centralwidget)
        self.InfoPushbutton.setObjectName("InfoPushbutton")
        self.verticalLayout.addWidget(self.InfoPushbutton)
        self.InfoPushbutton.clicked.connect(self.callDemo)

        '''Info on FP Growth'''
        self.InfoFPButton = QtWidgets.QPushButton(self.centralwidget)
        self.InfoFPButton.setObjectName("InfoFPButton")
        self.verticalLayout.addWidget(self.InfoFPButton)
        self.InfoFPButton.clicked.connect(self.fp_demo)

        '''clicking this button will call generalised dialog box'''
        self.TryOutPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.TryOutPushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.TryOutPushButton)
        self.TryOutPushButton.clicked.connect(self.RunAlgorithms)

        '''to Quit the application'''
        self.QuitButton = QtWidgets.QPushButton(self.centralwidget)
        self.QuitButton.setObjectName("QuitButton")
        self.verticalLayout.addWidget(self.QuitButton)
        self.QuitButton.clicked.connect(self.toQuit)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 625, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DataMining"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600;\">DATA MINING</span></p></body></html>"))
        self.InfoPushbutton.setText(_translate("MainWindow", "Apriori - Info"))
        self.InfoFPButton.setText(_translate("MainWindow", "FP-Growth Info"))
        self.TryOutPushButton.setText(_translate("MainWindow", "Try Out our Algorithms"))
        self.QuitButton.setText(_translate("MainWindow", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
