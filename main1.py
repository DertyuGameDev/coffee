# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.coffeeTable = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.coffeeTable.setGeometry(QtCore.QRect(10, 10, 780, 500))
        self.coffeeTable.setColumnCount(7)
        self.coffeeTable.setRowCount(0)
        self.coffeeTable.setHorizontalHeaderLabels(['ID', 'Название сорта', 'Степень обжарки', 'Молотый/В зернах', 'Описание вкуса', 'Цена', 'Объем упаковки'])
        self.coffeeTable.setObjectName("coffeeTable")
        self.loadButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.loadButton.setGeometry(QtCore.QRect(350, 530, 100, 30))
        self.loadButton.setObjectName("loadButton")
        self.addButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(200, 530, 100, 30))
        self.addButton.setObjectName("addButton")
        self.editButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.editButton.setGeometry(QtCore.QRect(500, 530, 100, 30))
        self.editButton.setObjectName("editButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loadButton.setText(_translate("MainWindow", "Загрузить"))
        self.addButton.setText(_translate("MainWindow", "Добавить"))
        self.editButton.setText(_translate("MainWindow", "Редактировать"))
