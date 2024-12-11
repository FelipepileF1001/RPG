from mobs import *

class Arma:
    dano : int

    def __init__(self, dano):
        self.dano = dano

    def golpear(self, dano, Mob):
        Mob.vida -= dano

#LONGA DISTÂNCIA______________________________________________________________________________________________________
class Longe(Arma):
    def atirar(self, dano, Mob):
        Mob.vida -= dano

class Arco(Longe):
    dano = 10
    crit_dano = 25

class Besta(Longe):
    dano = 20
    crit_dano = 50

#CURTA DISTÂNCIA________________________________________________________________________________________________________
class Perto(Arma):
    def atacar(self, dano, Mob):
        Mob.vida -= dano

class Espada(Perto):
    dano = 12
    crit_dano = 30

class Machado(Perto):
    dano = 24
    crit_dano = 60