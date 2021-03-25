import gi, os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk
import threading

class Ventana(Gtk.Window):
    def __init__(self):
        
        #Creamos la ventana
        Gtk.Window.__init__(self, title="rfid_gtk.py")
        self.connect("destroy", Gtk.main_quit)
        self.set_border_width(10)
        
        #Creamos una caja para colocar la etiqueta arriba y el boton abajo
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        
        #añadimos la caja a la ventana
        self.add(self.box)
        
        #Añadimos el fondo de la caja (RGBA(rojo, verde, azul, alfa)) valores del 0 al 1 siendo el ultimo opacidad         
        #css provider más complejo pero sin errores
        self.evbox = Gtk.EventBox()
        self.evbox.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(0,0,1,1))
        
        #Creamos el texto que se situa en la caja y la añadimos         
        self.label = Gtk.Label('<span foreground="white" size="x-large">Porfavor, identifiquese con su id universitario</span>')
        self.label.set_use_markup(True)
        self.label.set_size_request(600,150)
        self.evbox.add(self.label)
        
        #Creamos el boton
        self.button = Gtk.Button(label="Clear")
        self.button.connect("clicked", self.clicked)
        
        #Añadimos a la caja con la funcion de expansion         
        self.box.pack_start(self.evbox, True, True, 0)
        self.box.pack_start(self.button, True, True, 0)

        #Creamos hilo y lo inicializamos
        thread = threading.Thread(target=self.scan_uid)
        #Si cerramos ventana, cerramos hilo tambien
        thread.setDaemon(True)
        thread.start()
        
        self.show_all()
        Gtk.Window.set_focus(self)
        Gtk.main()
        
    #Funcion llamada al pulsar el boton         
    def clicked(self, widget):
    
        #Volvemos a pedir que se introduzca el id     
        self.label.set_label('<span foreground="white" size="x-large">Porfavor, identifiquese con su id universitario</span>')
        self.evbox.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(0,0,1,1))
            
        thread = threading.Thread(target=self.scan_uid)
        thread.start()
        
    
    #Funcion llamada cuando se lee el id     
    def scan_uid(self):
        
        #Eliminamos eco       
        os.system("stty -echo")
        #Creamos una entrada para la ventana Gtk     
        entry = Gtk.Entry()
        #Introducimos el valor de dicha entrada   
        entry.set_text(input())
        #Lo pasamos a integer y lo sacamos
        numB = int(entry.get_text())
        # traducimos el int a hexadecimal y lo pasamos a mayusculas
        uid = hex(numB).upper()[2:] #con el 2: cogemos el valor introducido a partir del segundo caracter saltandonos el 0x

        #Cambiamos el texto y el color de la caja     
        self.label.set_label('<span foreground="white" size="x-large">UID: '+uid+'</span>')
        self.evbox.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(1,0,0,1))
        #Por ultimo damos focust a la ventana para que no se quede en segundo plano al recibir el uid 
        self.present()

main = Ventana()
os.system("stty echo") #en el caso de cerrar la ventana antes de introducir el uid
quit()
            