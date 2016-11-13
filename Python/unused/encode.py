import serial
import time
import threading
import struct


class Encoder:
    def __init__(self, command):
        self.command = command
        self.ser = serial.Serial(
            port='/dev/cu.usbmodem1411',
            baudrate=9600,
            timeout=0.1
        )

    # Send hex instruction to ard
    def send_instruction_ard(self):
        cmd = '02' + self.command + '03'
        self.ser.write(bytes.fromhex(cmd))


























        # while 1:
        #     string = bytes.fromhex(self.command)
        #     ser.write(string)
        #     time.sleep(1)
        #     print(ser.read(3).decode('utf8'))
        #     time.sleep(1)
