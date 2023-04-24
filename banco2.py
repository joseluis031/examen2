#codigo simulacion banco con pool

import random
import time
from multiprocessing import Pool

class Banco:
    def __init__(self,saldo):
        self.saldo_inicial = saldo
        self.saldo = saldo
        
    
    def movimiento(self, monto):
        self.saldo += monto
        return self.saldo
    
    def saldo(self):
        return self.saldo == self.saldo_inicial
    
    def __str__(self):
        return "Saldo: {}".format(self.saldo)
    

class Cliente:
    def __init__(self, nombre, banco):
        self.nombre = nombre
        self.banco = banco
        
    def retirar(self, monto):
        if self.banco.saldo >= monto:
            self.banco.movimiento(-monto)
            return True
        else:
            return False
        
    def depositar(self, monto):
        self.banco.movimiento(monto)
        return True
    
    def __str__(self):
        return "Cliente: {} - Saldo: {}".format(self.nombre, self.banco.saldo)
    
    
def simulacion(cliente):
    for i in range(100):
        if random.randint(0,1) == 0:
            cliente.retirar(random.randint(1,10))
        else:
            cliente.depositar(random.randint(1,10))
        time.sleep(0.01)
    print(cliente)
    
def main():
    banco = Banco(100) #saldo inicial   
    clientes = [] #lista de clientes
    for i in range(5): 
        clientes.append(Cliente("\nCliente {}".format(i), banco))
    
    pool = Pool(processes=4)
    pool.map(simulacion, clientes)
    pool.close()
    pool.join()
    
    print(banco)
    
if __name__ == "__main__":
    main()