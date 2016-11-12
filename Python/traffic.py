import serial
import threading
from Python import object as obj


class Traffic:
    def __init__(self):
        self.ser = serial.Serial(port='/dev/cu.usbmodem1411',
                                 baudrate=9600,
                                 timeout=0.1)
        self.cmd = []
        self.stop = False
        self.instr = None
        # Assignment of return value-methods to me made in object and assigned from decode()
        self.codes = {
            '41': obj.ToGUI.return_succes,
            '42': obj.ToGUI.return_current_temp,
        }
        threading.Thread(target=self.listen).start()

    # Send hex instruction to ard
    def send_instruction(self, instruction):
        self.instr = instruction
        cmd = '02' + self.instr + '03'
        self.ser.write(bytes.fromhex(cmd))

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
                self.stop = True
