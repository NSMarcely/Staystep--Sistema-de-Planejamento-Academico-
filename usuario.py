from pessoa import Pessoa

class Usuario(Pessoa):
    def __init__(self, nome: str, senha: str, matricula: int, curso: str):
        super().__init__(nome,senha)
        self.__matricula = matricula 
        self.__curso = curso 
    def get_matricula(self):
        return self.__matricula
    def get_curso(self):
        return self.__curso
    def selecionar_curso(self):
        pass
    def mostrar_cursos(self):
        pass