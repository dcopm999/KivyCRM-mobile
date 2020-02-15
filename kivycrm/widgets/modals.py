from kivy.uix.modalview import ModalView


class LoginModal(ModalView):
    '''
    Окно авторизации
    '''
    def __init__(self, config, **kwargs):
        self.config = config
        super().__init__(**kwargs)

    def on_pre_open(self):
        print(self.username)
        self.username.text = self.config.get('authorization', 'username')
        self.password.text = self.config.get('authorization', 'password')
        self.remember.active = self.config.get('authorization', 'remember')

    def login_callback(self):
        if self.username.text != '' and self.password != '':
            self.is_authorized = True
            if self.remember.active:
                self.config.set('authorization', 'username', self.username.text)
                self.config.set('authorization', 'password', self.password.text)
                self.config.set('authorization', 'remember', self.remember.active)
                self.config.write()
            else:
                self.config.set('authorization', 'username', '')
                self.config.set('authorization', 'password', '')
                self.config.set('authorization', 'remember', '')
                self.config.write()
            self.dismiss()
        else:
            self.status.text = 'Incorrect login or password!'
            self.status.color = (1,0,0,1)
