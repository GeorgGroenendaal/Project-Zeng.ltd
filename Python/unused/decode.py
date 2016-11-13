# Main python
import serial
import time
import threading
import struct

cmd = []
stop = False


def decode():
    data = cmd[2:6]
    by = b''.join(data)
    temp = struct.unpack_from('<f', by)
    print("Temperatuur is {0:.1f} graden Celcius".format(temp[0]))


# Send hex instruction to ard
def send_instruction(instr):
    cmd = '02' + instr + '03'
    ser.write(bytes.fromhex(cmd))


# Listens to incoming serial connection
def listen():
    while not stop:
        char = ser.read(1)
        if bytes.fromhex('02') == char:
            cmd.append(char)
        elif bytes.fromhex('03') == char:
            cmd.append(char)
            decode()
        else:
            cmd.append(char)


if __name__ == "__main__":
    ser = serial.Serial(
        port='/dev/cu.usbmodem1411',
        baudrate=9600,
        timeout=1
    )

    time.sleep(2)
    t = threading.Thread(target=listen)
    t.start()
    for i in range(10):
        send_instruction('42')
        time.sleep(1)
        cmd = []
    stop = True
