

from kivy.app import App
from kivy.lang import Builder


__author__ = 'Matthew Spina'

M_TO_KM = 1.60934

class MilesToKilometresApp(App):
    """ MilesToKilometresApp is a Kivy App for converting metres to kilometres """
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "M to Km"
        self.root = Builder.load_file('miles_to_km.kv')
        return self.root

    def handle_calculate(self):
        """ handle calculation (could be button press or other call), output result to label widget """
        value = self.handle_valid_input()
        result = value * M_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self,change):
        value = self.handle_valid_input() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def handle_valid_input(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesToKilometresApp().run()
