# Classe principal de qualquer criatura.

class Mob:
    vida : int
    dano : int

    def __init__(self, vida, dano):
        self.vida = vida
        self.dano = dano

    def bater(self, dano, Mob):
        Mob.vida -= dano

    def fugir(self):
        return 0