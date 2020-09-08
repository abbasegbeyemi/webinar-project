# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'webinar_ui/appwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget#centralwidget {\n"
"background-color: white;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: rgb(252, 205, 97);\n"
"color: black;\n"
"border: 2px solid rgb(252, 205, 97);\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: white;\n"
"background-color: rgb(255, 153, 131);\n"
"border: 2px solid rgb(255, 153, 131);\n"
"}\n"
"\n"
"QLabel#label_video_feed{\n"
"border: 2px solid rgb(252, 205, 97);\n"
"}\n"
"\n"
"QLabel#employees_label{\n"
"background-color: rgb(252, 205, 97);\n"
"color: black;\n"
"}\n"
"\n"
"QListWidget#listwidget_signed_in{\n"
"border: 2px solid rgb(252, 205, 97);\n"
"font-size: 20pt;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QListWidget::item\n"
"{\n"
"color:black;\n"
"border-bottom: 2px solid rgb(252, 205, 97);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_video_feed = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_video_feed.sizePolicy().hasHeightForWidth())
        self.label_video_feed.setSizePolicy(sizePolicy)
        self.label_video_feed.setObjectName("label_video_feed")
        self.horizontalLayout.addWidget(self.label_video_feed)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.employees_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.employees_label.setFont(font)
        self.employees_label.setObjectName("employees_label")
        self.verticalLayout.addWidget(self.employees_label)
        self.listwidget_signed_in = QtWidgets.QListWidget(self.centralwidget)
        self.listwidget_signed_in.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.listwidget_signed_in.setFont(font)
        self.listwidget_signed_in.setAutoFillBackground(False)
        self.listwidget_signed_in.setObjectName("listwidget_signed_in")
        self.verticalLayout.addWidget(self.listwidget_signed_in)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.layout_buttons = QtWidgets.QHBoxLayout()
        self.layout_buttons.setObjectName("layout_buttons")
        self.button_signin = QtWidgets.QPushButton(self.centralwidget)
        self.button_signin.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(34)
        self.button_signin.setFont(font)
        self.button_signin.setObjectName("button_signin")
        self.layout_buttons.addWidget(self.button_signin)
        self.button_signout = QtWidgets.QPushButton(self.centralwidget)
        self.button_signout.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(34)
        self.button_signout.setFont(font)
        self.button_signout.setObjectName("button_signout")
        self.layout_buttons.addWidget(self.button_signout)
        self.verticalLayout_2.addLayout(self.layout_buttons)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Employee App"))
        self.label_video_feed.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Loading video feed...</p></body></html>"))
        self.employees_label.setText(_translate("MainWindow", "Employees Present"))
        self.button_signin.setText(_translate("MainWindow", "Sign In"))
        self.button_signout.setText(_translate("MainWindow", "Sign Out"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
