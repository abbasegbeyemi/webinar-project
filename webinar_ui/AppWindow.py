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
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_video_feed = QtWidgets.QLabel(self.centralwidget)
        self.label_video_feed.setObjectName("label_video_feed")
        self.horizontalLayout.addWidget(self.label_video_feed)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(300, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listwidget_signed_in = QtWidgets.QListWidget(self.groupBox)
        self.listwidget_signed_in.setObjectName("listwidget_signed_in")
        self.verticalLayout_2.addWidget(self.listwidget_signed_in)
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.layout_buttons = QtWidgets.QHBoxLayout()
        self.layout_buttons.setObjectName("layout_buttons")
        self.button_signin = QtWidgets.QPushButton(self.centralwidget)
        self.button_signin.setObjectName("button_signin")
        self.layout_buttons.addWidget(self.button_signin)
        self.button_signout = QtWidgets.QPushButton(self.centralwidget)
        self.button_signout.setObjectName("button_signout")
        self.layout_buttons.addWidget(self.button_signout)
        self.verticalLayout.addLayout(self.layout_buttons)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_video_feed.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Loading video feed...</p></body></html>"))
        self.groupBox.setTitle(_translate("MainWindow", "Employees Present"))
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
