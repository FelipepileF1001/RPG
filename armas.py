from abc import ABCMeta, ABC, abstractmethod
from mobs import *
import random

# Este arquivo está reservado a armas de players e inimigos, qualquer item que pode ser usado para ferir uma criatura
# será considerado uma arma, sendo ela uma espada, arco ou cajado.

class Arma(ABC):
    nome : str
    dano : int

    def __init__(self, dano, nome):
        self.dano = dano
        self.nome = nome

    def golpear(self, dano, Mob):
        Mob.vida -= dano

#LONGA DISTÂNCIA
class Longe(Arma):
    def atirar(self, dano, Mob):
        Mob.vida -= dano

class Arco(Longe):
    dano = random.randrange(10, 15)
    crit_dano = 25

class Besta(Longe):
    dano = 20
    crit_dano = 50

#CURTA DISTÂNCIA
class Perto(Arma):
    def atacar(self, dano, Mob):
        Mob.vida -= dano

class Espada(Perto):
    dano = 12
    crit_dano = 30

class Machado(Perto):
    dano = 24
    crit_dano = 60