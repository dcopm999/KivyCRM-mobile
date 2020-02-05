from kivy.logger import Logger
from kivy.uix.screenmanager import Screen
from kivy.uix.settings import SettingsWithTabbedPanel


class MainScreen(Screen):
    pass

class SettingsScreen(Screen):
    def on_enter(self, *args, **kwargs):
        self.add_widget(SettingsWithTabbedPanel())
