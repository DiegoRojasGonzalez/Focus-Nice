from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from pomodoro import Pomodoro

class MainApp(App):
    def build(self):
        return BoxLayout()

    def start_pomodoro(self):
        pomodoro = Pomodoro("Clasico", 25, 5, 15, 4, 0, "Focus", 0)
        pomodoro.start()

if __name__ == '__main__':
    MainApp().run()


