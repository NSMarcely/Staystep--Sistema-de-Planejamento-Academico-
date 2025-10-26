from curso import Curso
from disciplina import Disciplina

class Gerenciador_Dados:
    def __init__(self):
        self.cursos = {}
        self.__usuarios = {}
    
    def adicionar_curso(self, nome, semestres):
        chave = nome.lower()
        if chave in self.cursos:
            print(f"\n|O curso '{nome}' já existe!")
            return False
        self.cursos[chave] = Curso(nome, semestres)
        print(f"\n|O curso '{nome}' foi adicionado com sucesso!")
        return True
        
    def remove_curso(self, nome):
        chave = nome.lower()
        if chave in self.cursos:
            del self.cursos[chave]
            print(f"\n|Curso '{nome}' removido com sucesso!")
            return True
        print(f"\n|Curso '{nome}' não existe.")
        return False

    def adicionar_disciplina_curso(self, nome_curso, nome_disciplina, horas, codigo, requisitos):
        encontrar_curso = None
        for acha in self.cursos.values():
            if acha.nome.lower() == nome_curso.lower():
                encontrar_curso = acha
                break
        if not encontrar_curso:
            print(f"\n|O curso '{nome_curso}' não foi encontrado")   
            return
        
        list_requisitos = []
        if requisitos:
            for nome_req in requisitos:
                disciplina_req = None
                for d in encontrar_curso.disciplinas.values():
                    if d.nome.lower() == nome_req.lower():
                        disciplina_req = d
                        break
                if disciplina_req:
                    list_requisitos.append(disciplina_req)
                else:
                    print(f"\n|A disciplina '{nome_req}' não existe no curso e não pode ser requisito.")
        
        disciplina = Disciplina(nome_disciplina, horas, codigo, requisitos=list_requisitos)
        encontrar_curso.adicionar_disciplina(disciplina)
        encontrar_curso.listar_disciplinas()

    def remove_disciplina_curso(self, nome_curso, nome_disciplina):
        encontra_curso = None
        for acha in self.cursos.values():
            if acha.nome.lower() == nome_curso.lower():
                encontra_curso = acha 
                break
        if not encontra_curso:
            print("\n|Curso não encontrado") 
            return
        
        disciplina_encontrada = None
        for disciplina in encontra_curso.disciplinas.values():
            if disciplina.nome.lower() == nome_disciplina.lower():
                disciplina_encontrada = disciplina
                break
    
        if not disciplina_encontrada:
            print(f"\n|A disciplina '{nome_disciplina}' não foi encontrada no curso '{nome_curso}'.")
            return    
        encontra_curso.remover_disciplina(disciplina_encontrada.codigo)

    def registrar_usuario(self, username, usersenha, usercurso):
        from usuario import Usuario
        procura = None
        for acha in self.__usuarios.values():
            if acha.get_nome().lower() == username.lower():
                procura = acha
                print(f"\n|O usuário '{acha.get_nome()}' já existe!") 
                return    
        if len(usersenha) < 10:
            print("\n|Não é permitido menos que 10 caracteres")
            return
        else:
            usuario = Usuario(username, usersenha, usercurso, self)
            self.__usuarios[username.lower()] = usuario 
            print(f"\n|Usuário '{username}' registrado com sucesso!")

    def logar_usuario(self, username, usersenha):
        procura = None
        for acha in self.__usuarios.values():
            if acha.get_nome().lower() == username.lower():
                procura = acha
                break
        if not procura:
            print("\n|Esse usuário não existe")  
            return None
        if procura.get_senha() != usersenha:
            print("\n|Senha incorreta")
            return None
        else: 
            print(f"\n|Bem-vindo(a) {procura.get_nome()} ao seu planner")   
            return procura

    def retorna_curso(self, nome_curso: str):
        chave = nome_curso.lower()
        return self.cursos.get(chave) 

    def checa_disciplina_curso(self, nome_curso: str, nome_disciplina: str):
        curso = self.retorna_curso(nome_curso)
        if not curso:
            return False
        chave_disciplina = nome_disciplina.lower()
        for disciplina in curso.disciplinas.values():
            if disciplina.nome.lower() == chave_disciplina:
                return True
        return False
    
    def buscar_disciplina_por_nome(self, nome_curso: str, nome_disciplina: str):
        curso = self.retorna_curso(nome_curso)
        if not curso:
            return None
        chave_disciplina = nome_disciplina.lower()
        for disciplina in curso.disciplinas.values():
            if disciplina.nome.lower() == chave_disciplina:
                return disciplina
        return None