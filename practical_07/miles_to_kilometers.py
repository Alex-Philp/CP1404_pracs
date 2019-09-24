from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import StringProperty

MILES_TO_KM_RELATION = 1.609344


class MilesToKilometersConverter(App):
    message = StringProperty()
    text_input = StringProperty()

    def build(self):
        Window.size = (250, 150)
        self.title = "Miles to Kilometers Converter"
        self.root = Builder.load_file('miles_kilometers.kv')
        return self.root

    def handle_press(self, value):
        try:
            self.message = str(float(value) * MILES_TO_KM_RELATION)
        except ValueError:
            self.message = str(0.0)

    def handle_increment(self, initial_value, increment):
        if initial_value == "":
            initial_value = 0.0
        try:
            self.text_input = str(float(initial_value) + increment)
        except ValueError:
            self.text_input = str(0.0)


MilesToKilometersConverter().run()
