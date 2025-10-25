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
    def set_disciplinas(self, disciplinas):
        self.__disciplinas = disciplinas 
    def __str__(self):
        return self.__nome
    
    #add o objeto criado em gd na lista disciplinas
    def adicionar_disciplina(self,disciplina: Disciplina):
        for checa in self.__disciplinas:
            if checa.get_nome().lower() == disciplina.get_nome().lower():
                print("Já existe essa disciplina")
                return
        self.__disciplinas.append(disciplina)
        print(f"Disciplina {disciplina.get_nome()} foi adicionada com sucesso!")

    def listar_disciplinas(self):
        print("\nDisciplinas atuais do curso:")
        if not self.__disciplinas:
            print(f"O curso {self.__nome} ainda não possui disciplinas.")
            return
        print(f"Disciplinas do curso {self.__nome}:")
        for disciplina in self.__disciplinas:
            print(f"- {disciplina.get_nome()} (Código: {disciplina.get_codigo()}, {disciplina.get_horas()}h)")
    
                


