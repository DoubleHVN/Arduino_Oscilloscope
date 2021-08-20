from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget, plot
from pyqtgraph.metaarray.MetaArray import axis

from views.serial import update_serialConnected, update_serialDisconnected
from views.qt_gen.GUI_v2 import Ui_GUI
from views.tream import update_startStreaming, update_stopStreaming
from views.reset import update_Reset
from views.record import Record


import serial
from controller import Controllers



class Views(object):
    def __init__(self, app, widget):
        self.widget = widget
        self.app = app
        self.ui = Ui_GUI()
        self.ui.setupUi(self.widget)
        self.attachHandler()
        

    def attachHandler(self):
        self.ui.Connect.clicked.connect(getConnectHandler(self, self.app))
        self.ui.Start.clicked.connect(getStartHandler(self, self.app))
        self.ui.Reset.clicked.connect(getResetHanlder(self, self.app))
        self.ui.Record.clicked.connect(getRecordHandler(self, self.app))
        self.ui.timer_getdata.timeout.connect(lambda:Controllers(self, self.app))


def getConnectHandler(view, app):
    def handleConnect ():
        app.state.com = view.ui.Com.currentText()
        
        app.state.baudrate = int(view.ui.Baudrates.currentText())
        
        bytesize = view.ui.DataSize.currentText()
        if bytesize == "7":
            app.state.byteSize = serial.SEVENBITS
        elif bytesize == "8":
            app.state.byteSize = serial.EIGHTBITS

        parity = view.ui.Parity.currentText()
        if parity == "none":
            app.state.parity = serial.PARITY_NONE
        elif parity == "even":
            app.state.parity = serial.PARITY_EVEN
        elif parity == "odd":
            app.state.parity = serial.PARITY_ODD
        elif parity == "mark":
            app.state.parity = serial.PARITY_MARK
        
        errStr, err = app.connectSerial()
        if err == True:
            update_serialConnected(view.ui)
        elif err == False:
            update_serialDisconnected(view.ui)
            app.state.serialConn.close()
        else:
            view.ui.Monitor.append(errStr)
    return handleConnect

def getStartHandler(view, app):
    def handleStart():
        _ , method = app.startStream()
        if method == True:
            update_startStreaming(view.ui)
            app.state.serialConn.reset_input_buffer()
        elif method == False:
            update_stopStreaming(view.ui)
    return handleStart

def getResetHanlder(view, app):
    def handleReset():
        update_Reset(view.ui, app.state)
    return handleReset

def getRecordHandler(view, app):
    def handleRecord():
        Record(view.ui ,app.state)
    return handleRecord


