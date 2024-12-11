from mobs import *
from armas import *
from itens import *
from typing import *

# Classe principal do usuário convencional

class Jogador(Mob):
    inv_armas : List[Arma]

    def __init__(self, vida, dano):
        super().__init__(vida, dano)
        self.inv_armas : List[Arma] = []