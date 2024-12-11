from abc import ABC, abstractmethod
from mobs import *

# Este arquivo está reservado a itens que podem mudar o status da criatura.

class Potion(ABC):
    qte_uso : int
    valor : int
    status : bool

    def __init__(self, qte_uso, valor, status):
        self.qte_uso = qte_uso
        self.valor = valor
        self.status = status

    def usar_potion(self, Mob):
        if self.status == False:
            Mob.vida -= self.valor
        else:
            Mob.vida += self.valor
            
        self.qte_uso -= 1