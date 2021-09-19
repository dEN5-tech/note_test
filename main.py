from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.animation import Animation
from kivy.uix.scrollview import ScrollView
from  kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivymd.uix.behaviors import HoverBehavior
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineListItem
from kivymd.uix.behaviors import RectangularElevationBehavior, FocusBehavior
from kivy.properties import ListProperty
from kivymd.app import MDApp

class HoverText(HoverBehavior,OneLineListItem):
    pressed = ListProperty([0, 0])
    def __init__(self, **kwargs):
        super(HoverText, self).__init__(**kwargs)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            print(touch.pos)
            self.pressed = touch.pos
            return True
        return super(HoverText, self).on_touch_down(touch)


class MainApp(MDApp):
    def build(self):
        out = Builder.load_file("main.kv")
        return out


MainApp().run()




