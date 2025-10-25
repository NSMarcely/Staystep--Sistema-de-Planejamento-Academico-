from curso import Curso
from disciplina import Disciplina
from usuario import Usuario
class Gerenciador_Dados:
    def __init__(self):
        self.__cursos = []
        self.__usuarios = []
    def adicionar_curso(self, nome, semestres):
        encontrado = None
        for procura in self.__cursos:
            if procura.get_nome().lower() == nome.lower():
                encontrado = procura
                print(f"O curso '{procura.get_nome()}' já existe!")
                return False
        if not encontrado:
            curso = Curso(nome, semestres)
            self.__cursos.append(curso)
            print(f"O curso {nome}, foi adicionado com sucesso!")
            return True
        
    def remove_curso(self, nome):    
        encontrado = None
        for procura in self.__cursos:
            if procura.get_nome().lower() == nome.lower():
                encontrado = procura
                break
        if encontrado:
            self.__cursos.remove(encontrado)
            print("Curso removido com sucesso!")
            return True
        else:
            print("Não existe esse curso")
            return False

    def adicionar_disciplina_curso(self, nome_curso, nome_disciplina, horas, codigo, requisitos):
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
        if requisitos:
            for nome_req in requisitos:
                disciplina_req = None
                for d in encontrar_curso.get_disciplinas():
                    if d.get_nome().lower() == nome_req.lower():
                        disciplina_req = d
                        break
                if disciplina_req:
                    list_requisitos.append(disciplina_req)
                else:
                    print(f"A disciplina '{nome_req}' não existe no curso e não pode ser requisito.")
        #cria obj            
        disciplina = Disciplina(nome_disciplina, horas, codigo, requisitos=list_requisitos)
        encontrar_curso.adicionar_disciplina(disciplina)
        encontrar_curso.listar_disciplinas()

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
        for acha in encontra_curso.get_disciplinas():
            if acha.get_nome().lower() == nome_disciplina.lower():
                disciplina_encontrada = acha
                break
        if not disciplina_encontrada:
            print(f"A disciplina '{nome_disciplina}' não foi encontrada no curso '{nome_curso}'.")
            return    
        encontra_curso.get_disciplinas().remove(disciplina_encontrada)
        print(f"A disciplina '{nome_disciplina}' foi removida do curso '{nome_curso}' com sucesso!")

    def registrar_usuario(self, username, usersenha, usercurso):
        procura = None
        for acha in self.__usuarios:
            if acha.get_nome().lower() == username.lower():
                procura = acha
                print(f"O usuário '{acha.get_nome()}' já existe!") 
                return    
        if len(usersenha) < 10:
            print("Não é permitido menos que 10 caracteres")
            return
        else:
            #cria obj 
            usuario = Usuario(username, usersenha, usercurso)
            self.__usuarios.append(usuario) 
            print(f"Usuário '{username}' registrado com sucesso!")
    def logar_usuario(self, username, usersenha):
        procura = None
        for acha in self.__usuarios:
            if acha.get_nome().lower() == username.lower():
                procura = acha
                break
        if not procura:
            print("Esse usuário não existe")  
            return
        if   procura.get_senha() != usersenha:
            print("Senha incorreta")
            return
        else: 
            print(f"Bem-vindo(a) {procura.get_nome()} ao seu planner")    

    def obter_curso(self, nome_curso):
        for curso in self.__cursos:
            if curso.get_nome().lower() == nome_curso.lower():
                return curso 
        return None        
    
    




                 

