from PyQt5 import QtCore, QtGui, QtWidgets
from API import *
from notis import Ui_MainNotificationWindow
from opportunities import Ui_MainOpportunitiesWindow
from events import Ui_MainEventsWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 690)
        MainWindow.setMinimumSize(QtCore.QSize(850, 690))
        MainWindow.setMaximumSize(QtCore.QSize(850, 16777215))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QWidget(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, -20, 851, 771))
        self.background.setStyleSheet("background-color:#be808e;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.813, y2:0.653409, stop:0#00264d, stop:1#be808e);")
        self.background.setObjectName("background")
        self.notifimg = QtWidgets.QLabel(self.background)
        self.notifimg.setGeometry(QtCore.QRect(88, 361, 141, 141))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(63)
        sizePolicy.setHeightForWidth(self.notifimg.sizePolicy().hasHeightForWidth())
        self.notifimg.setSizePolicy(sizePolicy)
        self.notifimg.setMinimumSize(QtCore.QSize(0, 0))
        self.notifimg.setStyleSheet("background-color:none;")
        self.notifimg.setText("")
        self.notifimg.setPixmap(QtGui.QPixmap("src/aq.png"))
        self.notifimg.setScaledContents(True)
        self.notifimg.setObjectName("notifimg")
        self.notifbox = QtWidgets.QLabel(self.background)
        self.notifbox.setGeometry(QtCore.QRect(79, 356, 161, 241))
        self.notifbox.setStyleSheet("background-color:#c5bacc;\n"
" border-radius: 10px ;")
        self.notifbox.setText("")
        self.notifbox.setObjectName("notifbox")
        self.notifpushButton = QtWidgets.QPushButton(self.background)
        self.notifpushButton.setGeometry(QtCore.QRect(89, 555, 131, 31))
        self.notifpushButton.setMouseTracking(False)
        self.notifpushButton.clicked.connect(self.notificationWindow)
        self.notifpushButton.setStyleSheet("background-color:#01264e;\n"
"border-radius:10px;\n"
"color:white;\n"
"font: 75 10pt \"Tahoma\";\n"
"letter-spacing: 2 px;")
        self.notifpushButton.setCheckable(False)
        self.notifpushButton.setObjectName("notifpushButton")
        self.opporbox = QtWidgets.QLabel(self.background)
        self.opporbox.setGeometry(QtCore.QRect(244, 357, 161, 241))
        self.opporbox.setStyleSheet("background-color:#c5bacc;\n"
" border-radius: 10px ;")
        self.opporbox.setText("")
        self.opporbox.setObjectName("opporbox")
        self.eventbox = QtWidgets.QLabel(self.background)
        self.eventbox.setGeometry(QtCore.QRect(409, 358, 161, 241))
        self.eventbox.setStyleSheet("background-color:#c5bacc;\n"
" border-radius: 10px ;")
        self.eventbox.setText("")
        self.eventbox.setObjectName("eventbox")
        self.commandbox = QtWidgets.QLabel(self.background)
        self.commandbox.setStyleSheet("background-color:none;")
        self.commandbox.setGeometry(QtCore.QRect(380, 170, 100, 100))
        self.commandbox.setStyleSheet("background-color:#c5bacc;\n"
" border-radius: 10px ;")
        self.commandbox.setStyleSheet("background-color:none;")
        # self.commandbox.adjustSize()
        self.commandbox.setText("Welcome")
        self.commandbox.setObjectName("commandbox")
        self.perslbox = QtWidgets.QLabel(self.background)
        self.perslbox.setGeometry(QtCore.QRect(575, 357, 161, 241))
        self.perslbox.setStyleSheet("background-color:#c5bacc;\n"
" border-radius: 10px ;")
        self.perslbox.setText("")
        self.perslbox.setObjectName("perslbox")
        self.opporimg = QtWidgets.QLabel(self.background)
        self.opporimg.setGeometry(QtCore.QRect(255, 363, 141, 141))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(63)
        sizePolicy.setHeightForWidth(self.opporimg.sizePolicy().hasHeightForWidth())
        self.opporimg.setSizePolicy(sizePolicy)
        self.opporimg.setMinimumSize(QtCore.QSize(0, 0))
        self.opporimg.setStyleSheet("background-color:none;")
        self.opporimg.setText("")
        self.opporimg.setPixmap(QtGui.QPixmap("src/11.png"))
        self.opporimg.setScaledContents(True)
        self.opporimg.setObjectName("opporimg")
        self.opporpushButton = QtWidgets.QPushButton(self.background)
        self.opporpushButton.setGeometry(QtCore.QRect(259, 554, 131, 31))
        self.opporpushButton.setMouseTracking(False)
        self.opporpushButton.clicked.connect(self.opportunitiesWindow)
        self.opporpushButton.setStyleSheet("background-color:#01264e;\n"
"border-radius:10px;\n"
"color:white;\n"
"font: 75 10pt \"Tahoma\";\n"
"letter-spacing: 2 px;")
        self.opporpushButton.setCheckable(False)
        self.opporpushButton.setObjectName("opporpushButton")
        self.eventpushButton = QtWidgets.QPushButton(self.background)
        self.eventpushButton.setGeometry(QtCore.QRect(423, 556, 131, 31))
        self.eventpushButton.clicked.connect(self.eventsWindow)
        self.eventpushButton.setMouseTracking(False)
        self.eventpushButton.setStyleSheet("background-color:#01264e;\n"
"border-radius:10px;\n"
"color:white;\n"
"font: 75 10pt \"Tahoma\";\n"
"letter-spacing: 2 px;")
        self.eventpushButton.setCheckable(False)
        self.eventpushButton.setObjectName("eventpushButton")
        self.perslpushButton = QtWidgets.QPushButton(self.background)
        self.perslpushButton.setGeometry(QtCore.QRect(588, 553, 131, 31))
        self.perslpushButton.setMouseTracking(False)
        self.perslpushButton.setStyleSheet("background-color:#01264e;\n"
"border-radius:10px;\n"
"color:white;\n"
"font: 75 10pt \"Tahoma\";\n"
"letter-spacing: 2 px;")
        self.perslpushButton.setCheckable(False)
        self.perslpushButton.setObjectName("perslpushButton")
        self.eventimg = QtWidgets.QLabel(self.background)
        self.eventimg.setGeometry(QtCore.QRect(420, 360, 141, 151))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(63)
        sizePolicy.setHeightForWidth(self.eventimg.sizePolicy().hasHeightForWidth())
        self.eventimg.setSizePolicy(sizePolicy)
        self.eventimg.setMinimumSize(QtCore.QSize(0, 0))
        self.eventimg.setStyleSheet("background-color:none;")
        self.eventimg.setText("")
        self.eventimg.setPixmap(QtGui.QPixmap("src/event.png"))
        self.eventimg.setScaledContents(True)
        self.eventimg.setObjectName("eventimg")
        self.maintext = QtWidgets.QLabel(self.background)
        self.maintext.setGeometry(QtCore.QRect(140, 240, 541, 71))
        self.maintext.setStyleSheet("font: 24pt \"Tahoma\";\n"
"border-radius:10px;\n"
"color:#093545;\n"
"background-color:white;")
        self.maintext.setObjectName("maintext")
        self.pushButton_Start = QtWidgets.QPushButton(self.background)
        self.pushButton_Start.setGeometry(QtCore.QRect(89, 630, 75, 23))
        self.pushButton_Start.setStyleSheet("background-color:#01264e;\n"
"border-radius:10px;\n"
"color:white;\n"
"font: 75 10pt \"Tahoma\";\n"
"letter-spacing: 2 px;")
        self.pushButton_Start.clicked.connect(self.startProcess)
        self.pushButton_Start.setObjectName("Start_Button")
        self.pushButton_5 = QtWidgets.QPushButton(self.background)
        self.pushButton_5.setGeometry(QtCore.QRect(660, 630, 75, 23))
        # ! Connecting to the Push Button
        # self.pushButton_5.clicked.connect(self.logging)
        self.pushButton_5.setStyleSheet("background-color:#01264e;\n"
"border-radius:10px;\n"
"color:white;\n"
"font: 75 10pt \"Tahoma\";\n"
"letter-spacing: 2 px;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.uetlogo = QtWidgets.QLabel(self.background)
        self.uetlogo.setGeometry(QtCore.QRect(90, 50, 111, 111))
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
        self.cslogo = QtWidgets.QLabel(self.background)
        self.cslogo.setGeometry(QtCore.QRect(615, 50, 111, 111))
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
        self.perslimg = QtWidgets.QLabel(self.background)
        self.perslimg.setGeometry(QtCore.QRect(580, 360, 151, 141))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(63)
        sizePolicy.setHeightForWidth(self.perslimg.sizePolicy().hasHeightForWidth())
        self.perslimg.setSizePolicy(sizePolicy)
        self.perslimg.setMinimumSize(QtCore.QSize(0, 0))
        self.perslimg.setStyleSheet("background-color:none;")
        self.perslimg.setText("")
        self.perslimg.setPixmap(QtGui.QPixmap("src/personal-information.png"))
        self.perslimg.setScaledContents(True)
        self.perslimg.setObjectName("perslimg")
        self.notifbox.raise_()
        self.notifimg.raise_()
        self.notifpushButton.raise_()
        self.opporbox.raise_()
        self.eventbox.raise_()
        self.perslbox.raise_()
        self.opporimg.raise_()
        self.opporpushButton.raise_()
        self.eventpushButton.raise_()
        self.perslpushButton.raise_()
        self.eventimg.raise_()
        self.maintext.raise_()
        self.pushButton_5.raise_()
        self.uetlogo.raise_()
        self.cslogo.raise_()
        self.perslimg.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

#  !  function to execute on push button click
#     def logging(self):
#             print('Clicking the Push Button')

 # * New Windows Opening functions

    def notificationWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainNotificationWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def opportunitiesWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainOpportunitiesWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def eventsWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainEventsWindow()
        self.ui.setupUi(self.window)
        self.window.show()

 # * Label text updating function

    def showOutput(self, msg):
        self.commandbox.adjustSize()
        self.commandbox.setText(msg)
        self.commandbox.adjustSize()

    def startProcess(self):
        self.commandbox.clear()
        self.commandbox.setText('')
        self.showOutput("Go ahead! I'm listening")
        Boot()
        # print('Voice Assistant Activated')
        print("Go ahead! I'm listening ...")
        say("Go ahead! I'm listening ...")
        text = speak()
        # text = "scan"
        print(text)
        self.showOutput(text)
        Command(text, self)
            

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Voice Controlled Departmental NoticeBoard"))
        self.notifpushButton.setText(_translate("MainWindow", "NOTIFICATION"))
        self.opporpushButton.setText(_translate("MainWindow", "OPPORTUNITIES"))
        self.eventpushButton.setText(_translate("MainWindow", "EVENTS"))
        self.perslpushButton.setText(_translate("MainWindow", "Personal Information"))
        self.maintext.setText(_translate("MainWindow", "    SMART NOTIFICATION BOARD"))
        self.pushButton_5.setText(_translate("MainWindow", "Logout"))
        self.pushButton_Start.setText(_translate("MainWindow", "Start"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())