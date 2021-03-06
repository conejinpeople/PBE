class Rfid:
   
    def read_uid(self):
        # cogemos la entrada de teclado (la tarjeta funciona como uno)
        print("Pasa la tarjeta")
        numB = int(input())
        self.num = hex(numB).upper()
        return self.num
        
if __name__ == "__main__":
    rf = Rfid()
    uid = rf.read_uid()
    print(uid)
