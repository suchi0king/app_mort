from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class MortgageCalculatorAPP(MDApp):
    def build(self):
        return MDLabel(text = 'hello,world', halign="center")



MortgageCalculatorAPP().run()