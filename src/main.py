from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.clock import Clock
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

Window.size = (360, 640)

class UIStorage(ScreenManager):
    pass

class MainApp(MDApp):
    cicle_pom = 1500  # tiempo de trabajo en segundos
    brake_pom = 300  # tiempo de descanso corto en segundos
    Long_Break = 500  # tiempo de descanso largo en segundos
    state = "Inactive"  # estado inicial: trabajo
    dialog = None
    
    def build(self):
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
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
    
    def play_pause_pomodoro(self):
        if self.state == "Inactive":
            self.state = "Focus"
            self.root.ids.play_button.icon = 'pause-circle-outline' 
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = "Gray"
        elif not self.state == "Inactive":
            self.state = "Inactive"
            self.theme_cls.theme_style = "Light"
            self.theme_cls.primary_palette = "Blue"
            self.root.ids.play_button.icon = 'play-circle-outline' 

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text=" Are you sure you want to restart the pomodoro timer?",
                buttons=[
                    MDFlatButton(
                        text="RESTART",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=lambda x: self.reset_pomodoro(),
                    ),
                    MDFlatButton(
                        text="DISCARD",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=lambda x: self.dialog.dismiss(),
                    ),
                ],
            )
        self.dialog.open()
    def reset_button(self):
        self.show_alert_dialog()
        self.state = "Inactive"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"

    def reset_pomodoro(self):
        self.root.ids.play_button.icon = 'play-circle-outline' 
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        self.cicle_pom = 1500
        self.root.ids.time.text = "25:00"
        self.brake_pom = 300
        self.Long_Break = 900
        self.dialog.dismiss(),
        
if __name__ == "__main__":
    MainApp().run()
