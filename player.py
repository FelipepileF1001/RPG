from mobs import *
from armas import *
from itens import *
from typing import *

# Classe principal do usuário convencional

class Jogador(Mob):
    nome : str
    exp : int
    inv_armas : List[Arma]

    def __init__(self, vida, dano, nome, exp):
        super().__init__(vida, dano)
        self.nome = nome
        self.exp = exp
        self.inv_armas : List[Arma] = []

    def evoluir(self, Jogador):
        if Jogador.exp >= 100:
            print("EVOLUIU")
            Jogador.vida += 5
            Jogador.dano += 5
            Jogador.exp -= 100
        else:
            print("Falta", 100-Jogador.exp,"pontos para evoluir !!!")