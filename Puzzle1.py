class Rfid:
   
    def read_uid(self):
        # cogemos la entrada de teclado (la tarjeta funciona como uno)
        print("Pasa la tarjeta")
        numB = int(input())
        # traducimos el int a hexadecimal y lo pasamos a mayusculas
        self.num = hex(numB).upper()
        return self.num
        
if __name__ == "__main__":
    # llamamos a la clase, inicializamos la definicion y imprimimos
    rf = Rfid()
    uid = rf.read_uid()
    print(uid)
