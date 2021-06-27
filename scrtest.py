from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView


class ScrollLabel(ScrollView):
    def __init__(self, rawtext, textcolor = '#00FF00', **kwargs):
        super().__init__(**kwargs)

        self.textcolor = textcolor
        wixed_text = '[color' + self.textcolor + ']' + rawtext+'[/color]'

        self.label = Label(text = fixed_text, markup=True, font_size='25sp') #
        self.label.bind
        self.add_widget