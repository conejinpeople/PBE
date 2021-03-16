import gi, os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk
import threading
import Puzzle1Correccio

class Ventana(Gtk.Window):
    def __init__(self):
        
        #Creamos la ventana
        Gtk.Window.__init__(self, title="rfid_gtk.py")
        self.connect("destroy", Gtk.main_quit)
        self.set_border_width(10)
        
        #Creamos una caja para colocar la etiqueta rriba y el boton abajo
        
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
        
        #Leemos id (puzzle1)       
        reader = Puzzle1Correccio.Rfid()
        os.system("stty -echo")
        uid = reader.read_uid()
        os.system("stty echo")
        
        #Cambiamos el texto y el color de la caja     
        self.label.set_label('<span foreground="white" size="x-large">UID: '+uid+'</span>')
        self.evbox.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(1,0,0,1))

main = Ventana()
os.system("stty echo") #en el caso de cerrar la ventana antes de introducir el uid
quit()
            