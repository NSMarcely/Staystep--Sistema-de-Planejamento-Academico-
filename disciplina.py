class Disciplina:
    def __init__(self, nome: str, horas: int, codigo: str):
        self.__nome = nome
        self.__horas = horas 
        self.__codigo = codigo
    def get_nome(self):
        return self.__nome 
    def set_nome(self, nome):
        self.__nome = nome
    def get_nome(self):
        return self.__horas 
    def set_nome(self, horas):
        self.__horas = horas     
    def get_codigo(self):
        return self.__codigo 
    def set_nome(self, codigo):
        self.__codigo = codigo   
