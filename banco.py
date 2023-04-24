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
    
    