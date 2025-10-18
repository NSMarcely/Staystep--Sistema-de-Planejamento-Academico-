from pessoa import Pessoa
class Adm(Pessoa):
    def __init__(self, nome: str, senha: str, codigo_verificacao: str = "Mf2412"):
        super().__init__(nome, senha)
        self.__codigo_verificacao = codigo_verificacao
    def get_codigo_verificacao(self):
        return self.__codigo_verificacao    

    def verica_codigo(self): 
       for x in range(3):
           tentativa = input("\nDigite o código:")
           if tentativa == self.__codigo_verificacao:
              print(f"Bem-vindo(a), {self.get_nome()} ao modo administrador")
              break
           else:
              print("\nCódigo inválido!")
              print(f"Você só tem {3-x} chance(s) restantes")

if __name__ == "__main__":
    teste = Adm("Marce", "senha")
    teste.verica_codigo()
