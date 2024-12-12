from player import *
import random

def batalha(p1 : Jogador, p2 : Jogador, turno):

    print("\n")

    if turno % 2 == 0:
        print(p1.nome,"\n")
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
                    print(dano,"\n")
                elif atk > 15:
                    print("CRITOU")
                    e1.atacar(crit_dano, p2)
                    print(crit_dano,"\n")

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
                    print(dano,"\n")
                elif atk > 12:
                    print("CRITOU")
                    b1.atirar(crit_dano, p2)
                    print(crit_dano,"\n")

            elif esc == 2:
                print("ARREGÃO")
                p1.fugir()

    elif turno % 2 == 1:
        print(p2.nome,"\n")
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
                    e1.atacar(dano, p1)
                    print(dano,"\n")
                elif atk > 15:
                    print("CRITOU")
                    e1.atacar(crit_dano, p1)
                    print(crit_dano,"\n")

            elif esc_arma == 2:

                atk = random.randrange(1, 21)
                print(atk)

                dano = random.randrange(12, 17)
                crit_dano = dano*(3.5)

                if atk == 1:
                    print("ERROU")
                elif atk > 1 and atk < 13:
                    print("ACERTO NORMAL")
                    b1.atirar(dano, p1)
                    print(dano,"\n")
                elif atk > 12:
                    print("CRITOU")
                    b1.atirar(crit_dano, p1)
                    print(crit_dano,"\n")

        elif esc == 2:
            print("ARREGÃO")
            p2.fugir()

    if p1.vida >= 1 and p2.vida >= 1:
        return print("Vida de", p1.nome,":", p1.vida,"\nVida de", p2.nome,":",p2.vida)
    elif p2.vida <= 0:
        return print(p1.nome, "VENCEU !!!\n\nVida de", p1.nome,":", p1.vida, "\nVida de", p2.nome,": 0")
    elif p1.vida <= 0:
        return print(p2.nome, "VENCEU !!!\n\nVida de", p2.nome,":", p2.vida, "\nVida de", p1.nome,": 0")

# A arena funciona como um arquivo de teste, qualquer coisa que queira ser testada será feito aqui.

if __name__ == "__main__":

    dano = 5

    e1 = Espada(dano, "Lâmina de Aço")
    b1 = Besta(dano, "Visão Plena")    
    e2 = Espada(dano, "Espada de Treinamento")
    
    j1 = Jogador(50, dano, "Tadeu", 500)
    j2 = Jogador(50, dano, "Lineu", 3)   

    j1.inv_armas.append(e1)
    j1.inv_armas.append(b1)
    j1.inv_armas.append(e2)

    j2.inv_armas.append(e1)
    j2.inv_armas.append(b1)

    j1.criar_escolhas(j1)