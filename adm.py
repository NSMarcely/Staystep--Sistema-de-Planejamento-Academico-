from pessoa import Pessoa
from gerenciador_dados import Gerenciador_Dados
class Adm(Pessoa):
    def __init__(self, nome: str, senha: str, gerencia: Gerenciador_Dados):
        super().__init__(nome, senha)
        self.__gerencia = gerencia  
    def get_gerencia(self):
        return self.__gerencia 
    def adicionar_disciplina(self):
        nome_curso = input("Curso da disciplina: ").strip()
        nome_disciplina = input("Nome da disciplina: ").strip()
        erro = True
        horas = None
        while horas is None:
            horas_input = input("Horas da disciplina: ").strip()
            if horas_input.isdigit(): 
                horas = int(horas_input)
                if horas > 0:
                    break 
                else:
                    print("As horas devem ser um número positivo!")
                    horas = None
            else:
                print("As horas devem ser um número inteiro!")

        codigo = input("Código da disciplina: ").strip()  
        requisitos = input("Requisitos (separados por vírgula, vazio se não tiver): ").strip()
        if not requisitos:
            requisitos_lista = []
        else:
            requisitos_lista = [r.strip() for r in requisitos.split(",")]
        self.__gerencia.adicionar_disciplina_curso(nome_curso, nome_disciplina, horas, codigo, requisitos_lista)   

    def remover_disciplina(self):
        nome_curso = input("Curso da disciplina: ").strip()
        nome_disciplina = input("Nome da disciplina a remover: ").strip()
        self.__gerencia.remove_disciplina_curso(nome_curso, nome_disciplina)    
    
    def adicionar_curso(self):
        nome = input("Nome do Curso: ").strip()
        while True:
            semestres_input = input("Quantidade de semestres: ").strip()
            if semestres_input.isdigit():
                semestres = int(semestres_input)
                if semestres > 0:
                    break
                else:
                    print("Os semestres devem ser um número positivo!")
            else:
                print("Os semestres devem ser um número inteiro!")
        
        self.__gerencia.adicionar_curso(nome, semestres)       
    
    def remover_curso(self):
        nome = input("Nome do curso: ").strip()
        self.__gerencia.remove_curso(nome)      

    #obrigado 
    def rodar_comandos(self):
        x = True 
        while x:
            print("__________Modo Administrador__________")
            print("""1- Adicionar disciplina
2- Remover disciplinas
3- Adicionar curso
4- Remover curso
5- Sair""")
            opcao = input("Opção escolhida: ").strip()
            
            if opcao == "1":
                self.adicionar_disciplina()
            elif opcao == "2":
                self.remover_disciplina()
            elif opcao == "3":
                self.adicionar_curso()
            elif opcao == "4":
                self.remover_curso()
            elif opcao == "5":
                print("Saindo do modo administrador...")  
                break  
            else:
                print("Opção inválida, por favor tente novamente :(")
