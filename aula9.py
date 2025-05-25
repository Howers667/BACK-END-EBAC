class Animal:
    def __init__(self,nome):
        self.nome = nome

    def comer(self):
        print(f"{self.nome} esta comendo")


class Cachorro(Animal):
    def latir(self):
        print(f"{self.nome} esta latindo: auau, auau")

meu_cachorro = Cachorro("Goku")

meu_cachorro.comer()
meu_cachorro.latir()