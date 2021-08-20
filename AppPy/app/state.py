import serial

class AppState(object) :
    def __init__(self):
        self.com = ""
        self.baudrate = []
        self.byteSize = []
        self.parity = []
        self.data = {}
        self.bytetoread = 0
        self.serialConn = serial.Serial()
        
        self.isConnected = False
        self.isStart = False

        self.a = 0
        self.time = []
        self.StoragePath = "D:\Workspace\Vulcan\App\AppPy\storage"

        self.color = ['g','r','b','y','o','b']