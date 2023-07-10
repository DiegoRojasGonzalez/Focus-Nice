from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.clock import Clock

Window.size = (360, 640)

class UIStorage(ScreenManager):
    pass

class MainApp(MDApp):
    cicle_pom = 1500  # tiempo de trabajo en segundos
    brake_pom = 300  # tiempo de descanso corto en segundos
    long_break = 900  # tiempo de descanso largo en segundos
    
    state = "inactive"  # estado inicial: trabajo
    
    def build(self):
        Builder.load_file("style.kv")
        Clock.schedule_interval(self.update_text_time, 1)  # Llamamos al método update_text_time cada segundo
        return UIStorage()

    def update_text_time(self, dt):
        if self.state == "work":
            if self.cicle_pom > 0:
                print("work")
                self.cicle_pom -= 1
                time = self.cicle_pom
                minutes, seconds = divmod(time, 60)
                seconds = int(seconds)
                minutes = int(minutes)
                if len(str(seconds)) == 1:
                    seconds = '0' + str(seconds)
                if len(str(minutes)) == 1:
                    minutes = '0' + str(minutes)
                time = f'{minutes}:{seconds}'
                self.root.ids.time.text = str(time)
            else:
                self.state = "break"
                self.cicle_pom = self.brake_pom
                #self.root.ids.time.text = "00:00"

        elif self.state == "break":
            if self.cicle_pom > 0:
                print("break")
                self.cicle_pom -= 1
                time = self.cicle_pom
                minutes, seconds = divmod(time, 60)
                seconds = int(seconds)
                minutes = int(minutes)
                if len(str(seconds)) == 1:
                    seconds = '0' + str(seconds)
                if len(str(minutes)) == 1:
                    minutes = '0' + str(minutes)
                time = f'{minutes}:{seconds}'
                self.root.ids.time.text = str(time)
            else:
                self.cicle_pom = self.long_break
                self.state = "long_break"
                #self.root.ids.time.text = "00:00"

        elif self.state == "long_break":
            print("long_break")
            if self.cicle_pom > 0:
                self.cicle_pom -= 1
                time = self.cicle_pom
                minutes, seconds = divmod(time, 60)
                seconds = int(seconds)
                minutes = int(minutes)
                if len(str(seconds)) == 1:
                    seconds = '0' + str(seconds)
                if len(str(minutes)) == 1:
                    minutes = '0' + str(minutes)
                time = f'{minutes}:{seconds}'
                self.root.ids.time.text = str(time)
            else:
                self.cicle_pom = self.brake_pom
                self.state = "work"
                #self.root.ids.time.text = "00:00"

    def start_pomodoro(self):
        self.state = "work"
        if self.state == "work" or self.state == "break" or self.state == "long_break":
            print("¡Trabajando!")
            self.state = "work"


        

if __name__ == "__main__":
    MainApp().run()
