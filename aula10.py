class Animal:
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return"Au Au!"
    
class Gato(Animal):
    def falar(self):
        return"Miau Miau!"
    

animais = [Cachorro(), Gato()]

for Animal in animais:
    print(Animal.falar())