# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AppLayout\Layout2\form.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GUI(object):
    def setupUi(self, GUI):
        GUI.setObjectName("GUI")
        GUI.resize(1205, 756)
        self.Controller = QtWidgets.QGroupBox(GUI)
        self.Controller.setGeometry(QtCore.QRect(10, 10, 211, 731))
        self.Controller.setObjectName("Controller")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Controller)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Serial = QtWidgets.QGroupBox(self.Controller)
        self.Serial.setObjectName("Serial")
        self.formLayout_2 = QtWidgets.QFormLayout(self.Serial)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.Serial)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.Baudrates = QtWidgets.QComboBox(self.Serial)
        self.Baudrates.setObjectName("Baudrates")
        self.Baudrates.addItem("")
        self.Baudrates.setItemText(0, "")
        self.Baudrates.addItem("")
        self.Baudrates.addItem("")
        self.Baudrates.addItem("")
        self.Baudrates.addItem("")
        self.Baudrates.addItem("")
        self.Baudrates.addItem("")
        self.Baudrates.addItem("")
        self.Baudrates.addItem("")
        self.Baudrates.addItem("")
        self.Baudrates.addItem("")
        self.Baudrates.addItem("")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Baudrates)
        self.Com = QtWidgets.QComboBox(self.Serial)
        self.Com.setObjectName("Com")
        self.Com.addItem("")
        self.Com.setItemText(0, "")
        self.Com.addItem("")
        self.Com.addItem("")
        self.Com.addItem("")
        self.Com.addItem("")
        self.Com.addItem("")
        self.Com.addItem("")
        self.Com.addItem("")
        self.Com.addItem("")
        self.Com.addItem("")
        self.Com.addItem("")
        self.Com.addItem("")
        self.Com.addItem("")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Com)
        self.DataSize = QtWidgets.QComboBox(self.Serial)
        self.DataSize.setObjectName("DataSize")
        self.DataSize.addItem("")
        self.DataSize.setItemText(0, "")
        self.DataSize.addItem("")
        self.DataSize.addItem("")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.DataSize)
        self.Parity = QtWidgets.QComboBox(self.Serial)
        self.Parity.setObjectName("Parity")
        self.Parity.addItem("")
        self.Parity.addItem("")
        self.Parity.addItem("")
        self.Parity.addItem("")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.Parity)
        self.label_2 = QtWidgets.QLabel(self.Serial)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.Serial)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.Serial)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.Connect = QtWidgets.QPushButton(self.Serial)
        self.Connect.setObjectName("Connect")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.Connect)
        self.verticalLayout.addWidget(self.Serial)
        self.tabWidget = QtWidgets.QTabWidget(self.Controller)
        self.tabWidget.setObjectName("tabWidget")
        self.RealTime = QtWidgets.QWidget()
        self.RealTime.setObjectName("RealTime")
        self.tabWidget.addTab(self.RealTime, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.formLayout_3 = QtWidgets.QFormLayout(self.tab_2)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setObjectName("label_10")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.textEdit = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit.setObjectName("textEdit")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textEdit)
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setObjectName("label_11")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setObjectName("label_12")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_3.setObjectName("textEdit_3")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEdit_3)
        self.textEdit_4 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_4.setObjectName("textEdit_4")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.textEdit_4)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.Stream = QtWidgets.QGroupBox(self.Controller)
        self.Stream.setObjectName("Stream")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Stream)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Start = QtWidgets.QPushButton(self.Stream)
        self.Start.setObjectName("Start")
        self.horizontalLayout.addWidget(self.Start)
        self.Reset = QtWidgets.QPushButton(self.Stream)
        self.Reset.setObjectName("Reset")
        self.horizontalLayout.addWidget(self.Reset)
        self.verticalLayout.addWidget(self.Stream)
        self.Saver = QtWidgets.QGroupBox(self.Controller)
        self.Saver.setObjectName("Saver")
        self.formLayout = QtWidgets.QFormLayout(self.Saver)
        self.formLayout.setObjectName("formLayout")
        self.label_7 = QtWidgets.QLabel(self.Saver)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.Model = QtWidgets.QComboBox(self.Saver)
        self.Model.setObjectName("Model")
        self.Model.addItem("")
        self.Model.setItemText(0, "")
        self.Model.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Model)
        self.label_5 = QtWidgets.QLabel(self.Saver)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.Type = QtWidgets.QComboBox(self.Saver)
        self.Type.setObjectName("Type")
        self.Type.addItem("")
        self.Type.setItemText(0, "")
        self.Type.addItem("")
        self.Type.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Type)
        self.label_6 = QtWidgets.QLabel(self.Saver)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.Name = QtWidgets.QTextEdit(self.Saver)
        self.Name.setObjectName("Name")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Name)
        self.Record = QtWidgets.QPushButton(self.Saver)
        self.Record.setObjectName("Record")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.Record)
        self.checkBox_3 = QtWidgets.QCheckBox(self.Saver)
        self.checkBox_3.setObjectName("checkBox_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.checkBox_3)
        self.verticalLayout.addWidget(self.Saver)
        self.Send = QtWidgets.QGroupBox(GUI)
        self.Send.setGeometry(QtCore.QRect(890, 10, 291, 201))
        self.Send.setObjectName("Send")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Send)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.Send)
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout_2.addWidget(self.textEdit_2)
        self.Send_2 = QtWidgets.QPushButton(self.Send)
        self.Send_2.setObjectName("Send_2")
        self.verticalLayout_2.addWidget(self.Send_2)
        self.Hex = QtWidgets.QCheckBox(self.Send)
        self.Hex.setObjectName("Hex")
        self.verticalLayout_2.addWidget(self.Hex)
        self.SeriaPlotter = QtWidgets.QGroupBox(GUI)
        self.SeriaPlotter.setGeometry(QtCore.QRect(230, 220, 641, 521))
        self.SeriaPlotter.setObjectName("SeriaPlotter")
        self.Plotter = PlotWidget(self.SeriaPlotter)
        self.Plotter.setGeometry(QtCore.QRect(0, 20, 641, 501))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Plotter.sizePolicy().hasHeightForWidth())
        self.Plotter.setSizePolicy(sizePolicy)
        self.Plotter.setObjectName("Plotter")
        self.SerialMonitor = QtWidgets.QGroupBox(GUI)
        self.SerialMonitor.setGeometry(QtCore.QRect(230, 10, 641, 201))
        self.SerialMonitor.setObjectName("SerialMonitor")
        self.Monitor = QtWidgets.QTextBrowser(self.SerialMonitor)
        self.Monitor.setGeometry(QtCore.QRect(0, 20, 641, 141))
        self.Monitor.setObjectName("Monitor")
        self.AutoScroll = QtWidgets.QCheckBox(self.SerialMonitor)
        self.AutoScroll.setGeometry(QtCore.QRect(410, 170, 91, 22))
        self.AutoScroll.setObjectName("AutoScroll")
        self.label_8 = QtWidgets.QLabel(self.SerialMonitor)
        self.label_8.setGeometry(QtCore.QRect(10, 170, 55, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.SerialMonitor)
        self.label_9.setGeometry(QtCore.QRect(170, 170, 55, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.Max = QtWidgets.QTextBrowser(self.SerialMonitor)
        self.Max.setGeometry(QtCore.QRect(50, 170, 101, 21))
        self.Max.setObjectName("Max")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.SerialMonitor)
        self.textBrowser_2.setGeometry(QtCore.QRect(210, 170, 101, 21))
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.retranslateUi(GUI)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(GUI)

    def retranslateUi(self, GUI):
        _translate = QtCore.QCoreApplication.translate
        GUI.setWindowTitle(_translate("GUI", "GUI"))
        self.Controller.setTitle(_translate("GUI", "Controller"))
        self.Serial.setTitle(_translate("GUI", "Serial"))
        self.label.setText(_translate("GUI", "Baudrate:"))
        self.Baudrates.setItemText(1, _translate("GUI", "600"))
        self.Baudrates.setItemText(2, _translate("GUI", "1200"))
        self.Baudrates.setItemText(3, _translate("GUI", "2400"))
        self.Baudrates.setItemText(4, _translate("GUI", "4800"))
        self.Baudrates.setItemText(5, _translate("GUI", "9600"))
        self.Baudrates.setItemText(6, _translate("GUI", "14400"))
        self.Baudrates.setItemText(7, _translate("GUI", "19200"))
        self.Baudrates.setItemText(8, _translate("GUI", "38400"))
        self.Baudrates.setItemText(9, _translate("GUI", "56000"))
        self.Baudrates.setItemText(10, _translate("GUI", "57600"))
        self.Baudrates.setItemText(11, _translate("GUI", "115200"))
        self.Com.setItemText(1, _translate("GUI", "Com1"))
        self.Com.setItemText(2, _translate("GUI", "Com2"))
        self.Com.setItemText(3, _translate("GUI", "Com3"))
        self.Com.setItemText(4, _translate("GUI", "Com4"))
        self.Com.setItemText(5, _translate("GUI", "Com5"))
        self.Com.setItemText(6, _translate("GUI", "Com6"))
        self.Com.setItemText(7, _translate("GUI", "Com7"))
        self.Com.setItemText(8, _translate("GUI", "Com8"))
        self.Com.setItemText(9, _translate("GUI", "Com9"))
        self.Com.setItemText(10, _translate("GUI", "Com10"))
        self.Com.setItemText(11, _translate("GUI", "Com11"))
        self.Com.setItemText(12, _translate("GUI", "Com12"))
        self.DataSize.setItemText(1, _translate("GUI", "7"))
        self.DataSize.setItemText(2, _translate("GUI", "8"))
        self.Parity.setItemText(0, _translate("GUI", "none"))
        self.Parity.setItemText(1, _translate("GUI", "odd"))
        self.Parity.setItemText(2, _translate("GUI", "even"))
        self.Parity.setItemText(3, _translate("GUI", "mark"))
        self.label_2.setText(_translate("GUI", "COM"))
        self.label_3.setText(_translate("GUI", "Data Size:"))
        self.label_4.setText(_translate("GUI", "Parity:"))
        self.Connect.setText(_translate("GUI", "Connect"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.RealTime), _translate("GUI", "Tab 1"))
        self.label_10.setText(_translate("GUI", "Sample rate"))
        self.label_11.setText(_translate("GUI", "Time"))
        self.label_12.setText(_translate("GUI", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("GUI", "Tab 2"))
        self.Stream.setTitle(_translate("GUI", "Stream"))
        self.Start.setText(_translate("GUI", "Start"))
        self.Reset.setText(_translate("GUI", "Reset"))
        self.Saver.setTitle(_translate("GUI", "Saver"))
        self.label_7.setText(_translate("GUI", "Model:"))
        self.Model.setItemText(1, _translate("GUI", "Mark9.7"))
        self.label_5.setText(_translate("GUI", "Type:"))
        self.Type.setItemText(1, _translate("GUI", "csv"))
        self.Type.setItemText(2, _translate("GUI", "xlsx"))
        self.label_6.setText(_translate("GUI", "Name"))
        self.Record.setText(_translate("GUI", "Record"))
        self.checkBox_3.setText(_translate("GUI", "CheckBox"))
        self.Send.setTitle(_translate("GUI", "Send"))
        self.Send_2.setText(_translate("GUI", "Send"))
        self.Hex.setText(_translate("GUI", "Hex"))
        self.SeriaPlotter.setTitle(_translate("GUI", "Serial Plotter"))
        self.SerialMonitor.setTitle(_translate("GUI", "Serrial Monitor"))
        self.AutoScroll.setText(_translate("GUI", "Auto Scroll"))
        self.label_8.setText(_translate("GUI", "Max:"))
        self.label_9.setText(_translate("GUI", "Min:"))

from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GUI = QtWidgets.QWidget()
    ui = Ui_GUI()
    ui.setupUi(GUI)
    GUI.show()
    sys.exit(app.exec_())
