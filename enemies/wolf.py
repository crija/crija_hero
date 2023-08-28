from .enemy import Enemy

class Wolf(Enemy):
    def __init__(self, vida, ataque, defesa, tipo, tipo_poder, velocidade,  cor, tamanho, adulto):
        super().__init__(vida, ataque, defesa, tipo, tipo_poder, velocidade)
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.tipo = tipo
        self.tipo_poder = tipo_poder
        self.velocidade = velocidade
        self.cor = cor
        self.tamanho = tamanho
        self.adulto = adulto

    def fugir(self):
        print('Fugindo com o rabo entre as pernas')

    def esconder(self):
        print('Escondendo no arbusto')