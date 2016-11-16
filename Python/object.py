import traffic
import converter
import Dashboard as d
import threading


class Zonwering:
    def __init__(self):
        self.arduino = traffic.Traffic()




class ToGUI:
    # Returns current temperature from Arduino to GUI
    def return_current_temp(self, bycmd):
        value = converter.hex_to_int(bycmd)
        return value

    # Returns current distance of screen from Arduino to GUI
    def return_current_distance(self, bycmd):
        print(converter.hex_to_int(bycmd))

    # Returns current light intensity from Arduino to GUI
    def return_current_light(self, bycmd):
        print(converter.hex_to_int(bycmd))

    # Returns current temperature treshold from Arduino to GUI
    def return_current_temp_treshold(self, bycmd):
        print(converter.hex_to_int(bycmd))

    # Returns current light intensity treshold from Arduino to GUI
    def return_current_light_treshold(self, bycmd):
        print(converter.hex_to_int(bycmd))

    # Returns current temperature from Arduino to GUI
    def return_succes(self, bycmd):
        print(bycmd)
        succesorfailed = bycmd[1:-2]
        if succesorfailed == b'0':
            return True
        else:
            return False
