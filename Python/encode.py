import serial
import time


class Encoder:
    def __init__(self, command):
        self.command = command

        ser = serial.Serial(
            port='/dev/cu.usbmodem1411',
            baudrate=9600,
            timeout=0.1
        )

        while 1:
            string = bytes.fromhex(self.command)
            ser.write(string)
            time.sleep(1)
            print(ser.read(3).decode('utf8'))
            time.sleep(1)
