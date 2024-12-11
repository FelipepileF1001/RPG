from mobs import *
from armas import *
from itens import *
from typing import *
import random

class Jogador(Mob):
    inv : List[Arma]

    def __init__(self, vida, dano):
        super().__init__(vida, dano)
        self.inv : List[Arma] = []



