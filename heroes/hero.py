class Hero:
    def __init__(self, vida, defesa, ataque, velocidade):
        self.vida = vida
        self.defesa = defesa
        self.ataque = ataque
        self.velocidade = velocidade

    def atacar(self, enemy):
        print('Atacando com a espada')
        enemy.vida = enemy.vida - self.ataque

    def correr(self):
        print('Correndo rápido')

    def equipar(self):
        print('Equipando espada')

    
    