class Disciplina:
    def __init__(self, nome: str, horas: int, codigo: str, requisitos = None):
        self.__nome = nome
        self.__horas = horas 
        self.__codigo = codigo 
        self.__requisitos = requisitos if requisitos else []

    def get_nome(self):
        return self.__nome 
    def set_nome(self, nome):
        self.__nome = nome
    def get_horas(self):
        return self.__horas 
    def set_horas(self, horas):
        self.__horas = horas     
    def get_codigo(self):
        return self.__codigo 
    def set_codigo(self, codigo):
        self.__codigo = codigo 
    def get_requisitos(self):
        return self.__requisitos
    def set_requisitos(self, requisitos):
        self.__requisitos = requisitos      
    