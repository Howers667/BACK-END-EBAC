# Uma classe é um molde 
# Vamos usar esse molde para construir coisas que queremos que tem um mesmo padrão

# - Hp
# - Tipo do meu pokemon (elétrico, fogo, agua, gelo,.....)
# - Quais ataques ele tem (Choque do trovão)
# - Altura
# - Peso
# - Nome

#  Nome => Pikachu
# HP => 300
# Tipo => Eletrico
# Ataque => Choque do trovão
# Altura => 50cm
# Peso => 15kg


# Nome => Charizard
# HP => 450
# Tipo => Fogo
# Ataque => Lança chamas
# Altura => 2m
# Peso => 1500 kg

class MoldePokemon:
    # Método construtor
    # Self tem a responsabilidade de armazenar e manipular essas informações dos atributos
    def __init__(self, nome, hp, tipo, ataque, altura, peso):
        self.nome = nome
        self.hp = hp
        self.tipo = tipo
        self.ataque = ataque
        self.altura = altura
        self.peso = peso

    def mostrar_nome_pokemon(self, nome_pokemon):
        pass

    def mostrar_altura_pokemon(self):
        pass

    def mostrar_peso_pokemon(self):
        pass
