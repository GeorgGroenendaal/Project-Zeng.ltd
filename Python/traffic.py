import serial
import threading
from PyQt5.QtCore import *
import time
import struct
import codecs




class Arduino(QObject):

    successmsg = pyqtSignal(str)
    failedsmsg = pyqtSignal(str)

    tempmsg = pyqtSignal(int)
    lightmsg = pyqtSignal(int)
    distmsg = pyqtSignal(int)

    def __init__(self, port):
        self.ser = serial.Serial(port=port,
                                 baudrate=9600)
        self.cmd = []
        self.instr = None
        self.codes = {
            '41': self.return_success,
            '42': self.return_current_temp,
            '43': self.return_current_distance,
            '44': self.return_current_light,
            '45': self.return_success,
            '46': self.return_success,
            '47': self.return_success,
            '48': self.return_success,
            '49': self.return_success,
            # '4A': self.return_current_temp_treshold,
            # '4B': self.return_current_light_treshold,
            '4C': self.return_success,
            '4D': self.return_success,
            '4E': self.return_success
        }
        QObject.__init__(self)
        time.sleep(2)

        QTimer.singleShot(0,self.executor)
        self.timer = QTimer()
        self.timer.timeout.connect(self.executor)
        self.timer.start(10000)

    def executor(self):
        self.get_current_temp()
        self.get_current_light()
        self.get_current_distance()

    # Send hex instruction to ard
    def send_instruction(self, instruction):
        try:
            time.sleep(0.1)
            self.instr = instruction
            cmd = '02' + self.instr + '03'
            self.ser.write(bytes.fromhex(cmd))
            self.stop = False
            self.listen()
        except:
            pass

    def convert_float(self, bycmd):
        print(bycmd)
        newdata = bycmd[2:-1]
        print(newdata)
        int_val = struct.unpack_from('<f', newdata, 0)[0]
        return int_val

    # Decodes incoming instructions
    def decode(self):
        bycmd = b''.join(self.cmd)
        if bytes.fromhex('30') == self.cmd[1]:
            self.return_success()
        elif bytes.fromhex('31') == self.cmd[1]:
            self.return_failed()
        else:
            val = self.convert_float(bycmd)
            self.codes[self.instr](val)


    def floatify(self, string):
        strct = struct.pack('<f', int(string))
        return codecs.encode(strct, 'hex').decode()

    # Listens to incoming serial connection
    def listen(self):
        while not self.stop:
            char = self.ser.read(1)
            self.cmd.append(char)
            if bytes.fromhex('03') == char:
                self.cmd.append(char)
                self.decode()
                self.cmd = []
                self.stop = True

    def return_success(self):
        self.successmsg.emit("Success")

    def return_failed(self):
        self.failedmsg.emit("Failed")

    def return_current_temp(self, temp):
        self.tempmsg.emit(temp)

    def return_current_light(self, light):
        self.lightmsg.emit(light)

    def return_current_distance(self, distance):
        self.distmsg.emit(distance)

    # Asks Arduino if still connected
    def is_alive(self):
        self.send_instruction('41')

    # Requests current temperature from Arduino
    def get_current_temp(self):
        # threading.Timer(10.0, self.get_current_temp).start()
        self.send_instruction('42')

    # Requests current distance from Arduino
    def get_current_distance(self):
        self.send_instruction('43')

    # Requests currently measured light intensity
    def get_current_light(self):
        self.send_instruction('44')

    # Sends roll-down command to Arduino
    def manual_rolldown(self):
        self.send_instruction('45')

    # Sends roll-up command to Arduino
    def manual_rollup(self):
        self.send_instruction('46')

    # Sends command to roll to a given distance
    def roll_to_specific_distance(self):  # Nog een parameter aan meegeven
        self.send_instruction('47')

    # Sets/updates the roll-out temperature
    def update_temp_threshold(self, temp):  # Nog een parameter aan meegeven
        val = self.floatify(temp)
        self.send_instruction('48' + val)

    # Sets/updates the roll-out light intensity
    def update_light_threshold(self, light):  # Nog een parameter aan meegeven
        val = self.floatify(light)
        self.send_instruction('49' + val)

    # Requests the roll-out temperature
    def get_temp_threshold(self):
        self.send_instruction('4A')

    # Requests the roll-out light intensity
    def get_light_threshold(self):
        self.send_instruction('4B')

    # Updates the maximum roll-out distance
    def update_max_rollout(self, maxout):  # Nog een parameter aan meegeven
        val = self.floatify(maxout)
        self.send_instruction('4C' + val)

    # Updates the minimum roll-out distance
    def update_min_rollout(self, maxin):  # Nog een parameter aan meegeven
        val = self.floatify(maxin)
        self.send_instruction('4D' + val)

    # Resets a specified setting to default
    def reset_setting(self):
        self.send_instruction('4E')
