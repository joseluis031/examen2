from multiprocessing import Pool

class Banco:
    def __init__(self,saldo):
        self.saldo = saldo
        
    def ingreso(self,monto):
        self.saldo += monto
        print("Ingreso: {}".format(monto))
        
    def retiro(self,monto):
        self.saldo -= monto
        print("Retiro: {}".format(monto))
        
    def __str__(self):
        return "Saldo: {}".format(self.saldo)
    
def main():
    
    banco = Banco(100)
    
    #pool para ingresar
    
    ingreso100 = Pool()
    ingreso100.map_async(banco.ingreso(100),range(40))
    
    retiro100 = Pool()
    retiro100.map_async(banco.retiro(100),range(40))
    
    ingreso50 = Pool()
    ingreso50.map_async(banco.ingreso(50),range(20))
    
    retiro50 = Pool()
    retiro50.map_async(banco.retiro(50),range(20))
    
    ingreso20 = Pool()
    ingreso20.map_async(banco.ingreso(20),range(60))
    
    retiro20 = Pool()
    retiro20.map_async(banco.retiro(20),range(20))    
    
    print("Saldo final:", banco.__str__())
    

if __name__ == "__main__":
    main()