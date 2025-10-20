from curso import Curso
from disciplina import Disciplina
class Gerenciador_Dados:
    def __init__(self):
        self.__cursos = []
    def adicionar_curso(self, nome, semestres):
        encontrado = None
        for procura in self.__cursos:
            if procura.get_nome().lower() == nome.lower():
                encontrado = procura
                print(f"O curso '{encontrado}' já exite!")
                return
        if not encontrado:
            curso = Curso(nome, semestres)
            self.__cursos.append(curso)

        print(f"O curso {nome}, foi adicionado com sucesso!")
    def remove_curso(self, nome):    
        encontrado = None
        for procura in self.__cursos:
            if procura.get_nome().lower() == nome.lower():
                encontrado = procura
                break
        if encontrado:
            self.__cursos.remove(encontrado)
            print("Curso removido com sucesso!")
        else:
            print("Não existe esse curso")

    def adicionar_disciplina_curso(self, nome_curso, nome_disciplina, horas, codigo, nomes_requisitos):
        #fazer futaramente um metodo para não ficar repetindo codigo pra encontrar algum dado. dá até pra fazer poli!
        encontrar_curso = None
        for acha in self.__cursos:
            if acha.get_nome().lower() == nome_curso.lower():
                encontrar_curso = acha
                break
        if not encontrar_curso:
            print(f"O curso '{nome_curso}' não foi encontrado")   
            return
        list_requisitos = []
        if nomes_requisitos:
            for nome_req in nomes_requisitos:
                disciplina_req = None
                for d in encontrar_curso.get_disciplinas():
                    if d.get_nome().lower() == nome_req.lower():
                        disciplina_req = d
                        break
                if disciplina_req:
                    list_requisitos.append(disciplina_req)
                else:
                    print(f"A disciplina '{nome_req}' não existe no curso e não pode ser requisito.")
        disciplina = Disciplina(nome_disciplina, horas, codigo, requisitos=list_requisitos)
        encontrar_curso.adicionar_disciplina(disciplina)

    def remove_disciplina_curso(self, nome_curso, nome_disciplina):
        encontra_curso = None
        for acha in self.__cursos:
            if acha.get_nome().lower() == nome_curso.lower():
                encontra_curso = acha 
                break
        if not encontra_curso:
            print("Curso não encontrado") 
            return
        disciplina_encontrada = None
        for disciplina in encontra_curso.get_disciplinas():
            if disciplina.get_nome().lower() == nome_disciplina.lower():
                disciplina_encontrada = disciplina
                break
        if not disciplina_encontrada:
            print(f"A disciplina '{nome_disciplina}' não foi encontrada no curso '{nome_curso}'.")
            return    
        encontra_curso.get_disciplinas().remove(disciplina_encontrada)
        print(f"A disciplina '{nome_disciplina}' foi removida do curso '{nome_curso}' com sucesso!")


                 

