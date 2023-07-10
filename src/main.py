from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.clock import Clock

Window.size = (360, 640)

class UIStorage(ScreenManager):
    pass

class MainApp(MDApp):
    cicle_pom = 10  # tiempo de trabajo en segundos
    brake_pom = 3  # tiempo de descanso corto en segundos
    Long_Break = 5  # tiempo de descanso largo en segundos
    
    state = "Inactive"  # estado inicial: trabajo
    
    def build(self):
        Builder.load_file("style.kv")
        Clock.schedule_interval(self.update_text_time, 1)  # Llamamos al método update_text_time cada segundo
        return UIStorage()

    def update_text_time(self, dt):
        print(self.state)
        if self.state == "Inactive":
            time_actually = self.cicle_pom
            minutes, seconds = divmod(time_actually, 60)
            seconds = int(seconds)
            minutes = int(minutes)
            if len(str(seconds)) == 1:
                seconds = '0' + str(seconds)
            if len(str(minutes)) == 1:
                minutes = '0' + str(minutes)
            time_actually = f'{minutes}:{seconds}'
            self.root.ids.time.text = str(time_actually)
            
        if self.state == "Focus":
            if self.cicle_pom > 0:
                print("Focus")
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
                self.state = "Break"
                self.cicle_pom = self.brake_pom

        elif self.state == "Break":
            if self.cicle_pom > 0:
                print("Break")
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
                self.cicle_pom = self.Long_Break
                self.state = "Long_Break"

        elif self.state == "Long_Break":
            print("Long Break")
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
                self.state = "Focus"
    
    def start_pomodoro(self):
        self.state = "Focus"        
        print("Start")
        
    def pause_pomodoro(self):
        self.state = "Inactivo"
        print("Pause")

    def reset_pomodoro(self):
        self.state = "Inactivo"
        print("Restart")
        self.cicle_pom = 1500
        self.root.ids.time.text = "25:00"
        self.brake_pom = 300
        self.Long_Break = 900

if __name__ == "__main__":
    MainApp().run()
