from pessoa import Pessoa
from metas import Metas
from disciplina import Disciplina
class Usuario(Pessoa):
    def __init__(self, nome: str, senha: str, curso: str, metas = None):
        super().__init__(nome,senha)
        self.__curso = curso 
        self.__metas = metas if metas else []
        self.__disciplinas_cursadas = []
        self.__disciplinas_cursando = []
    def get_curso(self):
        return self.__curso
    def get_metas(self):
        return self.__metas
    def set_metas(self, metas):
        self.__metas = metas
    def get_disciplinas_cursadas(self):
        return self.__disciplinas_cursadas
    def set_disciplinas_cursadas(self, disciplinas_cursadas):
        self.__disciplinas_cursadas = disciplinas_cursadas 
    #checa metas e add o obj criado em adiciona_meta_usuario
    def adicionar_metas(self, metas: Metas):
        for acha in self.__metas:
            if acha.get_texto().lower() == metas.get_texto().lower():
                print(f"A meta '{metas.get_texto()}' já existe!")
                return
        self.__metas.append(metas)

    def listar_metas(self):
        if not self.__metas:
            print("Nenhuma meta cadastrada.")
            return
        for meta in self.__metas:
            print(f"{meta.get_texto()} - {meta.status()}")

    def checa_requisitos(self, disciplina_req: Disciplina):
        requisitos = disciplina_req.get_requisitos()
        #se não tem req
        if not requisitos:
            return True
        #se tem req ele "anda" pela lista de req
        for checa in requisitos:
            #defi parametro
            requisito_cursado = False
            #"anda" pela lista de já cursadas
            for checa1 in self.__disciplinas_cursadas:
                #vê se checa1 é = ao requisito 
                if checa1.get_nome().lower() == checa.get_nome().lower():
                    #se for = ok
                    requisito_cursado = True
                    break
            if not requisito_cursado:
                print(f"Não foi cumprido o pré-requisito '{checa.get_nome()}'")
                return False
        return True    

    def adicionar_disciplinas_cursadas(self, disciplina: Disciplina):
        for acha in self.__disciplinas_cursadas:
            if acha.get_nome().lower() == disciplina.get_nome().lower():
                print("Essa disciplina já foi selecionada!")
                return
        if not self.checa_requisitos(disciplina):
            print(f"Não pode cursar '{disciplina.get_nome()}'. Verifique os pré-requisitos!")
            return    
        self.__disciplinas_cursadas.append(disciplina)    
        print(f"A disciplina '{disciplina.get_nome()}' foi selecionada como concluída")

    def adicionar_disciplinas_cursando(self, disciplina: Disciplina):    
        for acha in  self.__disciplinas_cursando:
            if acha.get_nome().lower() == disciplina.get_nome().lower():
                print("Essa disciplina já foi selecionada!")
                return
        if not self.checa_requisitos(disciplina):
            print(f"Não pode cursar '{disciplina.get_nome()}'. Verifique os pré-requisitos!")
            return
        self.__disciplinas_cursando.append(disciplina)
        print(f"A disciplina '{disciplina.get_nome()}' foi selecionada como cursando")

    def concluir_disciplina(self, nome_concluida: str):
        for acha in self.__disciplinas_cursando:
            if acha.get_nome().lower() == nome_concluida.lower():
                self.__disciplinas_cursando.remove(acha)    
                self.__disciplinas_cursadas.append(acha)
                return True
        print(f"Você não estava cursando '{nome_concluida}'")    
    
    def listar_disciplinas_cursadas(self):   
        print("\nDisciplinas que você já cursou:")
        if not self.__disciplinas_cursadas:
            print("Você ainda não cursou nenhuma disciplina")
            return
        for disciplina in self.__disciplinas_cursadas:
            print(f"- {disciplina.get_nome()} (Código: {disciplina.get_codigo()}, {disciplina.get_horas()}h)")
    
    def listar_disciplinas_cursando(self):
        print("\nDisciplinas que você está cursando:")
        if not self.__disciplinas_cursando:
            print("Você ainda não adicionou nenhuma disciplina com cursando")
            return
        for disciplina in self.__disciplinas_cursando:
            print(f"- {disciplina.get_nome()} (Código: {disciplina.get_codigo()}, {disciplina.get_horas()}h)")

    def _adicionar_disciplina_cursada_input(self, gerenciador):
        meu_curso = gerenciador.obter_curso(self.get_curso())
        if not meu_curso:
            print("Curso não encontrado!")
            return
        disciplinas_do_meu_curso = meu_curso.get_disciplinas()
        if not disciplinas_do_meu_curso:
            print("Nenhuma disciplina no curso!")
            return
        print(f"\n|DISCIPLINAS DO SEU CURSO: {meu_curso.get_nome()}")
        for i, disciplina in enumerate(disciplinas_do_meu_curso, 1):
            print(f"{i}. {disciplina.get_nome()} ({disciplina.get_codigo()})")
        while True:
            escolha_input = input("\nEscolha o número da disciplina: ").strip()
            if escolha_input.isdigit():
                escolha = int(escolha_input)
                if 1 <= escolha <= len(disciplinas_do_meu_curso):
                    disciplina_escolhida = disciplinas_do_meu_curso[escolha - 1]
                    self.adicionar_disciplinas_cursadas(disciplina_escolhida)
                    break
                else:
                    print("Número inválido! Escolha entre 1 e", len(disciplinas_do_meu_curso))
            else:
                print("Digite apenas números!")    
    def _adicionar_meta_input(self):
        texto = input("Descrição da meta: ").strip()
        if not texto:
            print("A descrição não pode estar vazia!")
            return
        tempo_input = input("Tempo estimado (horas): ").strip()
        if tempo_input.replace('.', '').isdigit():
            tempo_estimado = float(tempo_input)
            if tempo_estimado > 0:
                meta = Metas(texto, tempo_estimado, concluida=False)
                self.adicionar_metas(meta)
                print("Meta adicionada com sucesso!")
            else:
                print("O tempo deve ser maior que zero!")
        else:
            print("Digite um número válido para o tempo!")             
    
    def rodar_comandos(self):
        x = True 
        while x:
            print("_________Modo Usuário____________")
            print(f"Bem-vindo(a) {self.get_nome()}!\nLembre-se: a cada passo que você dá, mais perto do seu sonho você está!")
            self.listar_disciplinas_cursando()

            print("""\n1- Adicionar disciplina em andamento
2- Concluir disciplina
3- Listar disciplinas concluídas
4- Adicionar meta
5- Listar metas
6- Sair""")
        
            opcao = input("Escolha uma opção: ").strip()
            if opcao == "1":
                self._adicionar_disciplina_cursando_input()
            elif opcao == "2":
                self._concluir_disciplina_input()
            elif opcao == "3":
                self.listar_disciplinas_cursadas()
            elif opcao == "4":
                self._adicionar_meta_input()
            elif opcao == "5":
                self.listar_metas()
            elif opcao == "6":
                print("Saindo do modo usuário...")
                break
            else:
                print("Opção inválida!")




