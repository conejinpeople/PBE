import getpass #la libreria nos oculta la informacion introducida por teclado
class Rfid:

    def read_uid(self):
        # cogemos la entrada de teclado (la tarjeta funciona como uno)
        numB = int(getpass.getpass(prompt="")) #Colocamos un espacio de prompt sino nos imprimer "password"
        # traducimos el int a hexadecimal y lo pasamos a mayusculas
        self.num = hex(numB).upper()[2:] #con el 2: cogemos el valor introducido a partir del segundo caracter saltandonos el 0x
        return self.num
        
if __name__ == "__main__":
    # llamamos a la clase, inicializamos la definicion y imprimimos
    rf = Rfid()
    uid = rf.read_uid()
    print ("\033[A\033[A") #limpiamos la linea previa y colocamos el cursor en ella
    print(uid)
