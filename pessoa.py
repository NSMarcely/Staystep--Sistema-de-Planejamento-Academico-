class Pessoa:
    def __init__(self, nome: str, matricula: str, senha: str):
        self.__nome = nome
        self.__matricula = matricula
        self.__senha = senha

    def __str__(self):
        return f"{self.__nome} ({self.__matricula})"