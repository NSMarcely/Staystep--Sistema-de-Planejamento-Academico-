from gerenciador_dados import Gerenciador_Dados
from usuario import Usuario
from adm import Adm

class Main:
    def __init__(self):
        self.gerenciador = Gerenciador_Dados()
        self.usuario_logado = None
    
    def menu_principal(self):
        while True:
            print("_"*50)
            print("|Staystep - Planner academico|")
            print("""\n1. Login de Usuário
2. Registrar Usuário
3. Login de Administrador
4. Sair""")
            print("_"*50)
            opcao = input("Escolha uma opção: ").strip()
            if opcao == "1":
                self.login_usuario()
            elif opcao == "2":
                self.registrar_usuario()
            elif opcao == "3":
                self.login_adm()
            elif opcao == "4":
                print("\n|Saindo do sistema...")
                break
            else:
                print("\n|Opção inválida! Tente novamente.")
    
    def registrar_usuario(self):
        print("\n___Cadastrar Usuáro___")
        username = input("Nome de usuário: ").strip()
        if not username:
            print("\n|Nome de usuário não pode estar vazio!")
            return
        usersenha = input("\n|Senha (mínimo 10 caracteres): ").strip()
        if not self.gerenciador.cursos:
            print("\n|Não há cursos cadastrados no sistema!")
            return
        print("\nCursos disponíveis:")
        for nome_curso in self.gerenciador.cursos.keys():
            print(f"- {nome_curso}")
        usercurso = input("Curso: ").strip()
        if not usercurso:
            print("\n|Curso não pode estar vazio!")
            return
        # Usa o método que você já tem no gerenciador
        self.gerenciador.registrar_usuario(username, usersenha, usercurso)
    
    def login_usuario(self):
        print("\n__Login do Usuário__") 
        username = input("Nome de usuário: ").strip()
        usersenha = input("Senha: ").strip()
        # Usa o método que tem no gerenciador
        usuario = self.gerenciador.logar_usuario(username, usersenha)
        if usuario:
            self.usuario_logado = usuario
            self.menu_usuario()
    
    def login_adm(self):
        print("\n__Login do Adm__")
        username = input("Nome de administrador: ").strip()
        usersenha = input("Senha: ").strip()
        if username == "Cely" and usersenha == "1234":
            administrador = Adm("Cely", "1234", self.gerenciador)
            print(f"\nBem-vindo(a), Administrador!")
            self.menu_adm(administrador)
        else:
            print("\n|Credenciais de administrador inválidas!")
    
    def menu_usuario(self):
        if not self.usuario_logado:
            return
        self.usuario_logado.rodar_comandos()
        self.usuario_logado = None  
    
    def menu_adm(self, administrador):
        administrador.rodar_comandos()

    def executar(self):
        print("\n|Inicializando Staystep - Planner academico...")
        self.menu_principal()

if __name__ == "__main__":
    sistema = Main()
    sistema.executar()