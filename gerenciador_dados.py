from curso import Curso
from disciplina import Disciplina
from usuario import Usuario
import json

class Gerenciador_Dados:
    def __init__(self, arquivo="dados.json"):
        self.cursos: dict[str, Curso] = {}
        self.__usuarios: dict[str, Usuario] = {}
        self.arquivo = arquivo 
        self.carregar_dados()
    
    def adicionar_curso(self, nome, semestres):
        chave = nome.lower()
        if chave in self.cursos:
            print(f"\n|O curso '{nome}' já existe!")
            return False
        self.cursos[chave] = Curso(nome, semestres)
        print(f"\n|O curso '{nome}' foi adicionado com sucesso!")
        self.salvar_dados()
        return True
        
    def remove_curso(self, nome):
        chave = nome.lower()
        if chave in self.cursos:
            del self.cursos[chave]
            print(f"\n|Curso '{nome}' removido com sucesso!")
            self.salvar_dados()
            return True
        print(f"\n|Curso '{nome}' não existe.")
        return False

    def adicionar_disciplina_curso(self, nome_curso, nome_disciplina, horas, codigo, requisitos):
        encontrar_curso = None
        for curso in self.cursos.values():
            if curso.nome.lower() == nome_curso.lower():
                encontrar_curso = curso
                break
        if not encontrar_curso:
            print(f"\n|O curso '{nome_curso}' não foi encontrado")   
            return False
        
        try:
            horas = int(horas)
            if horas <= 0:
                print("\n|Horas devem ser um número positivo!")
                return False
        except ValueError:
            print("\n|Horas devem ser um número inteiro!")
            return False
            
        list_requisitos = []
        if requisitos:
            for nome_req in requisitos:
                disciplina_req = None
                for disciplina in encontrar_curso.disciplinas.values():
                    if disciplina.nome.lower() == nome_req.lower():
                        disciplina_req = disciplina
                        break
                if disciplina_req:
                    list_requisitos.append(disciplina_req)
                else:
                    print(f"\n|Aviso: Disciplina '{nome_req}' não existe e não será adicionada como requisito.")
        
        disciplina = Disciplina(nome_disciplina, horas, codigo, requisitos=list_requisitos)
        resultado = encontrar_curso.adicionar_disciplina(disciplina)
        if resultado:
            self.salvar_dados()
        return resultado

    def remove_disciplina_curso(self, nome_curso, nome_disciplina):
        encontra_curso = None
        for curso in self.cursos.values():
            if curso.nome.lower() == nome_curso.lower():
                encontra_curso = curso 
                break
        if not encontra_curso:
            print("\n|Curso não encontrado") 
            return False
            
        disciplina_encontrada = None
        for disciplina in encontra_curso.disciplinas.values():
            if disciplina.nome.lower() == nome_disciplina.lower():
                disciplina_encontrada = disciplina
                break
                
        if not disciplina_encontrada:
            print(f"\n|A disciplina '{nome_disciplina}' não foi encontrada no curso '{nome_curso}'.")
            return False    
            
        resultado = encontra_curso.remover_disciplina(disciplina_encontrada.codigo)
        if resultado:
            self.salvar_dados()
        return resultado

    def registrar_usuario(self, username, usersenha, usercurso):
        if username.lower() in self.__usuarios:
            print(f"\n|O usuário '{username}' já existe!") 
            return False
                
        if len(usersenha) < 10:
            print("\n|Não é permitido menos que 10 caracteres")
            return False
            
        if usercurso.lower() not in self.cursos:
            print(f"\n|O curso '{usercurso}' não existe!")
            return False
            
        usuario = Usuario(username, usersenha, usercurso, self)
        self.__usuarios[username.lower()] = usuario 
        print(f"\n|Usuário '{username}' registrado com sucesso!")
        self.salvar_dados()
        return True

    def logar_usuario(self, username, usersenha):
        usuario = self.__usuarios.get(username.lower())
        if not usuario:
            print("\n|Esse usuário não existe")  
            return None
        if usuario.get_senha() != usersenha:
            print("\n|Senha incorreta")
            return None
        print(f"\n|Bem-vindo(a) {usuario.get_nome()} ao seu planner\n")   
        return usuario

    def retorna_curso(self, nome_curso: str):
        return self.cursos.get(nome_curso.lower()) 

    def checa_disciplina_curso(self, nome_curso: str, nome_disciplina: str):
        curso = self.retorna_curso(nome_curso)
        if not curso:
            return False
        nome_disciplina_lower = nome_disciplina.lower()
        for disciplina in curso.disciplinas.values():
            if disciplina.nome.lower() == nome_disciplina_lower:
                return True
        return False
    
    def buscar_disciplina_por_nome(self, nome_curso: str, nome_disciplina: str):
        curso = self.retorna_curso(nome_curso)
        if not curso:
            return None
        nome_disciplina_lower = nome_disciplina.lower()
        for disciplina in curso.disciplinas.values():
            if disciplina.nome.lower() == nome_disciplina_lower:
                return disciplina
        return None

    def listar_cursos(self):
        if not self.cursos:
            print("\n|Nenhum curso cadastrado no sistema.")
            return
        print("\n___Cursos Cadastrados___")
        for curso in self.cursos.values():
            print(f"- {curso.nome} ({curso.semestres} semestres)")
        
    # Dados JSON
    def salvar_dados(self):
        try:
            dados = {
                "cursos": {
                    nome: curso.to_dict() 
                    for nome, curso in self.cursos.items()
                },
                "usuarios": {
                    username: usuario.to_dict()
                    for username, usuario in self.__usuarios.items()
                }
            }
            with open(self.arquivo, "w", encoding="utf-8") as f:
                json.dump(dados, f, ensure_ascii=False, indent=4)
            print("\n|Dados salvos com sucesso!")
            return True
        except Exception as e:
            print(f"\n|Erro ao salvar dados: {e}")
            return False
            
    def carregar_dados(self):
        try:
            with open(self.arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)
            cursos_dict = dados.get("cursos", {})
            cursos_carregados = {}
            for nome, curso_dados in cursos_dict.items():
                try:
                    curso = Curso.from_dict(curso_dados)
                    cursos_carregados[nome.lower()] = curso
                    print(f"|Curso carregado: {curso.nome} ({len(curso.disciplinas)} disciplinas)")
                except Exception as e:
                    print(f"|Erro ao carregar curso {nome}: {e}")
            usuarios_dict = dados.get("usuarios", {})
            usuarios_carregados = {}
            
            for username, usuario_dados in usuarios_dict.items():
                try:
                    usuario = Usuario.from_dict(usuario_dados, self)
                    usuarios_carregados[username.lower()] = usuario
                    print(f"|Usuário carregado: {usuario.get_nome()} (Curso: {usuario.get_curso()}, {len(usuario.metas)} metas, {len(usuario.disciplinas_cursadas)} cursadas, {len(usuario.disciplinas_cursando)} cursando)")
                except Exception as e:
                    print(f"|Erro ao carregar usuário {username}: {e}")
            self.cursos = cursos_carregados
            self.__usuarios = usuarios_carregados
            print("|Dados carregados com sucesso!")
        except FileNotFoundError:
            print("|Arquivo de dados não encontrado. Começando com dados vazios.")
        except json.JSONDecodeError as e:
            print(f"|Erro ao decodificar JSON: {e}")
        except Exception as e:
            print(f"|Erro ao carregar dados: {e}")

    def listar_usuarios(self):
        if not self.__usuarios:
            print("\n|Nenhum usuário cadastrado.")
            return
        print("\n___Usuários Cadastrados___")
        for usuario in self.__usuarios.values():
            print(f"- {usuario.get_nome()} (Curso: {usuario.get_curso()})")