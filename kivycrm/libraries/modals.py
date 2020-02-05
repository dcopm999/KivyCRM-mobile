from kivy.properties import ObjectProperty
from kivy.uix.modalview import ModalView


class LoginModal(ModalView):
    '''
    Окно авторизации
    '''
    username = ObjectProperty()

    password = ObjectProperty()
    status = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def login_callback(self):
        if self.username.text and self.password:
            self.is_authorized = True        
            self.dismiss()
        else:
            self.status.text = 'Incorrect login or password!'
            self.status.color = (1,0,0,1)
