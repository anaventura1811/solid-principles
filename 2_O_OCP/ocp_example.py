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

company.do_work(seller)
company.do_work(programmer)
