'''
    DIP (Dependency Inversion Principle) ou
    Princípio da Inversão de Dependência

    Módulos de alto nível não devem depender
    diretamente dos módulos de baixo nível

    "Segundo o Princípio da Inversão da Dependência (DIP), os sistemas
    mais flexíveis são aqueles em que as dependências do código-fonte
    se referem apenas a abstrações e não a itens concretos" (p. 87)

    Módulo concreto pode ser definido como
    "qualquer módulo em que as funções chamadas são implementadas" (p. 88)

    "Queremos evitar depender dos elementos concretos voláteis
    do nosso sistema. Esses são os módulos que estamos desenvolvendo
    ativamente e que passam por mudanças frequentes" (p. 88)

    "as arquiteturas de software estáveis são aquelas que evitam depender
    de implementações concretas, e que favorecem o uso de interfaces abstratas
    e estáveis. Essa implicação pode ser sintetizada em um conjunto de
    práticas de programação muito específicas:
      1. Não se refira a classes concretas voláteis.(...)
      Refira-se a interfaces abstratas.(...)
      2. Não derive de classes concretas voláteis.(...)
      3. Não sobrescreva funções concretas.(...)
      4. Nunca mencione o nome de algo que seja concreto e volátil.(...)
    " (p. 89)

    --> Uso de fábricas (factories) e interfaces para lidar com
    as dependências indesejadas.

    "As violações do DIP não podem ser removidas completamente, mas é possível
    reuni-las em um número menor de componentes concretos para que fiquem
    separadas do resto do sistema" (p. 91)
'''


from .notificator_interface import NotificatorInterface


# Módulo de alto nível
class ClientService:
    def __init__(self, notificator: NotificatorInterface) -> None:
        self.notificator = notificator

    def send(self, message: str) -> None:
        self.notificator.send_notification(message)
