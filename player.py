from mobs import *
from armas import *
from typing import *

# Classe principal do usuário convencional

class Jogador(Mob):
    inv : List[Arma]

    def __init__(self, vida, dano):
        super().__init__(vida, dano)
        self.inv : List[Arma] = []