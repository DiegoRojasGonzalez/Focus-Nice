from kivy.lang import Builder
from kivymd.app import MDApp

class FocusNiceApp(MDApp):
    def build(self):
        return Builder.load_file("style.kv")

    def on_start(self):
        self.fps_monitor_start()


FocusNiceApp().run()