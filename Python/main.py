# # Main python
# import serial
# import time
# import threading
# import struct
#
# cmd = []
# stop = False
#
# def decode():
#     data = cmd[2:6]
#     by = b''.join(data)
#     temp = struct.unpack('<f', by)
#     print("Temperatuur is {0:.1f} graden Celcius".format(temp[0]))
#
# # Send hex instruction to ard
# def send_instruction(instr):
#     cmd = '02' + instr + '03'
#     ser.write(bytes.fromhex(cmd))
#
# # Listens to incomming serial connection
# def listen():
#     while stop == False:
#         char = ser.read(1)
#         if (bytes.fromhex('02') == char):
#             cmd.append(char)
#         elif (bytes.fromhex('03') == char):
#             cmd.append(char)
#             decode()
#         else:
#             cmd.append(char)
#
# if __name__ == "__main__":
#     ser = serial.Serial(
#         port='/dev/COM3',
#         baudrate=9600,
#         timeout=1
#     )
#
#     time.sleep(2)
#     t = threading.Thread(target=listen)
#     t.start()
#     for i in range(0,40):
#         send_instruction('44')
#         time.sleep(1)
#         cmd = []
#     stop = True

from object import Zonwering
from object import ToGUI
import time
from Dashboard import Dashboard
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    d1 = Dashboard()
    d1.show()

    d1.addTab(1)
    d1.addTab(2)
    d1.addTab(3)
    d1.addTab(4)

    z1 = Zonwering()
    tg = ToGUI()
    time.sleep(2)
    z1.get_current_temp()
    d1.w1.setcurrentTemp(tg.return_current_temp)
    time.sleep(0.1)

    sys.exit(app.exec_())
