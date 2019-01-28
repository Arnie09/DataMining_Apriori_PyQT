from AprioriDialog2 import Apriori_Window
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def callApriori(self):
        self.Apriori = QtWidgets.QMainWindow()
        self.ui = Apriori_Window()
        self.ui.setupUi(self.Apriori)
        self.Apriori.show()

    def toQuit(self):
        sys.exit()

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
        self.TryOutPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.TryOutPushButton.setObjectName("TryOutPushButton")
        self.TryOutPushButton.clicked.connect(self.callApriori)

        self.verticalLayout.addWidget(self.TryOutPushButton)
        self.QuitButton = QtWidgets.QPushButton(self.centralwidget)
        self.QuitButton.setObjectName("QuitButton")
        self.QuitButton.clicked.connect(self.toQuit)

        self.verticalLayout.addWidget(self.QuitButton)
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
        self.QuitButton.setText(_translate("MainWindow", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
