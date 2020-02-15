#import time
import pyttsx3
import speech_recognition as sr
from fuzzywuzzy import fuzz

from abc import ABCMeta, abstractmethod, abstractproperty


class SpeecherMinix:
    __metaclass__ = ABCMeta

    def __init__(self, *args, **kwargs):
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()
        self.microphone_id = 1
        self.microphone = sr.Microphone(device_index=self.microphone_id)
        self.opts = {
            'alias': ('ЦРМ', ),
            'tbr': ('открой', ),
            'commands': {
                'login_screen': ('авторизации', 'логин'),
                'on_login': ('войти', 'вход'),
                },
        }

        self.to_text()
        for index, name in enumerate(sr.Microphone.list_microphone_names()):
            print(index, name)
        super(SpeecherMinix, self).__init__(*args, **kwargs)

    def to_text(self):

        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
        stop_listening = self.recognizer.listen_in_background(self.microphone, self.callback)
        #while stop_listening:
        #    time.sleep(0.1)
        

    def callback(self, recognizer, audio):
        '''
        Запускается каждый раз когда произносится фраза в микрофон
        '''
        try:
            voice = self.recognizer.recognize_google(audio, language='ru_RU').lower()
            print("[Log] Распознано: " + voice)
            # Если текст начинается с имени помошника
            if voice.startswith(self.opts['alias']):
                voice = [voice.replace(item, '').strip() for item in self.opts['alias']]
                voice = [voice.replace(item, '').strip() for item in self.opts['tbr']]

            cmd = self.recognize_cmd(voice)
            self.execute_cmd(cmd)

        except sr.UnknownValueError:
            pass
            # self.to_speech('Нераспознанно, повторите ввод')
        except sr.RequestError:
            self.to_speech('Неизвестная ошибка, проверьте подключение к сети интернет')

    def recognize_cmd(self, cmd):
        '''
        Распознани нечетко произнесенных команд
        '''
        RC = {'cmd': '', 'percent': 50}
        for k,v in self.opts['commands'].items():
            for x in v:
                vrt = fuzz.ratio(cmd, x)
                if vrt >  RC['percent']:
                    RC['cmd'] = k
                    RC['percent'] = vrt
        return RC

    # @abstractmethod
    def execute_cmd(self, cmd):
        print(cmd)
        if cmd.get('cmd') == 'login_screen':
            self.manager.current = 'Login'
        

    def to_speech(self, text=None):
        if text is not None:
            self.engine.say(text)
            self.engine.runAndWait()

    '''
    def test(self):
        self.to_speech(self.to_text())
    
    def get_command(self):
        with sr.Microphone(device_index=self.microphone_id) as source:
            audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio, language='ru_RU')
            self.engine.say(query.lower())
        except UnknownValueError:
            self.engine.say('Нераспознанная команда,, повторите ввод:')
        finally:
            self.engine.runAndWait()
    '''