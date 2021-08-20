from PyQt5 import QtWidgets
from views import Views
from app.state import AppState
import serial

class App(object):
    def __init__(self):
        self.widget = QtWidgets.QWidget()
        self.state = AppState()
        self.views = Views(self, self.widget)
        self.widget.show()


    def connectSerial(self):
        state = self.state
        try:
            if (state.isConnected == False):
                state.serialConn = serial.Serial(state.com, baudrate=state.baudrate,
                                            bytesize=state.byteSize, parity=state.parity)
                state.isConnected = True
                return ("connected", True)
            if (state.isConnected == True):
                state.isConnected = False
                state.serialConn.close()
                state.a = 0
                state.time = []
                state.data = {}
                return ("disconnect", False)
        except IOError:
            state.isConnected = False
            return ("failed to connect", IOError)
    
    def startStream(self):
        state = self.state
        if state.isStart == False:
            state.isStart = True

            return ("Start Streaming",True)
        elif state.isStart == True:
            state.isStart = False
            return ("Stop Streaming", False)