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
    #40 procesos para ingresar 100
    for i in range(40):
        cliente.depositar(100)
        
    #40 procesos para retirar 100
    for i in range(40):
        cliente.retirar(100)
        
    #20 procesos para ingresar 50
    for i in range(20):
        cliente.depositar(50)
        
    #20 procesos para retirar 50
    for i in range(20):
        cliente.retirar(50)
        
    #60 procesos para ingresar 20
    for i in range(60):
        cliente.depositar(20)
    
    #60 procesos para retirar 20
    for i in range(60):
        cliente.retirar(20)
        
    print(cliente)
    
def main():
    banco = Banco(100) #saldo inicial   
    clientes = [] #lista de clientes
    for i in range(1):  #crea 1 cliente
        clientes.append(Cliente("\nCliente {}".format(i), banco))
    
    pool = Pool(processes=4) #crea 4 procesos
    pool.map(simulacion, clientes)  #ejecuta la funcion simulacion en los 4 procesos
    pool.close()    #cierra los procesos
    pool.join()    #espera a que terminen los procesos
    
    print(banco)
    
if __name__ == "__main__":
    main()