# Molde do pokemon

# Vamos ter varius atributos

class MoldelPokemon:
    def __init__(self, nome, altura, peso, hp, ataque, tipo):

        self.nome = nome
        self.altura = altura
        self.peso = peso
        self.hp = hp
        self.ataque = ataque
        self.tipo = tipo

    def mostrar_nome_pokemon(self):
        print(f"O nome do pokemon é: {self.nome}")

    def mostrar_altura_pokemon(self):
        print(f"A altura do pokemon é: {self.altura}")

    def mostrar_peso_pokemon(self):
        print(f"O peso do pokemon é: {self.peso}")


pikachu = MoldelPokemon("Pikachu", 50, 15, 400, "Choque do trovao", "eletrico")
charizard = MoldelPokemon("Charizard", 200, 1500, 500, "Lanca chamas", "Fogo")
miau = MoldelPokemon("Miau", 50, 15, 100, "Unhada", "Generalista" )


pikachu.mostrar_nome_pokemon()
charizard.mostrar_nome_pokemon()
miau.mostrar_nome_pokemon()