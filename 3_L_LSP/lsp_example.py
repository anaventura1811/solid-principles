'''
    LSP (Liskov Substitution Principle) - Princípio da substituição de Liskov
    LISKOV, Barbara (1988):
    "O que queremos aqui é algo como a seguinte propriedade de
    substituição: se, para cada objeto o1 de tipo S, houver um objeto
    o2 de tipo T, de modo que, para todos os programas P definidos
    em termos de T, o comportamento de P não seja modificado quando
    o1 for substituído por o2, então S é um subtipo de T" (p. 78)

    Entendendo tipos e subtipos no OOP:
        No exemplo abaixo, a Classe Animal é um tipo. Ou seja, é
        uma classe mais genérica. A Classe Felino vai herdar de Animal e,
        consequentemente, vai implementar (ou estender) métodos,
        sendo, portanto, um subtipo da Classe Animal.
        A herança seguirá um fluxo de classe mais genérica
        para mais específica. As classes mais específicas ganham
        mais atributos, no entanto isto se dá sem alterar os métodos genéricos.

    "O LSP pode, e deve, ser estendido ao nível da arquitetura.
    Uma simples violação da capacidade de substituição pode
    contaminar a arquitetura do sistema com uma quantidade
    significante de mecanismos extras." (p. 82)

'''


class Animal:
    def comer(self):
        print("O animal está comendo")

    def andar(self):
        print("O animal está andando na jaula")


class Felino(Animal):
    # Quebra do princípio de Liskov
    # def comer(self):
    # print("O felino come sua ração")

    def lamber(self):
        print("O felino está lambendo seu pelo")


class Leao(Felino):
    def rugir(self):
        print("O leão está rugindo alto")


class Pessoa:
    def observa(self, animal: Animal):
        animal.comer()


animal = Animal()
felino = Felino()
pessoa = Pessoa()

animal.comer()
felino.comer()
pessoa.observa(felino)
