from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicNames(App):
    NAMES = ["Jimmy", "Jimbo", "Jimjar", "Jimson", "Jimley", "Georgem"]

    def build(self):
        self.title = "A List of Names"
        self.root = Builder.load_file('dynamic_names.kv')
        return self.root

    def create_widgets(self):
        for name in self.NAMES:
            temp_label = Label(text=name, id=name)
            self.root.ids.name_list.add_widget(temp_label)

DynamicNames().run()