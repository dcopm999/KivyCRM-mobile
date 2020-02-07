from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.logger import Logger

from kivy.uix.settings import SettingsWithSidebar
from kivy.uix.screenmanager import ScreenManager
from kivycrm.libraries import (modals, screens)

from kivycrm.libraries.settings import settings_json



Config.set('kivy', 'keymoard_move', 'systemanddoc')


class KivycrmApp(App):
    """
    Main kivy app

    Edit kivycrm.kv to get started.
    """
    SCREEN_MANAGER = ScreenManager()
    DEBUG = False
    is_authorized = False

    def build(self):
        self.settings_cls = SettingsWithSidebar
        self.SCREEN_MANAGER.add_widget(screens.MainScreen(name='Main'))
        self.SCREEN_MANAGER.current= 'Main'
        return self.SCREEN_MANAGER

    def build_settings(self, settings):
        settings.add_json_panel(
            'Authorization',
            self.config,
            data=settings_json,
        )
    
    def build_config(self, config):
        config.setdefaults('authorization', 
            {
                'hostname': 'http://127.0.0.1',
                'port': 80,
                'username': '',
                'password': '',
                'remember': '',
            }
        )

    def on_start(self):
        if self.DEBUG:
            import cProfile
            self.profile = cProfile.Profile()
            self.profile.enable()

        if not self.is_authorized:
            login_modal = modals.LoginModal(config=self.config, auto_dismiss=False)
            login_modal.open()

    def on_stop(self):
        if self.DEBUG:
            self.profile.disable()
            self.profile.dump_stats(os.path.join(BASE_DIR, 'main_app.profile'))


if __name__ == '__main__':
    KivycrmApp().run()

