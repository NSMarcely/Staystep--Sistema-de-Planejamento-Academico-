class Curso:
    def __init__(self, nome: str,semestres):
        self.__nome = nome 
        self.__semestres = semestres
    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome = nome
    def get_semestres(self):
        return self.__semestres
    def set_semestres(self, semestres):
        self.__semestres = semestres      
    
