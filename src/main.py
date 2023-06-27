from kivymd.app import MDApp                                #incluimos la libreria de kivymd para Material Design
from kivy.lang import Builder                               #incluimos el builder para iniciar el archivo kv con los estilos
from kivy.uix.screenmanager import ScreenManager, Screen    #incluimos el screen manager para cambiar de pantalla
from kivy.core.window import Window                         #incluimos la libreria de window para cambiar el tamaño de la ventana 
from pomodoro import Pomodoro                               #incluimos la clase pomodoro para modificar el objeto

Window.size = (360, 640)                                    #cambiamos el tamaño de la ventana

class UIStorage(ScreenManager):                             #creamos la clase UIStorage que hereda de ScreenManager
    pass

class MainApp(MDApp):                                       #creamos la clase MainApp que hereda de MDApp
    
    def build(self):                                        #creamos el metodo build que se encarga de iniciar la aplicacion
        Builder.load_file("style.kv")                       #cargamos el archivo kv con los estilos
        return UIStorage()                                  #retornamos la clase Ui

        
    #Aqui van las funciones 
    # 
    #

if __name__ == "__main__":                                  #verificamos que el archivo se este ejecutando directamente
    MainApp().run()                                         #ejecutamos la aplicacion
