from PyQt5 import QtCore, QtGui, QtWidgets

lst=[("Proposal","December,23"),("Holidays","January,32"),("Ali","Naqi"), ("Tajammul", "Naeem")]
class Ui_MainEventsWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 690)
        MainWindow.move(265,10)
        MainWindow.setMinimumSize(QtCore.QSize(850, 690))
        MainWindow.setMaximumSize(QtCore.QSize(850, 690))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 850, 690))
        self.widget.setMinimumSize(QtCore.QSize(850, 690))
        self.widget.setMaximumSize(QtCore.QSize(850, 690))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.widget.setFont(font)
        self.widget.setStyleSheet("background-color:#be808e;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.813, y2:0.653409, stop:0#00264d, stop:1#be808e);")
        self.widget.setObjectName("widget")
        self.infotext = QtWidgets.QLabel(self.widget)
        self.infotext.setGeometry(QtCore.QRect(341, 220, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.infotext.setFont(font)
        self.infotext.setStyleSheet("font: 12pt \"Tahoma\";\n"
"border-radius:10px;\n"
"color:#093545;\n"
"background-color:white;\n"
"text-align: center;")
        self.infotext.setObjectName("infotext")
        self.uetlogo = QtWidgets.QLabel(self.widget)
        self.uetlogo.setGeometry(QtCore.QRect(50, 60, 120, 110))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(63)
        sizePolicy.setHeightForWidth(self.uetlogo.sizePolicy().hasHeightForWidth())
        self.uetlogo.setSizePolicy(sizePolicy)
        self.uetlogo.setMinimumSize(QtCore.QSize(0, 0))
        self.uetlogo.setStyleSheet("background-color:none;")
        self.uetlogo.setText("")
        self.uetlogo.setPixmap(QtGui.QPixmap("src/uetlogo.png"))
        self.uetlogo.setScaledContents(True)
        self.uetlogo.setObjectName("uetlogo")
        self.eventstable = QtWidgets.QTableWidget(self.widget)
        self.eventstable.setGeometry(QtCore.QRect(176, 303, 531, 25+len(lst)*30))
        self.eventstable.setStyleSheet("background-color:#c5bacc;\n"
" border-radius: 10px ;\n"
"self.tablewidget.setColumWidth:(0,233);")
        self.eventstable.setShowGrid(True)
        self.eventstable.setGridStyle(QtCore.Qt.SolidLine)
        self.eventstable.setRowCount(len(lst))
        self.eventstable.setColumnCount(2)
        self.eventstable.setObjectName("eventstable")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.eventstable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.eventstable.setHorizontalHeaderItem(1, item)
        self.eventstable.horizontalHeader().setVisible(True)
        self.eventstable.horizontalHeader().setDefaultSectionSize(258)
        self.eventstable.verticalHeader().setCascadingSectionResizes(False)
        self.eventstable.verticalHeader().setDefaultSectionSize(30)
        self.eventstable.verticalHeader().setSortIndicatorShown(False)
        self.eventstable.verticalHeader().setStretchLastSection(True)
        self.back_button = QtWidgets.QPushButton(self.widget)
        self.back_button.setGeometry(QtCore.QRect(631, 587, 75, 23))
        self.back_button.setMouseTracking(True)
        self.back_button.setStyleSheet("background-color:#093545;\n"
"border-radius:10px;\n"
"color:white;\n"
"font: 75 10pt \"Tahoma\";\n"
"letter-spacing: 2 px;")
        self.back_button.setObjectName("back_button")
        self.cslogo = QtWidgets.QLabel(self.widget)
        self.cslogo.setGeometry(QtCore.QRect(700, 60, 120, 110))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(63)
        sizePolicy.setHeightForWidth(self.cslogo.sizePolicy().hasHeightForWidth())
        self.cslogo.setSizePolicy(sizePolicy)
        self.cslogo.setMinimumSize(QtCore.QSize(0, 0))
        self.cslogo.setStyleSheet("background-color:none;")
        self.cslogo.setText("")
        self.cslogo.setPixmap(QtGui.QPixmap("src/cs.png"))
        self.cslogo.setScaledContents(True)
        self.cslogo.setObjectName("cslogo")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.infotext.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\"letter-spacing: 3px;\" \" font-size:18pt;\">EVENTS</span></p></body></html>"))
        self.eventstable.setSortingEnabled(True)
        item = self.eventstable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.eventstable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Notified Date"))
        self.back_button.setText(_translate("MainWindow", "Back"))
        self.eve_list()


    def eve_list(self):
        for ls, i in zip(lst, range(0, len(lst))):
            self.eventstable.setItem(i,0,QtWidgets.QTableWidgetItem(ls[0]))
            self.eventstable.setItem(i,1,QtWidgets.QTableWidgetItem(ls[1]))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainEventsWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())