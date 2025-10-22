from pessoa import Pessoa
from gerenciador_dados import Gerenciador_Dados
class Adm(Pessoa):
    def __init__(self, nome: str, senha: str,gerencia):
        super().__init__(nome, senha)
        self.__gerencia = gerencia  
    def get_gerencia(self):
        return self.__gerencia 
    def rodar_comandos(self):
        x = True 
        while x:
            print("__________Modo Usuário__________")
            print("""1- Adicionar disciplina
2- Remover disciplinas
3- Adicionar curso
4- Remover curso
5- Sair""")
            y = True 
            opcao = input("Opção escolhida:")
            if opcao == "1":
                nome_curso = input("Curso da disciplina: ")
                nome_disciplina = input("Nome da disciplina: ")
                horas = int(input("Horas da disciplina: "))
                codigo = input("Código da disciplina: ")
                requisitos = input("Requisitos (separados por vírgula, vazio se não tiver): ")
                if requisitos.strip() == "":
                    requisitos = []
                    self.__gerencia.adicionar_disciplina_curso(nome_curso, nome_disciplina, horas, codigo, requisitos)

                else:
                    requisitos = [r.strip() for r in requisitos.split(",")]
                    self.__gerencia.adicionar_disciplina_curso(nome_curso, nome_disciplina, horas, codigo, requisitos)

            elif opcao == "2":
                nome_curso = input("Curso da disciplina: ")
                nome_disciplina = input("Nome da disciplina a remover: ")
                self.__gerencia.remove_disciplina_curso(nome_curso, nome_disciplina)

            elif opcao == "3":
                nome = input("Nome do Curso:")
                semestres = input("Quantidade de semestres:")
                self.__gerencia.adicionar_curso(nome, semestres)
            elif opcao == "4":
                nome = input("Nome do curso:")
                self.__gerencia.remove_curso(nome)
            elif opcao == "5":
                print("Saindo do modo administrador...")  
                x = False  
            else:
                print("Opção invalida, por favor tente novamente :(")   
if __name__ == "__main__":
    # Cria o gerenciador de dados (o "banco central" do sistema)
    gerenciador = Gerenciador_Dados()

    # Cria um administrador e associa o gerenciador de dados a ele
    admin = Adm("Maly", "1234", gerenciador)

    print("===== SISTEMA STAYSTEP INICIADO =====")
    print(f"Bem-vindo(a), {admin.get_nome()}! Entrando no modo administrador...\n")

    # Chama o menu de comandos do administrador
    admin.rodar_comandos()

    print("===== FIM DO PROGRAMA =====")