class Enemy:
    def __init__(self, vida, ataque, defesa, tipo, tipo_poder, velocidade):
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.tipo = tipo
        self.tipo_poder = tipo_poder
        self.velocidade = velocidade

    def atacar(self, entity):
        print('Atacando')
        entity.vida = entity.vida - self.ataque

    def correr(self, ):
        print('Correndo')

    def perseguir(self, entity):
        print('Perseguindo')


    
