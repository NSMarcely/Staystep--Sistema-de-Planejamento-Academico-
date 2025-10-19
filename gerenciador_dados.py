from curso import Curso

class Gerenciador_Dados:
    def __init__(self):
        self.__cursos = []
    def adicionar_curso(self, nome, semestres):
        curso = Curso(nome, semestres) 
        self.__cursos.append(curso)
    def remove_curso(self, nome):    
        encontrado = "não"
        for procura in self.__cursos:
            if procura.get_nome.lower() == nome.lower():
                encontrado = procura
        if encontrado == "sim":
            self.__cursos.remove(procura)
            print("Curso removido com sucesso!")
        else:
            print("Não existe esse curso")
