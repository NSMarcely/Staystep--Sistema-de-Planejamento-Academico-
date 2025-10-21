from pessoa import Pessoa
from metas import Metas
class Usuario(Pessoa):
    def __init__(self, nome: str, senha: str, matricula: int, curso: str, metas = None):
        super().__init__(nome,senha)
        self.__matricula = matricula 
        self.__curso = curso 
        self.__metas = metas if metas else []
    def get_matricula(self):
        return self.__matricula
    def get_curso(self):
        return self.__curso
    def get_metas(self):
        return self.__metas
    def set_metas(self, metas):
        self.__metas = metas
    def adicionar_metas(self, metas: Metas):
        encontra = None  
        for acha in self.__metas:
            if acha.get_texto().lower() == metas.get_texto().lower():
                print(f"A meta '{metas.get_texto()}' já exite!")
                return
        self.__metas.append(metas)
            