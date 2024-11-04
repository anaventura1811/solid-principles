'''
    Classes criadas como exemplos de aplicação do
    Princípio aberto/fechado ou
    OCP (Open/Closed Principle)

    "Um artefato de software deve ser aberto para extensão,
    mas fechado para modificação" (p. 70)

    "Uma boa arquitetura de software deve reduzir a quantidade
    de código a ser mudado para o mínimo possível(...)
    Primeiro, devemos separar adequadamente as coisas que mudam por
    razões diferentes (o Princípio da Responsabilidade Única) para, então,
    organizarmos as dependências entre essas coisas de forma apropriada
    (o Princípio da Inversão de Dependência)"(p. 71)

'''


class Programmer:
    def make(self):
        print("Programmer is coding")


class Seller:
    def make(self):
        print("Seller is selling the product")


class HumanResources:
    def make(self):
        print("Human Resources hiring new devs")


class Frontend:
    def make(self):
        print("Frontend raising bugs for production")


class Company:
    def do_work(self, worker: any) -> None:
        worker.make()


company = Company()
seller = Seller()
programmer = Programmer()
rh = HumanResources()

company.do_work(seller)
company.do_work(programmer)
company.do_work(rh)
