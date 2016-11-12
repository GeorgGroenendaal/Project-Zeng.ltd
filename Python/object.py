from Python import traffic
from Python import converter


class Zonwering:
    def __init__(self):
        self.current_temp = 0
        self.current_light_intensity = 0
        self.current_rolldown_status = None
        self.temp_action_limit = None
        self.light_action_limit = None
        self.max_rollout = 160.0
        self.min_rollout = 0.5
        self.look_days_back = 0
        self.arduino = traffic.Traffic()

    def stop_it(self):
        self.arduino.stop = True

    # Asks Arduino if still connected
    def is_alive(self):
        self.arduino.send_instruction('41')

    # Requests current temperature from Arduino
    def get_current_temp(self):
        self.arduino.send_instruction('42')

    # Requests current distance from Arduino
    def get_current_distance(self):
        self.arduino.send_instruction('43')

    # Requests currently measured light intensity
    def get_current_light(self):
        self.arduino.send_instruction('44')

    # Sends roll-down command to Arduino
    def manual_rolldown(self):
        self.arduino.send_instruction('45')

    # Sends roll-up command to Arduino
    def manual_rollup(self):
        self.arduino.send_instruction('46')

    # Sends command to roll to a given distance
    def roll_to_specific_distance(self):
        self.arduino.send_instruction('47')

    # Sets/updates the roll-out temperature
    def update_temp_threshold(self):
        self.arduino.send_instruction('48')

    # Sets/updates the roll-out light intensity
    def update_light_threshold(self):
        self.arduino.send_instruction('49')

    # Requests the roll-out temperature
    def get_temp_threshold(self):
        self.arduino.send_instruction('4A')

    # Requests the roll-out light intensity
    def get_light_threshold(self):
        self.arduino.send_instruction('4B')

    # Updates the maximum roll-out distance
    def update_max_rollout(self):
        self.arduino.send_instruction('4C')

    # Updates the minimum roll-out distance
    def update_min_rollout(self):
        self.arduino.send_instruction('4D')

    # Resets a specified setting to default
    def reset_setting(self):
        self.arduino.send_instruction('4E')


class ToGUI:

    # Returns current temperature from Arduino to GUI
    def return_current_temp(self, bycmd):
        print(bycmd)
        print("Temperature returned")
        converter.hex_to_int(bycmd)

    def return_succes(self, bycmd):
        print(bycmd)
        print("Succes")
