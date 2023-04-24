import random

class Jugador:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial
        
    def apuesta_numero(self, numero):
        self.saldo -= 10
        if random.randint(0, 36) == numero:
            self.saldo += 360
    
    def apuesta_par_impar(self, es_par):
        self.saldo -= 10
        if (random.randint(0, 36) % 2 == 0) == es_par:
            self.saldo += 20
    
    def apuesta_martingala(self, numero):
        apuesta = 10
        while True:
            self.saldo -= apuesta
            if random.randint(0, 36) == numero:
                self.saldo += apuesta * 36
                break
            apuesta *= 2


class Banca:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial
        
    def acepta_apuesta(self, cantidad):
        self.saldo += cantidad
        
    def paga_ganancias(self, cantidad):
        if cantidad > self.saldo:
            cantidad = self.saldo
        self.saldo -= cantidad
        return cantidad
        
    def incrementa_saldo(self, cantidad):
        self.saldo += cantidad