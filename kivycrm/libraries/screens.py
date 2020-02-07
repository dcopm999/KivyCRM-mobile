from kivy.logger import Logger
from kivy.uix.screenmanager import Screen
from kivy.uix.settings import SettingsWithTabbedPanel


class MainScreen(Screen):
    pass

class SettingsScreen(Screen):
    def on_enter(self, *args, **kwargs):
        self.add_widget(SettingsWithTabbedPanel())

class LoginScreen(Screen):

    def on_pre_enter(self):
        self.username.text = self.parent.config.get('authorization', 'username')
        self.password.text = self.parent.config.get('authorization', 'password')
        self.remember.active = self.parent.config.get('authorization', 'remember')

    def on_login(self):
        if self.username.text != '' and self.password != '':
            self.is_authorized = True
            if self.remember.active:
                self.parent.config.set('authorization', 'username', self.username.text)
                self.parent.config.set('authorization', 'password', self.password.text)
                self.parent.config.set('authorization', 'remember', self.remember.active)
                self.parent.config.write()
            else:
                self.parent.config.set('authorization', 'username', '')
                self.parent.config.set('authorization', 'password', '')
                self.parent.config.set('authorization', 'remember', '')
                self.parent.config.write()
            self.manager.transition.direction = 'left'
            self.parent.current = 'Main'
        else:
            self.status.text = 'Incorrect login or password!'
            self.status.color = (1,0,0,1)