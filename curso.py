from disciplina import Disciplina 
class Curso:
    def __init__(self, nome: str,semestres):
        self.__nome = nome 
        self.__semestres = semestres
        self.__disciplinas = []
    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome = nome
    def get_semestres(self):
        return self.__semestres
    def set_semestres(self, semestres):
        self.__semestres = semestres      
    def get_disciplinas(self):
        return self.__disciplinas
    def set_diciplinas(self, diciplinas):
        self.__disciplinas = diciplinas 
    #add o objeto criado em gd na lista disciplinas
    def adicionar_disciplina(self,disciplina: Disciplina):
        tem = None
        for checa in self.__disciplinas:
            if checa.get_nome().lower() == disciplina.get_nome().lower():
                print("Já exite essa disciplina")
                return
              
        self.__disciplinas.append(disciplina)
        print(f"Disciplina {disciplina.get_nome()} foi adiciona com sucesso!")
                


