from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import re
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
        self.index_combo_box.addItems(self.columnheader)

        self.ShowPath.setText(self.path)
        print(self.path)

    def run(self):
        print(self.AlgorithmPicker.currentText())
        if(self.AlgorithmPicker.currentText() == "Apriori Algorithm"):
            '''do apriori work'''
            self.AprioriInstance = apriori(address=self.path,min = int(self.min_freq_tb.text()),minConf=float(self.MinConf.text()),maxConf = float(self.MaxConf.text()),invNo=self.index_combo_box.currentText(),rules_len = int(self.ruleLength_tb.text()))
            self.results = self.AprioriInstance.finalRules
            self.output()

    def output(self):

        '''show the output of the program'''
        PATTERNS = ["Good marks in ","Average marks in ","Poor marks in "]

        ''' A dictionary which stores the name of the subject as keys and their occurence in the course as the value which means courses in the
            first semester will have lower number than courses in the later part of the curriculum'''
        self.Chronological_order = {}
        self.count = 0
        for subject in self.AprioriInstance.columnheader:
            self.Chronological_order[subject] = self.count
            self.count+=1

        ''' A dictionary that will store all the valid rules'''
        self.relations = {}

        for items in self.AprioriInstance.finalRules:
            if(items != 1):
                for rules in self.AprioriInstance.finalRules[items]:
                    main_stuff = rules
                    rules,percentage = rules.split(": ")
                    left_part,right_part = rules.split('=>')
                    left_part = left_part[1:-1]
                    right_part = right_part[1:-1]
                    left_part = left_part.split(", ")
                    right_part = right_part.split(", ")
                    left_subjects = []
                    right_subjects = []
                    for items_ in left_part:
                        for pattern in PATTERNS:
                            if(re.search(pattern,items_)):
                                left_subjects.append(items_.replace(pattern,""))
                    for items_ in right_part:
                        for pattern in PATTERNS:
                            if(re.search(pattern,items_)):
                                right_subjects.append(items_.replace(pattern,""))


                    subjects_in_this_rule = tuple(sorted([subject for subject in left_subjects]+[subject for subject in right_subjects]))

                    if all(self.Chronological_order[subject_in_left[1:-1]] < self.Chronological_order[subject_in_right[1:-1]] for subject_in_left in left_subjects for subject_in_right in right_subjects ):
                        if(float(percentage[:-1])>75):
                            if(subjects_in_this_rule not in self.relations):
                                self.relations[subjects_in_this_rule] = [main_stuff]
                            else:
                                self.relations[subjects_in_this_rule].append(main_stuff)

        for relation in self.relations.keys():
            str = "Relationship between : "
            for subjects in relation:
                str+=subjects[1:-1]+", "
            self.OutputRules.append(str+"\n")

    def search(self):

        if(len(self.rule_to_search.text())>0):
            subjects = self.rule_to_search.text().split(",")
            for i in range(len(subjects)):
                subjects[i] = subjects[i].strip()
            for relation in self.relations:
                if(all(("'"+subject+"'") in relation for subject in subjects)):
                    str = "Relationship between : "
                    for subs in relation:
                        str+=subs[1:-1]+", "
                    self.searched_output_rules.append(str)
                    for items in self.relations[relation]:
                        self.searched_output_rules.append(items)
                    self.searched_output_rules.append("\n")

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1281, 954)
        MainWindow.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.532, y1:0, x2:0.538, y2:1, stop:0 rgba(233, 234, 194, 255), stop:1 rgba(255, 255, 255, 255))\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.length_of_the_rule_to_search_label = QtWidgets.QLabel(self.centralwidget)
        self.length_of_the_rule_to_search_label.setObjectName("length_of_the_rule_to_search_label")
        self.gridLayout.addWidget(self.length_of_the_rule_to_search_label, 18, 2, 1, 1)

        self.Run = QtWidgets.QPushButton(self.centralwidget)
        self.Run.setStyleSheet("background-color: rgb(80, 80, 80);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.Run.setObjectName("Run")
        self.Run.clicked.connect(self.run)

        self.gridLayout.addWidget(self.Run, 11, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 6, 2, 1, 1)
        self.max_con_label = QtWidgets.QLabel(self.centralwidget)
        self.max_con_label.setObjectName("max_con_label")
        self.gridLayout.addWidget(self.max_con_label, 12, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 14, 2, 1, 1)
        self.index_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.index_combo_box.setObjectName("index_combo_box")
        self.gridLayout.addWidget(self.index_combo_box, 3, 1, 1, 1)
        self.searched_output_rules = QtWidgets.QTextBrowser(self.centralwidget)
        self.searched_output_rules.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.searched_output_rules.setObjectName("searched_output_rules")
        self.gridLayout.addWidget(self.searched_output_rules, 21, 2, 1, 1)
        self.min_con_label = QtWidgets.QLabel(self.centralwidget)
        self.min_con_label.setObjectName("min_con_label")
        self.gridLayout.addWidget(self.min_con_label, 10, 1, 1, 1)
        self.save_to_file_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_to_file_button.setStyleSheet("background-color: rgb(80, 80, 80);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.save_to_file_button.setObjectName("save_to_file_button")
        self.gridLayout.addWidget(self.save_to_file_button, 13, 2, 1, 1)
        self.index_label = QtWidgets.QLabel(self.centralwidget)
        self.index_label.setObjectName("index_label")
        self.gridLayout.addWidget(self.index_label, 2, 1, 1, 1)
        self.MinConf = QtWidgets.QLineEdit(self.centralwidget)
        self.MinConf.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.MinConf.setObjectName("MinConf")
        self.gridLayout.addWidget(self.MinConf, 11, 1, 1, 1)
        self.min_freq_label = QtWidgets.QLabel(self.centralwidget)
        self.min_freq_label.setObjectName("min_freq_label")
        self.gridLayout.addWidget(self.min_freq_label, 4, 1, 1, 1)
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setObjectName("searchButton")
        self.searchButton.clicked.connect(self.search)

        self.gridLayout.addWidget(self.searchButton, 20, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("font: 75 9pt \"Yu Gothic UI Semibold\";\n"
"selection-color: rgb(85, 0, 255);")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.max_length_rule_label = QtWidgets.QLabel(self.centralwidget)
        self.max_length_rule_label.setObjectName("max_length_rule_label")
        self.gridLayout.addWidget(self.max_length_rule_label, 6, 1, 1, 1)
        self.ShowPath = QtWidgets.QLineEdit(self.centralwidget)
        self.ShowPath.setObjectName("ShowPath")
        self.gridLayout.addWidget(self.ShowPath, 1, 2, 1, 1)
        self.ruleLength_tb = QtWidgets.QLineEdit(self.centralwidget)
        self.ruleLength_tb.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ruleLength_tb.setObjectName("ruleLength_tb")
        self.gridLayout.addWidget(self.ruleLength_tb, 7, 1, 1, 1)

        self.AlgorithmPicker = QtWidgets.QComboBox(self.centralwidget)
        self.AlgorithmPicker.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.AlgorithmPicker.setObjectName("AlgorithmPicker")
        self.AlgorithmPicker.addItem("Apriori Algorithm")
        self.AlgorithmPicker.addItem("FP Growth Algorithm")

        self.gridLayout.addWidget(self.AlgorithmPicker, 7, 2, 1, 1)
        self.MaxConf = QtWidgets.QLineEdit(self.centralwidget)
        self.MaxConf.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.MaxConf.setObjectName("MaxConf")
        self.gridLayout.addWidget(self.MaxConf, 13, 1, 1, 1)
        self.OutputRules = QtWidgets.QTextBrowser(self.centralwidget)
        self.OutputRules.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.OutputRules.setObjectName("OutputRules")
        self.gridLayout.addWidget(self.OutputRules, 17, 1, 5, 1)
        self.Search_rule_label = QtWidgets.QLabel(self.centralwidget)
        self.Search_rule_label.setObjectName("Search_rule_label")
        self.gridLayout.addWidget(self.Search_rule_label, 15, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 15, 1, 1, 1)
        self.rule_to_search = QtWidgets.QLineEdit(self.centralwidget)
        self.rule_to_search.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.rule_to_search.setObjectName("rule_to_search")
        self.gridLayout.addWidget(self.rule_to_search, 17, 2, 1, 1)
        self.min_freq_tb = QtWidgets.QLineEdit(self.centralwidget)
        self.min_freq_tb.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.min_freq_tb.setObjectName("min_freq_tb")
        self.gridLayout.addWidget(self.min_freq_tb, 5, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 14, 1, 1, 1)

        self.length_of_the_rule_to_search_tb = QtWidgets.QLineEdit(self.centralwidget)
        self.length_of_the_rule_to_search_tb.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.length_of_the_rule_to_search_tb.setObjectName("length_of_the_rule_to_search_tb")

        self.gridLayout.addWidget(self.length_of_the_rule_to_search_tb, 19, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1281, 26))
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
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addAction(self.actionOpen)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Apriori"))
        self.length_of_the_rule_to_search_label.setText(_translate("MainWindow", "Length of the rule :"))
        self.Run.setText(_translate("MainWindow", "Run"))
        self.label.setText(_translate("MainWindow", "Algorithm To Use :"))
        self.max_con_label.setText(_translate("MainWindow", "Maximum confidence:"))
        self.min_con_label.setText(_translate("MainWindow", "Minimum confidence:"))
        self.save_to_file_button.setText(_translate("MainWindow", "Save output to an external file."))
        self.index_label.setText(_translate("MainWindow", "Select the Index Column of the database :"))
        self.min_freq_label.setText(_translate("MainWindow", "Minimum_frequency:"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.label_2.setText(_translate("MainWindow", "You have Entered :"))
        self.max_length_rule_label.setText(_translate("MainWindow", "Maximum length of the rule :"))
        self.Search_rule_label.setText(_translate("MainWindow", "Search Rule : "))
        self.label_6.setText(_translate("MainWindow", "All Rules :"))
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
