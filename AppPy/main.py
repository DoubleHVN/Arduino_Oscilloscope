from app import App
import sys
from PyQt5 import QtWidgets

if __name__ == "__main__":
    qt = QtWidgets.QApplication(sys.argv)
    app = App()
    sys.exit(qt.exec_())