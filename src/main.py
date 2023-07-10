from kivymd.app import MDApp                                #incluimos la libreria de kivymd para Material Design
from kivy.lang import Builder                               #incluimos el builder para iniciar el archivo kv con los estilos
from kivy.uix.screenmanager import ScreenManager, Screen    #incluimos el screen manager para cambiar de pantalla
from kivy.core.window import Window                         #incluimos la libreria de window para cambiar el tamaño de la ventana 
from kivy.clock import Clock

Window.size = (360, 640)                                    #cambiamos el tamaño de la ventana

class UIStorage(ScreenManager):                             #creamos la clase UIStorage que hereda de ScreenManager
    pass

class MainApp(MDApp):                                       #creamos la clase MainApp que hereda de MDApp
    # Zona de definicion de variables
    cicle_pom = 1500 #tiempo de trabajo
    brake_pom = 300 #tiempo de descanso corto
    long_break = 900 #tiempo de descanso largo
    #
    
    state = False #estado del pomodoro en falso

    def build(self):                                        #creamos el metodo build que se encarga de iniciar la aplicacion
        Builder.load_file("style.kv")                       #cargamos el archivo kv con los estilos
        Clock.schedule_interval(self.update_text_time, 0)   #llamamos al metodo update_text_time cada segundo
        return UIStorage()                                  #retornamos la clase Ui

    def on_start(self):
        self.fps_monitor_start()

    # Metodo start
    def update_text_time(self, event):                       #creamos el metodo update_text_time que recibe el tiempo
        if self.state == True:                              #si el estado es falso                                           
            print("✔")
            #POMODORO ACTIVO
            #
            #
            #
            self.cicle_pom -= event                              
            time = self.cicle_pom                                
            minutes, seconds = divmod(time, 60)
            seconds = int(seconds)
            minutes = int(minutes)
            if len(str(seconds)) == 1:
                seconds = '0' + str(seconds)
            if len(str(minutes)) == 1:
                minutes = '0' + str(minutes)
            time = f'{minutes}:{seconds}'
            self.root.ids.time.text = str(time)                  #cambiamos el texto de la etiqueta time por el tiempo        
        pass
        
    def start_pomodoro(self):                               #creamos el metodo start_pomodoro
        self.state = True                                   #cambiamos el estado a verdadero

if __name__ == "__main__":                                  #verificamos que el archivo se este ejecutando directamente
    MainApp().run()                                         #ejecutamos la aplicacion
