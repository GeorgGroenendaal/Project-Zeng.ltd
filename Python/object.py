from Python import encode
import threading


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

    # Haalt elke 40 sec de huidige temteratuur op vanuit de arduino
    def get_current_temp(self):
        threading.Timer(40.0, self.get_current_temp).start()
        # encode.Encoder('')
        return ''

    # Haalt elke 30 sec de huidige lichtintensiteit seconden vanuit de arduino
    def get_current_light(self):
        threading.Timer(30.0, self.get_current_light).start()
        # encode.Encoder('.')
        return ''

    # Update de huidige temperatuur elke 60 seconden naar de GUI
    def update_current_temp(self):
        # threading.Timer(60.0, self.update_current_temp()).start()
        self.current_temp = self.get_current_temp()
        return self.current_temp

    # Update de huidige lichtintensiteit elke 60 seconden naar de GUI
    def update_current_light(self):
        # threading.Timer(60.0, self.update_current_temp()).start()
        self.current_light_intensity = self.get_current_light()
        return self.current_light_intensity

    def update_current_rolldown_status(self):
        pass

    def update_temp_action_limit(self):
        pass

    def update_light_action_limit(self):
        pass

    def update_max_rollout(self):
        pass

    def update_min_rollout(self):
        pass

    def manual_rollup(self):
        pass

    def manual_rolldown(self):
        pass

    def update_graph(self):
        pass

    def process_days_back(self):
        pass

    # Temporary test method
    def turn_on_led(self):
        encode.Encoder('024203')
