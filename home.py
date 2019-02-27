from AprioriDialog2 import Apriori_Window
from Demo import Demo_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def callApriori(self):
        self.Apriori = QtWidgets.QMainWindow()
        self.ui = Apriori_Window()
        self.ui.setupUi(self.Apriori)
        self.Apriori.show()

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
        MainWindow.resize(657, 703)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background:\n"
"rgb(255, 253, 172)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_Data_Mining = QtWidgets.QLabel(self.frame)
        self.label_Data_Mining.setGeometry(QtCore.QRect(190, 220, 241, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_Data_Mining.setFont(font)
        self.label_Data_Mining.setObjectName("label_Data_Mining")
        self.verticalLayout.addWidget(self.frame)
        self.InfoPushbutton = QtWidgets.QPushButton(self.centralwidget)
        self.InfoPushbutton.setObjectName("InfoPushbutton")
        self.verticalLayout.addWidget(self.InfoPushbutton)
        self.InfoPushbutton.clicked.connect(self.callDemo)

        self.TryOutPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.TryOutPushButton.setObjectName("TryOutPushButton")
        self.verticalLayout.addWidget(self.TryOutPushButton)
        self.TryOutPushButton.clicked.connect(self.callApriori)

        self.InfoFPButton = QtWidgets.QPushButton(self.centralwidget)
        self.InfoFPButton.setObjectName("InfoFPButton")
        self.verticalLayout.addWidget(self.InfoFPButton)
        self.TryOutFPGrowthButton = QtWidgets.QPushButton(self.centralwidget)
        self.TryOutFPGrowthButton.setObjectName("TryOutFPGrowthButton")
        self.verticalLayout.addWidget(self.TryOutFPGrowthButton)
        self.QuitButton = QtWidgets.QPushButton(self.centralwidget)
        self.QuitButton.setObjectName("QuitButton")
        self.verticalLayout.addWidget(self.QuitButton)
        self.QuitButton.clicked.connect(self.toQuit)
        
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 657, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AprioriHome"))
        self.label_Data_Mining.setText(_translate("MainWindow", "Data Mining!"))
        self.InfoPushbutton.setText(_translate("MainWindow", "Apriori - Info"))
        self.TryOutPushButton.setText(_translate("MainWindow", "Try out Apriori!"))
        self.InfoFPButton.setText(_translate("MainWindow", "FP-Growth Info"))
        self.TryOutFPGrowthButton.setText(_translate("MainWindow", "Try out FP Growth"))
        self.QuitButton.setText(_translate("MainWindow", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
