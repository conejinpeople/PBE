import os #la libreria os nos permite ejecutar comandos de la consola desde python
class Rfid:

    def read_uid(self):
        # cogemos la entrada de teclado (la tarjeta funciona como uno)
        numB = int(input())
        # traducimos el int a hexadecimal y lo pasamos a mayusculas
        self.num = hex(numB).upper()[2:] #con el 2: cogemos el valor introducido a partir del segundo caracter saltandonos el 0x
        return self.num
        
if __name__ == "__main__":
    # llamamos a la clase, inicializamos la definicion y imprimimos
    rf = Rfid()
    os.system("stty -echo") #Desactivamos eco en consola
    uid = rf.read_uid()
    os.system("stty echo") #Activamos eco en cosnola
    print(uid)
