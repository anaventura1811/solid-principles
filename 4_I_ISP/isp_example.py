'''
    ISP (Interface Segregation Principle) ou
    Princípio da segregação de interface

    "depender de algo que contém itens desnecessários pode
    causar problemas inesperados"(p. 86)

    Uma classe não deve ser forçada a implementar
    interfaces que ela não utiliza.

    "Em vez disso, as interfaces devem ser segregadas em
    conjuntos menores e mais específicos de métodos"
'''


from abc import ABC, abstractmethod


class Document(ABC):

    @abstractmethod
    def load(self): pass

    # Exemplos de quebras do ISP
    # PDF
    # @abstractmethod
    # def view(self): pass

    # txt
    # @abstractmethod
    # def format(self): pass

    # excel
    # @abstractmethod
    # def calculate(self): pass


class DocumentPDF(ABC):  # ISP
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def view(self): pass


class DocumentTXT(ABC):  # ISP
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def format(self): pass


class DocumentExcel(ABC):  # ISP
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def calculate(self): pass
