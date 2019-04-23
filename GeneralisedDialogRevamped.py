from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
from Apriori_core import apriori
from FP_Growth_Core import FP_Tree
from PyQt5 import QtCore, QtGui, QtWidgets

class GeneralisedWindow(object):

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

    def setupUi(self, MainWindow):
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
        self.Run = QtWidgets.QPushButton(self.centralwidget)
        self.Run.setStyleSheet("background-color: rgb(80, 80, 80);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.Run.setObjectName("Run")
        self.gridLayout.addWidget(self.Run, 9, 2, 1, 1)
        self.OutputRules = QtWidgets.QTextBrowser(self.centralwidget)
        self.OutputRules.setStyleSheet("background-color: rgb(200, 200, 200);\n"
"")
        self.OutputRules.setObjectName("OutputRules")
        self.gridLayout.addWidget(self.OutputRules, 15, 1, 3, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("font: 75 9pt \"Yu Gothic UI Semibold\";\n"
"selection-color: rgb(85, 0, 255);")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.MaxConf = QtWidgets.QLineEdit(self.centralwidget)
        self.MaxConf.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.MaxConf.setObjectName("MaxConf")
        self.gridLayout.addWidget(self.MaxConf, 11, 1, 1, 1)
        self.MinConf = QtWidgets.QLineEdit(self.centralwidget)
        self.MinConf.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.MinConf.setObjectName("MinConf")
        self.gridLayout.addWidget(self.MinConf, 9, 1, 1, 1)
        self.max_length_rule_label = QtWidgets.QLabel(self.centralwidget)
        self.max_length_rule_label.setObjectName("max_length_rule_label")
        self.gridLayout.addWidget(self.max_length_rule_label, 4, 1, 1, 1)
        self.max_con_label = QtWidgets.QLabel(self.centralwidget)
        self.max_con_label.setObjectName("max_con_label")
        self.gridLayout.addWidget(self.max_con_label, 10, 1, 1, 1)
        self.Search_rule_label = QtWidgets.QLabel(self.centralwidget)
        self.Search_rule_label.setObjectName("Search_rule_label")
        self.gridLayout.addWidget(self.Search_rule_label, 13, 2, 1, 1)
        self.rule_to_search = QtWidgets.QLineEdit(self.centralwidget)
        self.rule_to_search.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.rule_to_search.setObjectName("rule_to_search")
        self.gridLayout.addWidget(self.rule_to_search, 15, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 16, 2, 1, 1)
        self.searched_output_rules = QtWidgets.QTextBrowser(self.centralwidget)
        self.searched_output_rules.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.searched_output_rules.setObjectName("searched_output_rules")
        self.gridLayout.addWidget(self.searched_output_rules, 17, 2, 1, 1)
        self.ruleLength_tb = QtWidgets.QLineEdit(self.centralwidget)
        self.ruleLength_tb.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ruleLength_tb.setObjectName("ruleLength_tb")
        self.gridLayout.addWidget(self.ruleLength_tb, 5, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 12, 1, 1, 1)
        self.ShowPath = QtWidgets.QLineEdit(self.centralwidget)
        self.ShowPath.setObjectName("ShowPath")
        self.gridLayout.addWidget(self.ShowPath, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 12, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 2, 1, 1)
        self.AlgorithmPicker = QtWidgets.QComboBox(self.centralwidget)
        self.AlgorithmPicker.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.AlgorithmPicker.setObjectName("AlgorithmPicker")
        self.gridLayout.addWidget(self.AlgorithmPicker, 5, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 13, 1, 1, 1)
        self.min_con_label = QtWidgets.QLabel(self.centralwidget)
        self.min_con_label.setObjectName("min_con_label")
        self.gridLayout.addWidget(self.min_con_label, 8, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setStyleSheet("background-color: rgb(80, 80, 80);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 11, 2, 1, 1)
        self.index_label = QtWidgets.QLabel(self.centralwidget)
        self.index_label.setObjectName("index_label")
        self.gridLayout.addWidget(self.index_label, 2, 1, 1, 1)
        self.index_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.index_combo_box.setObjectName("index_combo_box")
        self.gridLayout.addWidget(self.index_combo_box, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
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
        self.actionTo_open_an_xlsx_file = QtWidgets.QAction(MainWindow)
        self.actionTo_open_an_xlsx_file.setObjectName("actionTo_open_an_xlsx_file")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addAction(self.actionOpen)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Apriori"))
        self.Run.setText(_translate("MainWindow", "Run"))
        self.label_2.setText(_translate("MainWindow", "You have Entered :"))
        self.max_length_rule_label.setText(_translate("MainWindow", "Maximum length of the rule :"))
        self.max_con_label.setText(_translate("MainWindow", "Maximum confidence:"))
        self.Search_rule_label.setText(_translate("MainWindow", "Search Rule : "))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.label.setText(_translate("MainWindow", "Algorithm To Use :"))
        self.label_6.setText(_translate("MainWindow", "All Rules :"))
        self.min_con_label.setText(_translate("MainWindow", "Minimum confidence:"))
        self.pushButton_2.setText(_translate("MainWindow", "Save output to an external file."))
        self.index_label.setText(_translate("MainWindow", "Select the Index Column of the database :"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionTo_open_an_xlsx_file.setText(_translate("MainWindow", "to open an xlsx file"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
