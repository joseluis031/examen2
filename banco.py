#codigo de simulacion de banco

import random
import time

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
    
    
def main():
    
    
    