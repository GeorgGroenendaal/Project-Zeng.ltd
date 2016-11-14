import serial
import threading
import object as obj
import time


class Traffic:
    def __init__(self):
        self.ser = serial.Serial(port='/dev/cu.usbmodem1411',
                                 baudrate=9600,
                                 timeout=0.1)
        self.cmd = []
        self.stop = False
        self.instr = None
        self.codes = {
            '41': obj.ToGUI.return_succes,
            '42': obj.ToGUI.return_current_temp,
            '43': obj.ToGUI.return_current_distance,
            '44': obj.ToGUI.return_current_light,
            '45': obj.ToGUI.return_succes,
            '46': obj.ToGUI.return_succes,
            '47': obj.ToGUI.return_succes,
            '48': obj.ToGUI.return_succes,
            '49': obj.ToGUI.return_succes,
            '4A': obj.ToGUI.return_current_temp_treshold,
            '4B': obj.ToGUI.return_current_light_treshold,
            '4C': obj.ToGUI.return_succes,
            '4D': obj.ToGUI.return_succes,
            '4E': obj.ToGUI.return_succes
        }


    # Send hex instruction to ard
    def send_instruction(self, instruction):
        time.sleep(0.1)
        self.instr = instruction
        cmd = '02' + self.instr + '03'
        self.ser.write(bytes.fromhex(cmd))
        self.stop = False
        threading.Thread(target=self.listen).start()

    # Decodes incoming instructions
    def decode(self):
        bycmd = b''.join(self.cmd)
        self.codes[self.instr](None, bycmd)

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
