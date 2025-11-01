from pessoa import Pessoa
from gerenciador_dados import Gerenciador_Dados

class Adm(Pessoa):
    def __init__(self, nome: str, senha: str, gerencia: Gerenciador_Dados):
        super().__init__(nome, senha)
        self.__gerencia = gerencia  
    
    def get_gerencia(self):
        return self.__gerencia 
    
    def adicionar_disciplina(self):
        print("\n___Adicionar Disciplina___")
        nome_curso = input("Curso da disciplina: ").strip()
        if not nome_curso:
            print("\n|Nome do curso não pode estar vazio!")
            return
            
        nome_disciplina = input("Nome da disciplina: ").strip()
        if not nome_disciplina:
            print("\n|Nome da disciplina não pode estar vazio!")
            return
            
        horas = None
        while horas is None:
            horas_input = input("Horas da disciplina: ").strip()
            if horas_input.isdigit(): 
                horas = int(horas_input)
                if horas > 0:
                    break 
                else:
                    print("\n|As horas devem ser um número positivo!")
                    horas = None
            else:
                print("\n|As horas devem ser um número inteiro!")

        codigo = input("Código da disciplina: ").strip()
        if not codigo:
            print("\n|Código da disciplina não pode estar vazio!")
            return
            
        requisitos = input("Requisitos (separados por vírgula, vazio se não tiver): ").strip()
        if not requisitos:
            requisitos_lista = []
        else:
            requisitos_lista = [r.strip() for r in requisitos.split(",")]
            
        # Chama o método do gerenciador e salva se foi bem-sucedido
        if self.__gerencia.adicionar_disciplina_curso(nome_curso, nome_disciplina, horas, codigo, requisitos_lista):
            self.__gerencia.salvar_dados()  # Salva após adicionar disciplina
    
    def remover_disciplina(self):
        print("\n___Remover Disciplina___")
        nome_curso = input("Curso da disciplina: ").strip()
        if not nome_curso:
            print("\n|Nome do curso não pode estar vazio!")
            return
            
        nome_disciplina = input("Nome da disciplina a remover: ").strip()
        if not nome_disciplina:
            print("\n|Nome da disciplina não pode estar vazio!")
            return
            
        # Chama o método do gerenciador e salva se foi bem-sucedido
        if self.__gerencia.remove_disciplina_curso(nome_curso, nome_disciplina):
            self.__gerencia.salvar_dados()  # Salva após remover disciplina
    
    def adicionar_curso(self):
        print("\n___Adicionar Curso___")
        nome = input("Nome do Curso: ").strip()
        if not nome:
            print("\n|Nome do curso não pode estar vazio!")
            return
            
        while True:
            semestres_input = input("Quantidade de semestres: ").strip()
            if semestres_input.isdigit():
                semestres = int(semestres_input)
                if semestres > 0:
                    break
                else:
                    print("\n|Os semestres devem ser um número positivo!")
            else:
                print("\n|Os semestres devem ser um número inteiro!")
        
        # Chama o método do gerenciador e salva se foi bem-sucedido
        if self.__gerencia.adicionar_curso(nome, semestres):
            self.__gerencia.salvar_dados()  # Salva após adicionar curso
    
    def remover_curso(self):
        print("\n___Remover Curso___")
        nome = input("Nome do curso: ").strip()
        if not nome:
            print("\n|Nome do curso não pode estar vazio!")
            return
            
        # Chama o método do gerenciador e salva se foi bem-sucedido
        if self.__gerencia.remove_curso(nome):
            self.__gerencia.salvar_dados()  # Salva após remover curso

    def listar_cursos(self):
        """Método adicional para listar cursos existentes"""
        print("\n___Cursos Cadastrados___")
        if not self.__gerencia.cursos:
            print("|Nenhum curso cadastrado|")
            return
            
        for curso in self.__gerencia.cursos.values():
            print(f"- {curso.nome} ({curso.semestres} semestres)")
            if curso.disciplinas:
                print(f"  Disciplinas: {len(curso.disciplinas)}")
            else:
                print("  Disciplinas: Nenhuma")

    def rodar_comandos(self):
        while True:
            print("\n" + "="*50)
            print("__________Modo Administrador__________")
            print("="*50)
            
            print("""\n1- Adicionar disciplina
2- Remover disciplina
3- Adicionar curso
4- Remover curso
5- Listar cursos
6- Sair""")
            
            opcao = input("\nOpção escolhida: ").strip()
            
            if opcao == "1":
                self.adicionar_disciplina()
            elif opcao == "2":
                self.remover_disciplina()
            elif opcao == "3":
                self.adicionar_curso()
            elif opcao == "4":
                self.remover_curso()
            elif opcao == "5":
                self.listar_cursos()
            elif opcao == "6":
                print("\n|Saindo do modo administrador...")
                self.__gerencia.salvar_dados()  # Salva antes de sair
                break  
            else:
                print("\n|Opção inválida, por favor tente novamente :(")