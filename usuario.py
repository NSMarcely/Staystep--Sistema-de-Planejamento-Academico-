from pessoa import Pessoa
from metas import Metas
class Usuario(Pessoa):
    def __init__(self, nome: str, senha: str, curso: str, metas = None):
        super().__init__(nome,senha)
        self.__curso = curso 
        self.__metas = metas if metas else []
        self.__disciplinas_cursadas = []
    def get_curso(self):
        return self.__curso
    def get_metas(self):
        return self.__metas
    def set_metas(self, metas):
        self.__metas = metas
    def get_disciplinas_cursadas(self):
        return self.__disciplinas_cursadas
    def set_disciplina_cursadas(self, disciplinas_cursadas):
        self.__disciplinas_cursadas = disciplinas_cursadas 

    def adicionar_metas(self, metas: Metas):
        encontra = None  
        for acha in self.__metas:
            if acha.get_texto().lower() == metas.get_texto().lower():
                print(f"A meta '{metas.get_texto()}' já exite!")
                return
        self.__metas.append(metas)
            