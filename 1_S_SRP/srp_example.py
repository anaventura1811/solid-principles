'''
    Classe criada como exemplo de aplicação do
    Princípio da responsabilidade única ou
    SRP (Single Responsibility Principle)

    "Um módulo deve ser responsável por um, e apenas um, ator" (p. 62)

    Módulo é definido como arquivo fonte ou
    "conjunto coeso de funções e estruturas de dados"

'''


class Process:
    def handle(self, username: str, password: str) -> None:
        if self.__verify_input_data(username, password):
            self.__verify_input_in_database(username)
            self.__insert_new_user(username, password)
        else:
            self.__raise_error('Dados inválidos')

    def __verify_input_data(self, username: str, password: str) -> bool:
        return isinstance(username, str) and isinstance(password)

    def __verify_input_in_database(self, username: str) -> None:
        print('Acessando o banco de dados...')
        print('Verificando a existência do usuário...')

    def __insert_new_user(self, username: str, password: str) -> None:
        print('Cadastro de usuário realizado com sucesso!')

    def __raise_error(self, message: str) -> Exception:
        raise Exception(message)
