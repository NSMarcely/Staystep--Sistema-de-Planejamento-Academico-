from pessoa import Pessoa
from gerenciador_dados import Gerenciador_Dados
class Adm(Pessoa):
    def __init__(self, nome: str, senha: str,gerencia, codigo_verificacao: str = "Mf2412"):
        super().__init__(nome, senha)
        self.__codigo_verificacao = codigo_verificacao
        self.__gerencia = gerencia

    def get_codigo_verificacao(self):
        return self.__codigo_verificacao   
    def get_gerencia(self):
        return self.__gerencia 

    def verica_codigo(self): 
       for x in range(3):
           tentativa = input("\nDigite o código:")
           if tentativa == self.__codigo_verificacao:
              print(f"Bem-vindo(a), {self.get_nome()} ao modo administrador")
              break
           else:
              print("\nCódigo inválido!")
              print(f"Você só tem {3-x} chance(s) restantes")

    def rodar_comandos(self):
        x = True 
        while x:
            print("__________Modo Usuário__________")
            print("""1- Adcionar disciplina
    2- Remover disciplins
    3- Adicionar curso
    4- Remover curso
    5- Sair""")
            y = True 
            opcao = input("Opção escolhida:")
            if opcao == "1":
                pass
            elif opcao == "2":
                pass
            elif opcao == "3":
                nome = input("Nome do Curso:")
                semestres = input("Quantidade de semestres:")
                self.__gerencia.adicionar_curso(nome, semestres)
            elif opcao == "4":
                nome = input("Nome do curso:")
                self.__gerencia.remove_cursos(nome)
            elif opcao == "5":
                print("Saindo do modo administrador...")  
                x = False  
            else:
                print("Opção invalida, por favor tente novamente :(")   
