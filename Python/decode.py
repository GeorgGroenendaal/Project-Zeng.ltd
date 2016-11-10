import serial
import time


class Decoder:
    # def __init__(self):
    #     # self.command = command
    #
    #     ser = serial.Serial(
    #         port='/dev/cu.usbmodem1411',
    #         baudrate=9600,
    #         timeout=0.1
    #     )

    def decoder(self, output):
        outputNoStartEnd = output[2:-2]
        instruction = outputNoStartEnd[-2:]
        reversed = outputNoStartEnd[::-1]
        print(reversed)




d = Decoder()
d.decoder('02329A99FF4303')



