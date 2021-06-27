from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

Window.clearcolor = (115/255, 0/255, 150/255, 1)

from scrollLabel import ScrollLabel
from instructions import txt_instruction, txt_test1, txt_test2, txt_test3, txt_sits

class InstrScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class PulseScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class CheckScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class PulseScrs(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Result(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class HeartScr(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr(name = 'Instro'))
        sm.add_widget(PulseScr(name = 'Pulse1'))
        sm.add_widget(PulseScrs(name = 'Pulse2'))
        sm.add_widget(CheckScr(name = 'Check'))
        sm.add_widget(Result(name = 'Result')) 

        return sm


app = HeartScr()
app.run()








