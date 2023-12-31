from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.clock import Clock
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.core.audio import SoundLoader
from kivymd.uix.snackbar import Snackbar 
from kivymd.uix.bottomsheet import MDListBottomSheet
import webbrowser


Window.size = (360, 640)

class UIStorage(ScreenManager):
    pass

class FocusNiceApp(MDApp):
    cicle_pom = 1500
    brake_pom = 300   
    Long_Break = 900 
    state = "Inactive"   
    dialog = None
    snackbar = None
    cicles = 0
    alarm_clock = SoundLoader.load('sounds/MechanicalClockSound.wav')
    rain_sound = SoundLoader.load('sounds/Rain.mp3')
    rain_sound.loop = True
    rain_sound.volume = 0
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange" 
        Builder.load_file("style.kv")
        Clock.schedule_interval(self.update_text_time, 1) 
        return UIStorage()
    
    def on_start(self):
        self.root.ids.slider_volume.opacity = 0
        self.root.ids.slider_volume.disabled = True
        self.rain_sound.play()

    def on_resume(self):
        print("on resume")
        Clock.schedule_interval(self.update_text_time, 1)

    def on_pause(self):
        print("on pause")
        Clock.unschedule(self.update_text_time)

    def update_text_time(self, dt):
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
            self.root.ids.focus_button.text_color = "orange"
            self.root.ids.brake_button.text_color = "gray"
            self.root.ids.long_brake_button.text_color = "gray"
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
                self.alarm_clock.play()
                self.show_snackbar_alert()
                self.state = "Break"
                self.cicle_pom = self.brake_pom

        elif self.state == "Break":
            self.root.ids.focus_button.text_color = "gray"
            self.root.ids.brake_button.text_color = "orange"
            self.root.ids.long_brake_button.text_color = "gray"
            self.root.ids.time.text = "05:00"
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
                self.cicles += 1
                self.alarm_clock.play()
                self.show_snackbar_alert()
                if self.cicles == 4:  
                    self.cicles = 0                  
                    self.cicle_pom = self.Long_Break
                    self.state = "Long_Break"
                else:
                    self.cicle_pom = self.brake_pom
                    self.state = "Focus"

        elif self.state == "Long_Break":
            self.root.ids.focus_button.text_color = "gray"
            self.root.ids.brake_button.text_color = "gray"
            self.root.ids.long_brake_button.text_color = "orange"
            self.root.ids.time.text = "15:00"
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
                self.alarm_clock.play()
                self.show_snackbar_alert()
                self.cicle_pom = self.brake_pom
                self.state = "Focus"
    
    def play_pause_pomodoro(self):
        if self.state == "Inactive":
            self.state = "Focus"
            self.root.ids.play_button.icon = 'pause-circle-outline' 
        elif not self.state == "Inactive":
            self.rain_sound.volume = 0
            self.root.ids.focus_button.text_color = "gray"
            self.root.ids.brake_button.text_color = "gray"
            self.root.ids.long_brake_button.text_color = "gray"
            self.state = "Inactive"
            self.root.ids.play_button.icon = 'play-circle-outline' 

    
    def show_snackbar_alert(self):
        currently_state = self.state
        if currently_state == "Focus":
            message = "You focus nice it's time to move your body"
        if currently_state == "Break":
            message = "Go to work"
        elif currently_state == "Long_Break":
            message = "You have completed 4 pomodoros relax"
        self.snackbar = Snackbar(text=f"{message}",)
        self.snackbar.open()
    
    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text=" Are you sure you want to restart the pomodoro timer?",
                buttons=[
                    MDFlatButton(
                        text="RESTART",
                        on_release=lambda x: self.reset_pomodoro(), 

                    ),
                    MDFlatButton(
                        text="DISCARD",
                        on_release=lambda x: self.demis_reset(),
                    ),
                ],
            )
        self.dialog.open()
    def reset_button(self):
        self.show_alert_dialog()
        self.state = "Inactive"


    def reset_pomodoro(self):
        self.root.ids.play_button.icon = 'play-circle-outline' 
        self.cicle_pom = 1500
        self.root.ids.time.text = "25:00"
        self.brake_pom = 300
        self.Long_Break = 900
        self.cicles = 0                  
        self.dialog.dismiss(),
        self.root.ids.focus_button.text_color = "gray"
        self.root.ids.brake_button.text_color = "gray"
        self.root.ids.long_brake_button.text_color = "gray"
    
    def demis_reset(self):
        self.dialog.dismiss()
        self.root.ids.play_button.icon = 'play-circle-outline'


    def play_pause_music(self):   
        if self.root.ids.music_button.icon == "music-off":
            self.root.ids.music_button.icon = "music"
            self.rain_sound.volume = 0.5
            self.root.ids.slider_volume.opacity = 1
            self.root.ids.slider_volume.disabled = False

        else:
            self.root.ids.music_button.icon = "music-off"
            self.rain_sound.volume = 0
            self.root.ids.slider_volume.opacity = 0
            self.root.ids.slider_volume.disabled = True

    def show_bottom_sheet_info(self):
        bottom_sheet_menu = MDListBottomSheet()
        bottom_sheet_menu.add_item(
            "Linkedin",
            lambda x: webbrowser.open("https://www.linkedin.com/in/diegoignaciorojasgonzalez/"),
            icon="linkedin",
        )
        bottom_sheet_menu.add_item(
            "Github",
            lambda x: webbrowser.open("https://github.com/DiegoRojasGonzalez"),
            icon="github",
        )
        bottom_sheet_menu.open()

    def change_state_focus(self):
        self.cicle_pom = 1500
        self.state = "Focus"
        self.root.ids.play_button.icon = 'pause-circle-outline' 
        self.cicle_pom = self.cicle_pom
        pass
    
    def change_state_brake(self):
        self.cicle_pom = 300
        self.state = "Break"
        self.root.ids.play_button.icon = 'pause-circle-outline' 
        self.cicle_pom = self.brake_pom
        pass
    
    def change_state_lgbrake(self):
        self.cicle_pom = 900
        self.state = "Long_Break"
        self.root.ids.play_button.icon = 'pause-circle-outline' 
        self.cicle_pom = self.cicle_pom
        pass

if __name__ == "__main__":
    FocusNiceApp().run()
