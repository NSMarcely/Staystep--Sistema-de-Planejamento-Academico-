from pessoa import Pessoa
from metas import Metas
from disciplina import Disciplina

class Usuario(Pessoa):
    def __init__(self, nome: str, senha: str, curso: str, gerenciador, metas=None):
        super().__init__(nome, senha)
        self.__curso = curso 
        self.metas = metas if metas else []
        self.disciplinas_cursadas = {}   
        self.disciplinas_cursando = {}   
        self.gerenciador = gerenciador
    
    def get_curso(self):
        return self.__curso
    
    def set_curso(self, curso):
        self.__curso = curso

    def adicionar_metas(self, meta: Metas):
        for acha in self.metas:
            if acha.texto.lower() == meta.texto.lower(): 
                print(f"\n|A meta '{meta.texto}' já existe!") 
                return
        self.metas.append(meta)

    def listar_metas(self):
        if not self.metas:
            print("\n|Nenhuma meta cadastrada.")
            return
        for i, meta in enumerate(self.metas, 1):
            status = "✓ Concluída" if meta.concluida else "Pendente :()"  
            print(f"{i}. {meta.texto} - {status}")  

    def checa_requisitos(self, disciplina_req: Disciplina):
        requisitos = disciplina_req.requisitos
        if not requisitos:
            return True
        for checa in requisitos:
            requisito_cursado = False
            for checa1 in self.disciplinas_cursadas.values():
                if checa1.nome.lower() == checa.nome.lower():
                    requisito_cursado = True
                    break
            if not requisito_cursado:
                print(f"\n|Não foi cumprido o pré-requisito '{checa.nome}'")
                return False
        return True    

    def adicionar_disciplinas_cursadas(self, disciplina: Disciplina):
        chave = disciplina.nome.lower()
        if chave in self.disciplinas_cursadas:
            print("\n|Essa disciplina já foi selecionada!")
            return
        if not self.gerenciador.checa_disciplina_curso(self.get_curso(), disciplina.nome):
            print(f"\n|A disciplina '{disciplina.nome}' não existe no curso '{self.get_curso()}'")
            return

        if not self.checa_requisitos(disciplina):
            print(f"\n|Não pode cursar '{disciplina.nome}'. Verifique os pré-requisitos!")
            return    
        self.disciplinas_cursadas[chave] = disciplina
        print(f"\n|A disciplina '{disciplina.nome}' foi selecionada como concluída")

    def adicionar_disciplinas_cursando(self, disciplina: Disciplina):   
        chave = disciplina.nome.lower()
        if chave in self.disciplinas_cursando:
            print(f"\n|Você já está cursando a disciplina '{disciplina.nome}'!")
            return
        if chave in self.disciplinas_cursadas:
            print(f"\n|Você já cursou a disciplina '{disciplina.nome}'!")
            return
        if not self.gerenciador.checa_disciplina_curso(self.get_curso(), disciplina.nome): 
            print(f"\n|A disciplina '{disciplina.nome}' não existe no curso '{self.get_curso()}'")
            return
        if not self.checa_requisitos(disciplina):
            print(f"\n|Não pode cursar '{disciplina.nome}'. Verifique os pré-requisitos!")
            return
        self.disciplinas_cursando[chave] = disciplina
        print(f"\n|A disciplina '{disciplina.nome}' foi selecionada como cursando")

    def concluir_disciplina(self, nome_concluida: str):
        chave = nome_concluida.lower()
        if not self.disciplinas_cursando:
            print("\n|Você não está cursando nenhuma disciplina!")
            return False
        if chave in self.disciplinas_cursando:
            disciplina = self.disciplinas_cursando.pop(chave)
            self.disciplinas_cursadas[chave] = disciplina
            print(f"\n|Disciplina '{disciplina.nome}' concluída com sucesso!")
            return True
        print(f"\n|Você não estava cursando '{nome_concluida}'")
        return False

    def listar_disciplinas_cursadas(self):   
        print("\nDisciplinas que você já cursou:")
        if not self.disciplinas_cursadas:
            print("|Você ainda não cursou nenhuma disciplina|")
            return
        for disciplina in self.disciplinas_cursadas.values():
            print(f"- {disciplina.nome} (Código: {disciplina.codigo}, {disciplina.horas}h)")
    
    def listar_disciplinas_cursando(self):
        print("\nDisciplinas que você está cursando:")
        if not self.disciplinas_cursando:
            print("\n|Você ainda não adicionou nenhuma disciplina com cursando")
            return
        for disciplina in self.disciplinas_cursando.values():
            print(f"- {disciplina.nome} (Código: {disciplina.codigo}, {disciplina.horas}h)")
     
    def concluir_meta(self, indice: int):
        if indice < 1 or indice > len(self.metas):
            print("\n|Índice de meta inválido!")
            return False
        meta = self.metas[indice - 1]
        if meta.concluida:  
            print(f"\n|A meta '{meta.texto}' já estava concluída!")  
            return False
        meta.concluida = True  
        print(f"\n|Meta '{meta.texto}' concluída com sucesso!")
        return True

    def _concluir_meta_input(self):
        if not self.metas:
            print("\n|Você não tem nenhuma meta cadastrada!")
            return
        print("\n__Concluir Meta___")
        self.listar_metas()
        try:
            indice = int(input("\nDigite o número da meta a concluir: ").strip())
            self.concluir_meta(indice)
        except ValueError:
            print("\n|Por favor, digite um número válido!")

    def _adicionar_disciplina_cursando_input(self):
        print("\n_____Adicionar Disciplina em Andamento_____")
        
        # Mostra disciplinas disponíveis do curso
        curso_obj = self.gerenciador.retorna_curso(self.get_curso())
        if curso_obj:
            print(f"\nDisciplinas disponíveis no curso {self.get_curso()}:")
            disciplinas_disponiveis = []
            for disciplina in curso_obj.disciplinas.values():
                chave = disciplina.nome.lower()
                if chave not in self.disciplinas_cursadas and chave not in self.disciplinas_cursando:
                    print(f"- {disciplina.nome} (Código: {disciplina.codigo}, {disciplina.horas}h)")
                    disciplinas_disponiveis.append(disciplina)
            
            if not disciplinas_disponiveis:
                print("\n|Todas as disciplinas já foram cursadas ou estão em andamento!")
                return
        
        nome_disciplina = input("\nDigite o nome da disciplina: ").strip()
        if not nome_disciplina:
            print("\n|Nome da disciplina não pode estar vazio!")
            return
        
        # Busca a disciplina REAL/obj do gerenciador
        disciplina = self.gerenciador.buscar_disciplina_por_nome(self.get_curso(), nome_disciplina)
        if not disciplina:
            print(f"A disciplina '{nome_disciplina}' não existe no curso '{self.get_curso()}'")
            return
        
        # Usa a disciplina REAL/obj do sistema
        self.adicionar_disciplinas_cursando(disciplina)
        
    def _concluir_disciplina_input(self): 
        print("\n____Concluir Disciplina____")
        if not self.disciplinas_cursando:
            print("\n|Você não está cursando nenhuma disciplina!")
            return
        nome_disciplina = input("Digite o nome da disciplina a concluir: ").strip()
        if not nome_disciplina:
            print("\n|Nome da disciplina não pode estar vazio!")
            return     
        self.concluir_disciplina(nome_disciplina)

    def _adicionar_meta_input(self):
        print("\n___Adicionar Meta___")
        texto = input("Digite a meta que deseja adicionar: ").strip()
        if not texto:
            print("\n|A meta não pode estar vazia!")
            return    
        tempo_estimado = input("Digite o tempo de estudo (horas): ").strip()
        try:
            tempo_float = float(tempo_estimado) if tempo_estimado else 0.0
            if tempo_float < 0:
                print("\n|O tempo não pode ser negativo!")
                return
        except ValueError:
            print("\n|Tempo deve ser um número! Usando 0 horas.")
            tempo_float = 0.0
        
        # Cria a meta e adiciona
        meta = Metas(texto, tempo_float, False)
        self.adicionar_metas(meta)
        print("\n|Meta adicionada com sucesso!")

    def rodar_comandos(self):
        x = True 
        while x:
            print("\n_________Modo Usuário____________")
            print(f"Bem-vindo(a) {self.get_nome()}!\nLembre-se: a cada passo que você dá, mais perto do seu sonho você está!")
            self.listar_disciplinas_cursando()
            self.listar_metas()

            print("""\n1- Adicionar disciplina em andamento
2- Concluir disciplina
3- Listar disciplinas concluídas
4- Adicionar meta
5- Concluir meta
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
                self._concluir_meta_input()
            elif opcao == "6":
                print("\n|Saindo do modo usuário...")
                break
            else:
                print("\n|Opção inválida!")
