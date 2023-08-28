from .enemy import Enemy

class Bear(Enemy):
    def __init__(self, vida, ataque, defesa, tipo, tipo_poder, velocidade, genero, idade):
        super().__init__(vida, ataque, defesa, tipo, tipo_poder, velocidade)
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.tipo = tipo
        self.tipo_poder = tipo_poder
        self.velocidade = velocidade
        self.genero = genero
        self.idade = idade

    def caçar(self):
        print('Caçando peixe')

    def hibernar(self):
        print('Hiberando na toca')