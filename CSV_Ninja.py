# -*- coding: utf-8 -*-


# Import Modules
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import csv
import os
from os.path import basename
import pandas as pd
import webbrowser, os


#Variables
delimeter = ","
x = []
fileName =""
csvfile =""
message = "Welcome to CSV Ninja."
folderpath =""
filenoext = ""
msg_text = ""
msg_info = ""
filename =""
msg_icon = ""
IntervalValue = 0
PartValue = 0
SB_singleR_Value = 0
SB_fromR_Value = 0
SB_toR_Value = 0
row_number = 0
delim = [",",".","  ",";"]
cur_delim =""
req_delim =""


#GUI for Main window
class Ui_CSV_Tools(object):
    def setupUi(self, CSV_Tools):
        CSV_Tools.setObjectName("CSV_Tools")
        #CSV_Tools.resize(615, 482)
        CSV_Tools.showFullScreen()
        CSV_Tools.showMaximized()
        CSV_Tools.setWindowIcon(QtGui.QIcon('Icon.png'))
        self.centralwidget = QtWidgets.QWidget(CSV_Tools)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setRowCount(1000)
        self.tableWidget.setColumnCount(1000)
        self.tableWidget.setObjectName("tableWidget")
        self.gridLayout_5.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.OpenButton = QtWidgets.QPushButton(self.groupBox_2)
        self.OpenButton.setObjectName("OpenButton")
        self.gridLayout_2.addWidget(self.OpenButton, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.DelimButton = QtWidgets.QPushButton(self.groupBox)
        self.DelimButton.setObjectName("DelimButton")
        self.gridLayout.addWidget(self.DelimButton, 0, 2, 1, 1)
        self.MergeButton = QtWidgets.QPushButton(self.groupBox)
        self.MergeButton.setObjectName("MergeButton")
        self.gridLayout.addWidget(self.MergeButton, 1, 0, 1, 1)
        self.SplitButton = QtWidgets.QPushButton(self.groupBox)
        self.SplitButton.setObjectName("SplitButton")
        self.gridLayout.addWidget(self.SplitButton, 0, 0, 1, 1)
        self.DeleteButton = QtWidgets.QPushButton(self.groupBox)
        self.DeleteButton.setObjectName("DeleteButton")
        self.gridLayout.addWidget(self.DeleteButton, 0, 1, 1, 1)
        self.TransposeButton = QtWidgets.QPushButton(self.groupBox)
        self.TransposeButton.setObjectName("TransposeButton")
        self.gridLayout.addWidget(self.TransposeButton, 1, 1, 1, 1)
        self.ArrangeButton = QtWidgets.QPushButton(self.groupBox)
        self.ArrangeButton.setEnabled(True)
        self.ArrangeButton.setObjectName("ArrangeButton")
        self.gridLayout.addWidget(self.ArrangeButton, 1, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setObjectName("checkBox")
        self.checkBox.stateChanged.connect(self.viewtable)
        self.gridLayout_4.addWidget(self.checkBox, 0, 2, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.rb_comma = QtWidgets.QRadioButton(self.groupBox_3)
        self.rb_comma.setObjectName("rb_comma")
        self.verticalLayout_2.addWidget(self.rb_comma)
        self.rb_tab = QtWidgets.QRadioButton(self.groupBox_3)
        self.rb_tab.setObjectName("rb_tab")
        self.verticalLayout_2.addWidget(self.rb_tab)
        self.rb_semicolon = QtWidgets.QRadioButton(self.groupBox_3)
        self.rb_semicolon.setObjectName("rb_semicolon")
        self.verticalLayout_2.addWidget(self.rb_semicolon)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.rb_custom = QtWidgets.QRadioButton(self.groupBox_3)
        self.rb_custom.setObjectName("rb_custom")
        self.verticalLayout_3.addWidget(self.rb_custom)
        self.customvalue = QtWidgets.QLineEdit(self.groupBox_3)
        self.customvalue.setObjectName("customvalue")
        self.verticalLayout_3.addWidget(self.customvalue)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addWidget(self.groupBox_3)
        self.gridLayout_5.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_5)
        self.tableWidget.raise_()
        self.groupBox.raise_()
        CSV_Tools.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CSV_Tools)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 615, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        CSV_Tools.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CSV_Tools)
        self.statusbar.setObjectName("statusbar")
        CSV_Tools.setStatusBar(self.statusbar)
        CSV_Tools.statusBar().showMessage(message)
        self.actionAbout = QtWidgets.QAction(CSV_Tools)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout.triggered.connect(self.about)
        self.actionHelp = QtWidgets.QAction(CSV_Tools)
        self.actionHelp.setObjectName("actionHelp")
        self.actionHelp.triggered.connect(self.help)
        self.actionOpen = QtWidgets.QAction(CSV_Tools)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.triggered.connect(self.on_click)
        self.actionExit = QtWidgets.QAction(CSV_Tools)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(self.exit_)
        self.actionSplit = QtWidgets.QAction(CSV_Tools)
        self.actionSplit.setObjectName("actionSplit")
        self.actionSplit.triggered.connect(self.split)
        self.actionMerge = QtWidgets.QAction(CSV_Tools)
        self.actionMerge.setObjectName("actionMerge")
        self.actionMerge.triggered.connect(self.merge)
        self.actionDelete = QtWidgets.QAction(CSV_Tools)
        self.actionDelete.setObjectName("actionDelete")
        self.actionDelete.triggered.connect(self.delete)
        self.actionTranspose = QtWidgets.QAction(CSV_Tools)
        self.actionTranspose.setObjectName("actionTranspose")
        self.actionTranspose.triggered.connect(self.transpose)
        self.actionChange_Delimiter = QtWidgets.QAction(CSV_Tools)
        self.actionChange_Delimiter.setObjectName("actionChange_Delimiter")
        self.actionChange_Delimiter.triggered.connect(self.change_delim)
        self.actionArrange_Columns = QtWidgets.QAction(CSV_Tools)
        self.actionArrange_Columns.setObjectName("actionArrange_Columns")
        self.actionArrange_Columns.triggered.connect(self.arrange)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionSplit)
        self.menuEdit.addAction(self.actionMerge)
        self.menuEdit.addAction(self.actionDelete)
        self.menuEdit.addAction(self.actionTranspose)
        self.menuEdit.addAction(self.actionChange_Delimiter)
        self.menuEdit.addAction(self.actionArrange_Columns)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionHelp)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.SplitButton.clicked.connect(self.split)
        self.MergeButton.clicked.connect(self.merge)
        self.DeleteButton.clicked.connect(self.delete)
        self.OpenButton.clicked.connect(self.on_click)
        self.TransposeButton.clicked.connect(self.transpose)
        self.DelimButton.clicked.connect(self.change_delim)
        self.ArrangeButton.clicked.connect(self.arrange)
        #self.sfButton.clicked.connect(self.searchreplace)
        self.retranslateUi(CSV_Tools)
        QtCore.QMetaObject.connectSlotsByName(CSV_Tools)



    def retranslateUi(self, CSV_Tools):
        _translate = QtCore.QCoreApplication.translate
        CSV_Tools.setWindowTitle(_translate("CSV_Tools", "CSV_Ninja"))
        self.groupBox_2.setTitle(_translate("CSV_Tools", "File :"))
        self.OpenButton.setText(_translate("CSV_Tools", "File &Open"))
        self.groupBox.setTitle(_translate("CSV_Tools", "Edit Tools :"))
        self.DelimButton.setToolTip(_translate("CSV_Tools", "Change Delimiters jfewhfov;;bwhv /n  o ;hwv; HG;G    G;G ;EWG;B  ;WUG"))
        self.DelimButton.setText(_translate("CSV_Tools", "&,/- ; :."))
        self.MergeButton.setToolTip(_translate("CSV_Tools", "Merge CSV"))
        self.MergeButton.setText(_translate("CSV_Tools", "&Merge"))
        self.SplitButton.setToolTip(_translate("CSV_Tools", "Split CSV"))
        self.SplitButton.setText(_translate("CSV_Tools", "&Split"))
        self.DeleteButton.setToolTip(_translate("CSV_Tools", "Delete Rows or Columns"))
        self.checkBox.setText(_translate("CSV_Tools", "&View Table"))
        self.DeleteButton.setText(_translate("CSV_Tools", "&Delete R/C"))
        self.TransposeButton.setToolTip(_translate("CSV_Tools", "Transpose Rows or Columns"))
        self.TransposeButton.setText(_translate("CSV_Tools", "&Transpose"))
        self.ArrangeButton.setToolTip(_translate("CSV_Tools", "Arrange Columns"))
        self.ArrangeButton.setText(_translate("CSV_Tools", "&Arrange"))
        self.menuFile.setTitle(_translate("CSV_Tools", "&File"))
        self.menuEdit.setTitle(_translate("CSV_Tools", "&Edit"))
        self.menuHelp.setTitle(_translate("CSV_Tools", "&Help"))
        self.actionOpen.setText(_translate("CSV_Tools", "&Open"))
        self.actionExit.setText(_translate("CSV_Tools", "&Exit"))
        self.actionSplit.setText(_translate("CSV_Tools", "&Split"))
        self.actionMerge.setText(_translate("CSV_Tools", "&Merge"))
        self.actionDelete.setText(_translate("CSV_Tools", "&Delete"))
        self.actionTranspose.setText(_translate("CSV_Tools", "&Transpose"))
        self.actionChange_Delimiter.setText(_translate("CSV_Tools", "&Change Delimiter"))
        self.actionArrange_Columns.setText(_translate("CSV_Tools", "&Arrange Columns"))
        self.actionAbout.setText(_translate("CSV_Tools", "&About"))
        self.actionHelp.setText(_translate("CSV_Tools", "&Help"))
        self.groupBox_3.setTitle(_translate("CSV_Tools", "Delimeter:"))
        self.rb_comma.setText(_translate("CSV_Tools", ",Comma"))
        self.rb_tab.setText(_translate("CSV_Tools", "Tab"))
        self.rb_semicolon.setText(_translate("CSV_Tools", "; Semi Colon"))
        self.rb_custom.setText(_translate("CSV_Tools", "Custom:"))





    def msg_window(self):
        global msg_text
        global msg_info
        global msg_icon
        msg = QMessageBox()
        msg.setIcon(msg_icon)
        msg.setText(msg_text)
        msg.setInformativeText(msg_info)
        msg.setWindowTitle("Information")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()



    def exit_(self):
        sys.exit()




#View table on selecting chck box
    def viewtable(self,state):
        self.checkdelim()
        global delimeter
        if state == QtCore.Qt.Checked:
            if fileName != "":
                global row_number
                with open(fileName) as csvfile:
                    csv_reader = csv.reader(csvfile, delimiter=delimeter)
                    for row_number, row_data in enumerate(csv_reader):
                        self.tableWidget.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                            self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

            else:
                self.checkBox.setChecked(False)
                global msg_icon
                global msg_text
                global msg_info
                msg_icon = QMessageBox.Warning
                msg_text = "No .csv file opened"
                msg_info = "Open .csv file"
                self.msg_window()

        else:
            if fileName == "":
                self.checkBox.setChecked(False)
            else:
                self.closetable()


    def checkdelim(self):
        global delimeter
        if self.rb_comma.isChecked():
            delimeter = ','
        elif self.rb_semicolon.isChecked():
            delimeter = ';'
        elif self.rb_tab.isChecked():
            delimeter = '\t'
        elif self.rb_custom.isChecked():
            delimeter = self.customvalue.text()
        else:
            delimeter =','

    ## File open dialog
    def on_click(self):
        global fileName
        fileName, _ = QFileDialog.getOpenFileName(None, "Select .csv file", ""," *.csv")
        global row_number
        global delimeter
        if fileName != "":
            message = fileName
            self.checkdelim()

            with open(fileName) as csvfile:
                global filenoext
                global folderpath

                filenoext = os.path.splitext(basename(fileName))[0]
                folderpath = os.path.dirname(fileName)
                csv_reader = csv.reader(csvfile, delimiter=delimeter)
                row_number = sum(1for row in csv_reader)
                CSV_Tools.statusBar().showMessage("Input file path : " + str(message) + "   Total Number of Rows = " + str(row_number))
        else:
            CSV_Tools.statusBar().showMessage("Welcome to CSV_Ninja")
            self.closetable()

    def closetable(self):
        #while (self.tableWidget.rowCount() > 0):
            #self.tableWidget.removeRow(0)
        self.tableWidget.clear()




    #Split button click event
    def split(self):
        split = QtWidgets.QDialog()
        ui = Ui_split()
        ui.setupUi(split)
        split.show()
        result = split.exec()

    # Merge button click event
    def merge(self):
        merge = QtWidgets.QDialog()
        ui = Ui_merge()
        ui.setupUi(merge)
        merge.show()
        mergeresult = merge.exec()

    # Delete button click event
    def delete(self):
        delete = QtWidgets.QDialog()
        ui = Ui_delete_rc()
        ui.setupUi(delete)
        delete.show()
        deleteresult = delete.exec()

    # Transpose button click event
    def transpose(self):
        global msg_text
        global msg_info
        global msg_icon
        if fileName != "":
            myfile = pd.read_csv(fileName).T.to_csv(str(folderpath)+"/"+str(filenoext)+"_"+"Transpose"+".csv",header=False)
            msg_icon = QMessageBox.Information
            msg_text = "Completed"
            msg_info = "File saved successfully"
            self.msg_window()

        else:
            msg_icon = QMessageBox.Warning
            msg_text = "No .csv file opened"
            msg_info = "Open .csv file"
            self.msg_window()


    # Change delimeter but-ton click event
    def change_delim(self):
        delim = QtWidgets.QDialog()
        ui = Ui_ChangeDel()
        ui.setupUi(delim)
        delim.show()
        result = delim.exec()


    def arrange(self):
        arrange = QtWidgets.QDialog()
        ui = Ui_arrange_dialog()
        ui.setupUi(arrange)
        arrange.show()
        result = arrange.exec()


    # Show about dialog box ==============
    def about(self):
        about = QtWidgets.QDialog()
        ui = Ui_About()
        ui.setupUi(about)
        about.show()
        result = about.exec()

    def help(self):
        webbrowser.open('file://' + os.path.realpath("CSV_Ninja_UserGuide.htm"))


###==========About window =========
class Ui_About(QtWidgets.QDialog):
    def __init__(self):
        super(Ui_About, self).__init__()

    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(357, 250)
        About.setWindowFlags(
            QtCore.Qt.Window |
            QtCore.Qt.CustomizeWindowHint |
            QtCore.Qt.WindowTitleHint |
            QtCore.Qt.WindowCloseButtonHint
        )
        About.setWindowIcon(QtGui.QIcon('Icon.png'))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(About)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(About)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icon.png"))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(About)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(About)
        self.label_4.setWordWrap(True)
        self.label_4.setOpenExternalLinks(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.buttonBox = QtWidgets.QDialogButtonBox(About)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(About)
        self.buttonBox.accepted.connect(About.accept)
        self.buttonBox.rejected.connect(About.reject)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "Dialog"))
        self.label_2.setText(_translate("About", "About CSV_Ninja"))
        self.label_4.setText(_translate("About",
                                        "<html><head/><body><p><br/></p><p>Version 1.0.0</p><p>CSV_Ninja is an application to do basic<br/>operations on CSV file.</p><p><br/>This tool is developed by appIsolutions.</p><p>For feedback and suggetions:</p><p><a href=\"https://appisolutions.wordpress.com\"><span style=\" text-decoration: underline; color:#0000ff;\">https://appisolutions.wordpress.com</span></a></p></body></html>"))


###========= This is start of split function ===============
class Ui_split(QtWidgets.QDialog):

    def __init__(self):
        super(Ui_split, self).__init__()
    
    def setupUi(self, split):
        split.setObjectName("split")
        split.resize(205, 247)
        split.setWindowFlags(
            QtCore.Qt.Window |
            QtCore.Qt.CustomizeWindowHint |
            QtCore.Qt.WindowTitleHint |
            QtCore.Qt.WindowCloseButtonHint
        )
        split.setWindowIcon(QtGui.QIcon('Icon.png'))
        self.verticalLayout = QtWidgets.QVBoxLayout(split)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(split)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.RB_intervals = QtWidgets.QRadioButton(self.groupBox)
        self.RB_intervals.setObjectName("RB_intervals")
        self.verticalLayout_2.addWidget(self.RB_intervals)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.IntervalSpin = QtWidgets.QSpinBox(self.groupBox)
        self.IntervalSpin.setMaximum(10000000)
        self.IntervalSpin.setSingleStep(10)
        self.IntervalSpin.setObjectName("IntervalSpin")
        self.horizontalLayout_3.addWidget(self.IntervalSpin)
        self.IntervalSpin.valueChanged.connect(self.intervalvalue)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.RB_Parts = QtWidgets.QRadioButton(self.groupBox)
        self.RB_Parts.setObjectName("RB_Parts")
        self.verticalLayout_2.addWidget(self.RB_Parts)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.PartsSpin = QtWidgets.QSpinBox(self.groupBox)
        self.PartsSpin.setMaximum(10000000)
        self.PartsSpin.setObjectName("PartsSpin")
        self.horizontalLayout_2.addWidget(self.PartsSpin)
        self.PartsSpin.valueChanged.connect(self.partvalue)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.RB_CValue = QtWidgets.QRadioButton(self.groupBox)
        self.RB_CValue.setObjectName("RB_CValue")
        self.RB_CValue.toggled.connect(self.fill)
        self.verticalLayout_2.addWidget(self.RB_CValue)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ColumnValue = QtWidgets.QLabel(self.groupBox)
        self.ColumnValue.setObjectName("ColumnValue")
        self.horizontalLayout.addWidget(self.ColumnValue)
        self.ColumnName = QtWidgets.QComboBox(self.groupBox)
        self.ColumnName.setObjectName("ColumnName")
        self.horizontalLayout.addWidget(self.ColumnName)
        #self.ColumnName.textChanged.connect(self.columnvalue)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(split)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.retranslateUi(split)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(split.reject)
        QtCore.QMetaObject.connectSlotsByName(split)

    def retranslateUi(self, split):
        _translate = QtCore.QCoreApplication.translate
        split.setWindowTitle(_translate("split", "Split CSV"))
        self.groupBox.setTitle(_translate("split", "Parameters :"))
        self.RB_intervals.setText(_translate("split", "Split at equal &intervals"))
        self.label.setText(_translate("split", "Intervals           : "))
        self.RB_Parts.setText(_translate("split", "Split in equal &parts"))
        self.label_2.setText(_translate("split", "Number of Parts : "))
        self.RB_CValue.setText(_translate("split", "Split Based on &column value"))
        self.ColumnValue.setText(_translate("split", "Column Name : "))

    def intervalvalue(self):
        global IntervalValue
        IntervalValue = self.IntervalSpin.value()

    def partvalue(self):
        global PartValue
        PartValue = self.PartsSpin.value()

    def msg_window(self):
        global msg_text
        global msg_info
        global msg_icon
        msg = QMessageBox()
        msg.setIcon(msg_icon)
        msg.setText(msg_text)
        msg.setInformativeText(msg_info)
        msg.setWindowTitle("Information")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        # msg.buttonClicked.connect(msgbtn)

        retval = msg.exec_()

    def fill(self):
        with open(fileName) as fin:
            csvin = csv.DictReader(fin)
            fieldnames = csvin.fieldnames
            self.ColumnName.addItems(fieldnames)
            self.ColumnName.currentIndexChanged.connect(self.ColVal)


    def ColVal(self, value):
        global ColumnValue
        global txt
        ColumnValue = value
        ColumnValue = self.ColumnName.currentText()


    def accept(self):
        if fileName == "":
            global msg_icon
            global msg_text
            global msg_info
            msg_icon = QMessageBox.Warning
            msg_text = "No .csv file opened"
            msg_info = "Open .csv file"
            self.msg_window()

        else:
            if self.RB_intervals.isChecked():
                if IntervalValue > row_number+1 :
                    msg_icon = QMessageBox.Warning
                    msg_text = "Interval value is more then Row count"
                    msg_info = "Change interval value"
                    self.msg_window()
                elif IntervalValue == 0:
                    msg_icon = QMessageBox.Warning
                    msg_text = "No interval value"
                    msg_info = "Please enter Interval Value"
                    self.msg_window()
                else:
                    csvfile = open(fileName, 'r').readlines()
                    filename = 1
                    for i in range(len(csvfile)):
                        if i % IntervalValue == 0:
                            open(str(folderpath)+"/"+str(filenoext)+"_"+str(filename)+".csv",'w+').writelines(csvfile[i:i + IntervalValue])
                            filename += 1

                    msg_icon = QMessageBox.Information
                    msg_text = "Completed"
                    msg_info = "File split successfully"
                    self.msg_window()


            elif self.RB_Parts.isChecked():
                if PartValue > row_number+1 :
                    msg_icon = QMessageBox.Warning
                    msg_text = "Part value is more then Row count"
                    msg_info = "Change Part value"
                    self.msg_window()
                elif PartValue == 0:
                    msg_icon = QMessageBox.Warning
                    msg_text = "No Part value"
                    msg_info = "Please enter Part Value"
                    self.msg_window()
                else:
                    chunksize = int(round(((row_number+1)/PartValue),0))
                    csvfile = open(fileName, 'r').readlines()
                    #file = 1
                    start = 1
                    end = int(start)*int(chunksize)
                    for i in range(len(csvfile)):
                        if i % chunksize == 0:
                            #open(str(file) + '.csv', 'w+').writelines(csvfile[i:i + chunksize])
                            open(str(folderpath) + "/" + str(filenoext) + "_" + str(start) +"_"+str(end)+ ".csv", 'w+').writelines(csvfile[i:i + chunksize])
                            start += 1

                    msg_icon = QMessageBox.Information
                    msg_text = "Completed"
                    msg_info = "File split successfully"
                    self.msg_window()




            elif self.RB_CValue.isChecked():
                with open(fileName) as fin:
                    csvin = csv.DictReader(fin)
                    fieldnames = csvin.fieldnames
                    if ColumnValue in fieldnames:
                            outputs = {}
                            for row in csvin:
                                cat = row[str(ColumnValue)]
                                # Open a new file and write the header
                                if cat not in outputs:
                                    #fout = open(str(folderpath) + "/" +'{}.csv'.format(cat), 'w',newline='')
                                    fout = open(str(folderpath) + "/" +str(filenoext)+"_"+str(cat)+'.csv', 'w',newline='')
                                    dw = csv.DictWriter(fout, fieldnames)
                                    #dw.writeheader()
                                    outputs[cat] = fout, dw
                                # Always write the row
                                outputs[cat][1].writerow(row)
                            # Close all the files
                            for fout, _ in outputs.values():
                                fout.close()
                            msg_icon = QMessageBox.Information
                            msg_text = "Completed"
                            msg_info = "File split successfully"
                            self.msg_window()

                    else:
                        msg_icon = QMessageBox.Warning
                        msg_text = "Missing Column Value"
                        msg_info = "Enter correct Column Name"
                        self.msg_window()



###========= This is end of split function ===============



###==============Start of Merge function========

class Ui_merge(QtWidgets.QDialog):
    def __init__(self):
        super(Ui_merge, self).__init__()

    def setupUi(self, Merge):
        Merge.setObjectName("Merge")
        Merge.resize(257, 236)
        Merge.setWindowFlags(
            QtCore.Qt.Window |
            QtCore.Qt.CustomizeWindowHint |
            QtCore.Qt.WindowTitleHint |
            QtCore.Qt.WindowCloseButtonHint
        )
        Merge.setWindowIcon(QtGui.QIcon('Icon.png'))
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Merge)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(Merge)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkbox_mergeall = QtWidgets.QRadioButton(self.groupBox)
        self.checkbox_mergeall.setObjectName("checkbox_mergeall")
        self.verticalLayout.addWidget(self.checkbox_mergeall)
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.checkbox_contains = QtWidgets.QRadioButton(self.groupBox)
        self.checkbox_contains.setObjectName("checkbox_contains")
        self.verticalLayout.addWidget(self.checkbox_contains)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.csv_path = QtWidgets.QPlainTextEdit(Merge)
        self.csv_path.setObjectName("csv_path")
        self.verticalLayout_3.addWidget(self.csv_path)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.buttonBox = QtWidgets.QDialogButtonBox(Merge)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_4.addWidget(self.buttonBox)

        self.retranslateUi(Merge)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(Merge.reject)
        QtCore.QMetaObject.connectSlotsByName(Merge)

    def retranslateUi(self, Merge):
        _translate = QtCore.QCoreApplication.translate
        Merge.setWindowTitle(_translate("Merge", "Merge CSV"))
        self.groupBox.setTitle(_translate("Merge", "Parameters :"))
        self.checkbox_mergeall.setToolTip(_translate("Merge", "check to merge all csv in a folder"))
        self.checkbox_mergeall.setText(_translate("Merge", "Merge &All"))
        self.checkbox_contains.setToolTip(_translate("Merge", "Check this to select files which has given text"))
        self.checkbox_contains.setText(_translate("Merge", "Merge file name which &Contains:"))
        self.lineEdit.setText(_translate("Merge", "Enter text here"))
        self.csv_path.setPlainText(_translate("Merge", "Enter folder path here"))



    def accept(self):
        global path
        global msg_icon
        global msg_text
        global msg_info
        path = self.csv_path.toPlainText()
        if os.path.exists(path):
            with open(path+"\merged.csv",'w') as csvfile:
                if self.checkbox_mergeall.isChecked():
                    for file in os.listdir(str(path)):
                        if file.endswith(".csv"):
                            if file != "merged.csv":
                                fileName = str(path)+"\\"+file
                                for line in open(fileName,'r'):
                                    csvfile.write(line)
                    msg_icon = QMessageBox.Warning
                    msg_text = "Completed"
                    msg_info = "File merged Successfully"
                    Ui_split.msg_window(self)

                elif self.checkbox_contains.isChecked():
                    contain_text = self.lineEdit.text()
                    for file in os.listdir(str(path)):
                        if file.endswith(".csv"):
                            if file != "merged.csv":
                                if contain_text in file:
                                    fileName = str(path) + "\\" + file
                                    for line in open(fileName, 'r'):
                                        csvfile.write(line)
                    msg_icon = QMessageBox.Warning
                    msg_text = "Completed"
                    msg_info = "File merged Successfully"
                    Ui_split.msg_window(self)



        else:
            msg_icon = QMessageBox.Warning
            msg_text = "Path Not Exist"
            msg_info = "Enter corret file path"
            Ui_split.msg_window(self)


#End of merge function===========================

#start of delete function========

class Ui_delete_rc(QtWidgets.QDialog):
    global msg_icon
    global msg_text
    global msg_info

    def __init__(self):
        super(Ui_delete_rc, self).__init__()

    def setupUi(self, delete_rc):
        delete_rc.setObjectName("delete_rc")
        delete_rc.resize(252, 294)
        delete_rc.setWindowFlags(
            QtCore.Qt.Window |
            QtCore.Qt.CustomizeWindowHint |
            QtCore.Qt.WindowTitleHint |
            QtCore.Qt.WindowCloseButtonHint
        )
        delete_rc.setWindowIcon(QtGui.QIcon('Icon.png'))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(delete_rc)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_3 = QtWidgets.QGroupBox(delete_rc)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.RB_SingleR = QtWidgets.QRadioButton(self.groupBox_3)
        self.RB_SingleR.setObjectName("RB_SingleR")
        self.horizontalLayout_2.addWidget(self.RB_SingleR)
        self.SB_singleR = QtWidgets.QSpinBox(self.groupBox_3)
        self.SB_singleR.setObjectName("SB_singleR")
        self.horizontalLayout_2.addWidget(self.SB_singleR)
        self.SB_singleR.valueChanged.connect(self.SB_singleR_Value)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.RB_SingleC = QtWidgets.QRadioButton(self.groupBox_3)
        self.RB_SingleC.setObjectName("RB_SingleC")
        self.RB_SingleC.toggled.connect(self.fill)
        self.horizontalLayout.addWidget(self.RB_SingleC)
        self.singleC = QtWidgets.QComboBox(self.groupBox_3)
        self.singleC.setObjectName("singleC")
        self.horizontalLayout.addWidget(self.singleC)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(self.groupBox_3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.RB_multiple_R = QtWidgets.QRadioButton(self.groupBox_3)
        self.RB_multiple_R.setObjectName("RB_multiple_R")
        self.verticalLayout.addWidget(self.RB_multiple_R)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.SB_fromR = QtWidgets.QSpinBox(self.groupBox_3)
        self.SB_fromR.setObjectName("SB_fromR")
        self.SB_fromR.setMaximum(10000000)
        self.horizontalLayout_3.addWidget(self.SB_fromR)
        self.SB_fromR.valueChanged.connect(self.SB_fromR_Value)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.SB_toR = QtWidgets.QSpinBox(self.groupBox_3)
        self.SB_toR.setMaximum(10000000)
        self.SB_toR.setObjectName("SB_toR")
        self.horizontalLayout_4.addWidget(self.SB_toR)
        self.SB_toR.valueChanged.connect(self.SB_toR_Value)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.RB_multiple_C = QtWidgets.QRadioButton(self.groupBox_3)
        self.RB_multiple_C.setObjectName("RB_multiple_C")
        self.RB_multiple_C.toggled.connect(self.fillC)
        self.verticalLayout.addWidget(self.RB_multiple_C)
        self.Multiple_C = QtWidgets.QListWidget(self.groupBox_3)
        self.Multiple_C.setObjectName("Multiple_C")
        self.Multiple_C.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.verticalLayout.addWidget(self.Multiple_C)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.buttonBox = QtWidgets.QDialogButtonBox(delete_rc)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(delete_rc)
        self.buttonBox.accepted.connect(self.delete_accept)
        self.buttonBox.rejected.connect(delete_rc.reject)
        QtCore.QMetaObject.connectSlotsByName(delete_rc)

    def retranslateUi(self, delete_rc):
        _translate = QtCore.QCoreApplication.translate
        delete_rc.setWindowTitle(_translate("delete_rc", "Delete Row/Column"))
        self.groupBox_3.setTitle(_translate("delete_rc", "Delete Row/Column :"))
        self.RB_SingleR.setText(_translate("delete_rc", "Delete This &Row :"))
        self.RB_SingleC.setText(_translate("delete_rc", "Delete This &Column :"))
        self.RB_multiple_R.setText(_translate("delete_rc", "&Delete Row From - To :"))
        self.label.setText(_translate("delete_rc", "From :"))
        self.label_2.setText(_translate("delete_rc", "To :"))
        self.RB_multiple_C.setText(_translate("delete_rc", " Delete &Multiple columns :"))



    def fill(self):
        if fileName!="":
            if self.RB_SingleC.isChecked():
                with open(fileName) as fin:
                    csvin = csv.DictReader(fin)
                    fieldnames = csvin.fieldnames
                    self.singleC.addItems(fieldnames)
                    self.singleC.currentIndexChanged.connect(self.CB_changed)
        else:
            global msg_icon
            global msg_text
            global msg_info
            self.RB_SingleC.setChecked(False)
            msg_icon = QMessageBox.Warning
            msg_text = "No .csv file opened"
            msg_info = "Open .csv file"
            Ui_split.msg_window(self)

    def fillC(self):
        if fileName != "":
            if self.RB_multiple_C.isChecked():
                with open(fileName) as fin:
                    csvin = csv.DictReader(fin)
                    fieldnames = csvin.fieldnames
                    self.Multiple_C.addItems(fieldnames)
                    self.Multiple_C.itemClicked.connect(self.RB_Mchanged)
        else:
            global msg_icon
            global msg_text
            global msg_info
            msg_icon = QMessageBox.Warning
            msg_text = "No .csv file opened"
            msg_info = "Open .csv file"
            Ui_split.msg_window(self)
            self.RB_multiple_C.setChecked(False)


    def RB_Mchanged(self,value):
        global MultipleC_Value
        items = self.Multiple_C.selectedItems()
        global x
        x = []
        for i in range(len(items)):
            x.append(str(self.Multiple_C.selectedItems()[i].text()))


    def CB_changed(self,value):
        global CB_singleC_Value
        global txt
        CB_singleC_Value = value
        txt = self.singleC.currentText()


    def SB_singleR_Value(self):
        global SB_singleR_Value
        SB_singleR_Value = self.SB_singleR.value()

    def SB_fromR_Value(self):
        global SB_fromR_Value
        SB_fromR_Value = self.SB_fromR.value()

    def SB_toR_Value(self):
        global SB_toR_Value
        SB_toR_Value = self.SB_toR.value()

    def delete_accept(self):
        if fileName == "":
            global msg_icon
            global msg_text
            global msg_info
            msg_icon = QMessageBox.Warning
            msg_text = "No .csv file opened"
            msg_info = "Open .csv file"
            Ui_split.msg_window(self)

        else:
            csvfile = open(fileName, 'r').readlines()
            if self.RB_SingleR.isChecked():
                with open(str(folderpath) + "/"+str(filenoext)+"_"+str(SB_singleR_Value)+"_row_deleted.csv", 'w+') as fout:
                    i = 1
                    for row in csvfile:
                        if i != SB_singleR_Value:
                            fout.write(row)
                        i += 1
                msg_icon = QMessageBox.Information
                msg_text = "Completed"
                msg_info = "File saved successfully"
                Ui_split.msg_window(self)

            elif self.RB_SingleC.isChecked():
                with open(fileName,"r") as source:
                    rdr = csv.reader(source)
                    with open(str(folderpath) + "/" +str(filenoext)+"_"+ str(txt) + "_Column_deleted.csv", "w+",newline='') as result:
                        wtr = csv.writer(result)
                        for r in rdr:
                            del r[CB_singleC_Value]
                            wtr.writerow(r)

                msg_icon = QMessageBox.Information
                msg_text = "Completed"
                msg_info = "File saved successfully"
                Ui_split.msg_window(self)

            elif self.RB_multiple_R.isChecked():
                if SB_toR_Value <= row_number+1 and SB_fromR_Value <= row_number+1 and SB_fromR_Value < SB_toR_Value:
                        with open(str(folderpath) + "/" + str(filenoext)+"_"+str(SB_fromR_Value) +"_to_"+str(SB_toR_Value) + "_row_deleted.csv", 'w+') as fout:
                            i = 1
                            for row in csvfile:
                                if i < SB_fromR_Value or i > SB_toR_Value :
                                    fout.write(row)
                                i += 1
                        msg_icon = QMessageBox.Information
                        msg_text = "Completed"
                        msg_info = "File saved successfully"
                        Ui_split.msg_window(self)
                else:
                    msg_icon = QMessageBox.Information
                    msg_text = "Value error"
                    msg_info = "Check From row value and to Row value"
                    Ui_split.msg_window(self)



            elif self.RB_multiple_C.isChecked():
                myfile = pd.read_csv(fileName)
                myfile.drop(x,axis=1,inplace=True)
                myfile.to_csv(str(folderpath) + "/" +filenoext + "_Columns_deleted.csv",index=False)

                msg_icon = QMessageBox.Information
                msg_text = "Completed"
                msg_info = "File saved successfully"
                Ui_split.msg_window(self)

            else :
                msg_icon = QMessageBox.Information
                msg_text = "No option selected"
                msg_info = "Select one item and its parameters"
                Ui_split.msg_window(self)



###=======This is end of delete function and start of change_delimiter functions========
class Ui_ChangeDel(object):
    def setupUi(self, ChangeDel):
        ChangeDel.setObjectName("ChangeDel")
        ChangeDel.resize(190, 141)
        ChangeDel.setWhatsThis("")
        ChangeDel.setSizeGripEnabled(False)
        ChangeDel.setModal(False)
        ChangeDel.setWindowFlags(
            QtCore.Qt.Window |
            QtCore.Qt.CustomizeWindowHint |
            QtCore.Qt.WindowTitleHint |
            QtCore.Qt.WindowCloseButtonHint
        )
        ChangeDel.setWindowIcon(QtGui.QIcon('Icon.png'))
        self.verticalLayout = QtWidgets.QVBoxLayout(ChangeDel)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(ChangeDel)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_2.textChanged.connect(self.cur_delim)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.lineEdit.textChanged.connect(self.req_delim)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(ChangeDel)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ChangeDel)
        self.buttonBox.accepted.connect(self.delim_accept)
        self.buttonBox.rejected.connect(ChangeDel.reject)
        QtCore.QMetaObject.connectSlotsByName(ChangeDel)

    def retranslateUi(self, ChangeDel):
        _translate = QtCore.QCoreApplication.translate
        ChangeDel.setWindowTitle(_translate("ChangeDel", "Change Delimeter"))
        self.groupBox.setTitle(_translate("ChangeDel", "Set Parameters :"))
        self.label.setText(_translate("ChangeDel", "Current Delimeter:"))
        self.label_2.setText(_translate("ChangeDel", "Required Delimeter:"))

    def cur_delim(self, value):
        global cur_delim
        cur_delim = str(value)


    def req_delim(self,value):
        global req_delim
        req_delim = str(value)


    def delim_accept(self):
        if fileName == "":
            global msg_text
            global msg_info
            global msg_icon
            msg_icon = QMessageBox.Warning
            msg_text = "No .csv file opened"
            msg_info = "Open .csv file"
            Ui_split.msg_window(self)

        else:
            if cur_delim != "" and req_delim != "" :
                if len(cur_delim) <= 2 and len(req_delim) <= 2:
                    with open(fileName) as infile:
                        with open(str(folderpath) + "/" + filenoext +str(req_delim)+ "_delimeter.csv", 'w+') as outfile:
                            for line in infile:
                                fields = line.split(cur_delim)
                                outfile.write(req_delim.join(fields))

                    msg_icon = QMessageBox.Information
                    msg_text = "Completed"
                    msg_info = "File saved successfully"
                    Ui_split.msg_window(self)
                else:
                    msg_icon = QMessageBox.Information
                    msg_text = "Check delimeters"
                    msg_info = "Enter valid Delimeter"
                    Ui_split.msg_window(self)
            else:
                msg_icon = QMessageBox.Information
                msg_text = "Check delimeters"
                msg_info = "Enter valid Delimeter"
                Ui_split.msg_window(self)

##----------------End of deimeter function and start of arrange function-------------

class Ui_arrange_dialog(object):
    def setupUi(self, arrange_dialog):
        arrange_dialog.setObjectName("arrange_dialog")
        arrange_dialog.setWindowModality(QtCore.Qt.NonModal)
        arrange_dialog.resize(258, 255)
        arrange_dialog.setWindowFlags(
            QtCore.Qt.Window |
            QtCore.Qt.CustomizeWindowHint |
            QtCore.Qt.WindowTitleHint |
            QtCore.Qt.WindowCloseButtonHint
        )
        arrange_dialog.setWindowIcon(QtGui.QIcon('Icon.png'))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(arrange_dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(arrange_dialog)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(arrange_dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.inlist = QtWidgets.QListWidget(arrange_dialog)
        self.inlist.setAcceptDrops(True)
        self.inlist.setTabKeyNavigation(True)
        self.inlist.setDragEnabled(False)
        self.inlist.setDragDropOverwriteMode(True)
        self.inlist.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.inlist.setAlternatingRowColors(False)
        self.inlist.setObjectName("inlist")
        self.horizontalLayout.addWidget(self.inlist)
        self.outlist = QtWidgets.QListWidget(arrange_dialog)
        self.outlist.setAcceptDrops(True)
        self.outlist.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.outlist.setTabKeyNavigation(True)
        self.outlist.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.outlist.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.outlist.setAlternatingRowColors(False)
        self.outlist.setObjectName("outlist")

        if fileName != "":
            with open(fileName) as fin:
                csvin = csv.DictReader(fin)
                fieldnames = csvin.fieldnames
                self.inlist.addItems(fieldnames)
                self.outlist.addItems(fieldnames)

        else:
            global msg_text
            global msg_info
            global msg_icon
            msg_icon = QMessageBox.Warning
            msg_text = "No .csv file opened"
            msg_info = "Open .csv file"
            Ui_split.msg_window(self)


        self.horizontalLayout.addWidget(self.outlist)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.delete_button = QtWidgets.QToolButton(arrange_dialog)
        self.delete_button.setObjectName("delete_button")
        self.delete_button.clicked.connect(self.delme)
        self.verticalLayout.addWidget(self.delete_button)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(arrange_dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.buttonBox.raise_()
        self.delete_button.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.inlist.raise_()
        self.outlist.raise_()
        self.outlist.raise_()
        self.retranslateUi(arrange_dialog)
        self.buttonBox.accepted.connect(self.arrange_accept)
        self.buttonBox.rejected.connect(arrange_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(arrange_dialog)


    def retranslateUi(self, arrange_dialog):
        _translate = QtCore.QCoreApplication.translate
        arrange_dialog.setWindowTitle(_translate("arrange_dialog", "Arrange Columns"))
        self.label.setText(_translate("arrange_dialog", "Input Columns :"))
        self.label_2.setText(_translate("arrange_dialog", "Arrange :"))
        self.delete_button.setText(_translate("arrange_dialog", "del"))



    def delme(self):
        listItems = self.outlist.selectedItems()
#        if not listItems: return
        for item in listItems:
            self.outlist.takeItem(self.outlist.row(item))




    def arrange_accept(self):
        global out_list
        out_list =[]
        count = self.inlist.count()
        out_count = self.outlist.count()
        if count == 0 or out_count == 0:
            global msg_text
            global msg_info
            global msg_icon
            msg_icon = QMessageBox.Warning
            msg_text = "No .csv file opened"
            msg_info = "Open .csv file"
            Ui_split.msg_window(self)


        else:
            for i in range(count):
                item = self.inlist.item(i)
                item = item.text()
            for x in range(out_count):
                oitem = self.outlist.item(x)
                oitem = oitem.text()
                out_list.append(oitem)
            
            
            with open(fileName, 'r') as infile, open(str(folderpath) + "/" + str(filenoext)+"_Arranged"+ ".csv",'w+',newline='') as outfile:
                # output dict needs a list for new column ordering
                writer = csv.DictWriter(outfile, fieldnames=out_list,extrasaction ='ignore')
                # reorder the header first
                writer.writeheader()
                for row in csv.DictReader(infile):
                    # writes the reordered rows to the new file
                    writer.writerow(row)

                msg_icon = QMessageBox.Information
                msg_text = "Completed"
                msg_info = "File saved successfully"
                Ui_split.msg_window(self)


    ##-------------------------------------------------

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CSV_Tools = QtWidgets.QMainWindow()
    ui = Ui_CSV_Tools()
    ui.setupUi(CSV_Tools)
    CSV_Tools.show()
    sys.exit(app.exec_())

