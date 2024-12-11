from mobs import *
from itens import *
from typing import *
import random

class Jogador(Mob):
    inv : List[Arma]

    def __init__(self, vida, dano):
        super().__init__(vida, dano)
        self.inv : List[Arma] = []

p1 = Jogador(50, 5)

dano = int

e1 = Espada(dano)
b1 = Besta(dano)

p1.inv.append(e1)
p1.inv.append(b1)

p2 = Jogador(50, dano)

while(p2.vida >= 0):

    esc = int(input("O que vai fazer?\n1 - Atacar\n2 - Fugir\nDigite AQUI: "))
    print("\n")

    if esc == 1: 

        esc_arma = int(input("1 - Espada\n2 - Besta\nDigite AQUI: "))
        print("\n")

        if esc_arma == 1:

            atk = random.randrange(1, 21)
            print(atk)

            dano = random.randrange(10, 15)
            crit_dano = dano*(2.5)

            if atk == 1:
                print("ERROU")
            elif atk > 1 and atk < 16:
                print("ACERTO NORMAL")
                e1.atacar(dano, p2)
                print(dano)
            elif atk > 15:
                print("CRITOU")
                e1.atacar(crit_dano, p2)
                print(crit_dano)

        elif esc_arma == 2:

            atk = random.randrange(1, 21)
            print(atk)

            dano = random.randrange(12, 17)
            crit_dano = dano*(3.5)

            if atk == 1:
                print("ERROU")
            elif atk > 1 and atk < 13:
                print("ACERTO NORMAL")
                b1.atirar(dano, p2)
                print(dano)
            elif atk > 12:
                print("CRITOU")
                b1.atirar(crit_dano, p2)
                print(crit_dano)


        print(p2.vida)

    elif esc == 2:
        print("ARREGÃO")
        p1.fugir()