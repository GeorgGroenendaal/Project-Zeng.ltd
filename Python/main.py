import time
from PyQt5.QtCore import *
import serial.tools.list_ports

# Main initializer
class Main(QThread):

    addtab = pyqtSignal(int, str)
    deltab = pyqtSignal(int)

    def __init__(self):
        self.devices = {}
        QThread.__init__(self)

    def run(self):
        while 1:
            ports = serial.tools.list_ports.comports();
            serial_number = []
            for port in ports:
                if port.description[0:7] == "Arduino":
                    serial_number.append(port.serial_number)
                    if port.serial_number not in self.devices:
                        name = "Arduino " + port.serial_number[-4:]
                        self.addtab.emit(port.serial_number, name)
                        self.devices[port.serial_number] = {name}
            for key in list(self.devices.keys()):
                if key not in serial_number:
                    self.deltab.emit(key)
                    del self.devices[key]
            QThread.sleep(2)

    def createInterface(self):
        print(self.addtab.emit('hi'))
        # return {'tab': tab, 'tabindex': index}
        # Create communication interface for the arduino's
