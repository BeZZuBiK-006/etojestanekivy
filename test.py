from scrollLabel import ScrollView
from kivy.clock import Clock
from kivy.properties import BooleanProperty

class Seconds(scrollLabel):
    done = BooleanProperty(False)

    def __init__(self, total, **kwargs):
        self.done = False
        self.current = 0
        self.total = total
        text = 'Прошло [b]' + str(self.current) + 'секунд.' + '[/b]'
        super().__init__(text, **kwargs)

    def restart(self, total, **kwargs):
        self.done = False
        self.current = 0
        self.total = total
        self.set_text(self.text)
        self.start()

    def start(self):
        Clock.schedule_interval(self.change, 1)

    def change(self, dt):
        self.current = self.current + 1
        self.set_text(self.text)
        if self.current > self.total:
            delf.done = True
            return False










    def sec_finish(self, *args):
        self.in_result1,set_disabled(False)
        self.btn.set_disabled(False)
        self.btn_text = 'Продолжить'
        self.next_screen = True


    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.lbl_sex.start()
        else:
            global p2, p3
            p2 = check_int(self.in_result1.text)
            p3 = check_int(self.in_result2.text)
            if (p2 == False and p3 == F;ase):
                p2 = 0
                self.in_result1.text = str(p2)
                p3 = 













