from pessoa import Pessoa
from metas import Metas
from disciplina import Disciplina

class Usuario(Pessoa):
    def __init__(self, nome: str, senha: str, curso: str, gerenciador, metas=None, disciplinas_cursadas=None, disciplinas_cursando=None):
        super().__init__(nome, senha)
        self.__curso = curso 
        self.metas = metas if metas is not None else []
        self.disciplinas_cursadas = disciplinas_cursadas if disciplinas_cursadas is not None else {}   
        self.disciplinas_cursando = disciplinas_cursando if disciplinas_cursando is not None else {}   
        self.gerenciador = gerenciador
    
    def get_curso(self):
        return self.__curso
    
    def set_curso(self, curso):
        self.__curso = curso

    # Métodos para JSON
    def to_dict(self):
        return {
            "nome": self.get_nome(),
            "senha": self.get_senha(),
            "curso": self.__curso,
            "metas": [meta.to_dict() for meta in self.metas],
            "disciplinas_cursadas": {
                nome: disciplina.codigo for nome, disciplina in self.disciplinas_cursadas.items()
            },
            "disciplinas_cursando": {
                nome: disciplina.codigo for nome, disciplina in self.disciplinas_cursando.items()
            }
        }
    @classmethod
    def from_dict(cls, dados, gerenciador):
        nome = dados.get("nome", "")
        senha = dados.get("senha", "")
        curso = dados.get("curso", "")
        metas_data = dados.get("metas", [])
        disciplinas_cursadas_data = dados.get("disciplinas_cursadas", {})
        disciplinas_cursando_data = dados.get("disciplinas_cursando", {})
        usuario = cls(
            nome=nome,
            senha=senha,
            curso=curso,
            gerenciador=gerenciador,
            metas=[],
            disciplinas_cursadas={},
            disciplinas_cursando={}
        )
        try:
            usuario.metas = [Metas.from_dict(meta_data) for meta_data in metas_data]
        except Exception as e:
            print(f"|Erro ao carregar metas do usuário {nome}: {e}")
            usuario.metas = []
        try:
            for nome_disciplina, codigo_disciplina in disciplinas_cursadas_data.items():
                curso_obj = gerenciador.retorna_curso(usuario.__curso)
                if curso_obj:
                    disciplina = curso_obj.obter_disciplina_por_codigo(codigo_disciplina)
                    if disciplina:
                        usuario.disciplinas_cursadas[nome_disciplina.lower()] = disciplina
                    else:
                        print(f"|Aviso: Disciplina {codigo_disciplina} não encontrada no curso para usuário {nome}")
        except Exception as e:
            print(f"|Erro ao carregar disciplinas cursadas do usuário {nome}: {e}")
        try:
            for nome_disciplina, codigo_disciplina in disciplinas_cursando_data.items():
                curso_obj = gerenciador.retorna_curso(usuario.__curso)
                if curso_obj:
                    disciplina = curso_obj.obter_disciplina_por_codigo(codigo_disciplina)
                    if disciplina:
                        usuario.disciplinas_cursando[nome_disciplina.lower()] = disciplina
                    else:
                        print(f"|Aviso: Disciplina {codigo_disciplina} não encontrada no curso para usuário {nome}")
        except Exception as e:
            print(f"|Erro ao carregar disciplinas cursando do usuário {nome}: {e}")
        return usuario

    def adicionar_metas(self, meta: Metas):
        for acha in self.metas:
            if acha.texto.lower() == meta.texto.lower(): 
                print(f"\n|A meta '{meta.texto}' já existe!") 
                return False
        self.metas.append(meta)
        return True

    def listar_metas(self):
        if not self.metas:
            print("\n|Nenhuma meta cadastrada.")
            return
        print("\n___Suas Metas___")
        for i, meta in enumerate(self.metas, 1):
            status = "✓ Concluída" if meta.concluida else "⌛ Pendente"  
            tempo = f" ({meta.tempo_estimado}h)" if meta.tempo_estimado > 0 else ""
            print(f"{i}. {meta.texto}{tempo} - {status}")

    def checa_requisitos(self, disciplina_req: Disciplina):
        requisitos = disciplina_req.requisitos
        if not requisitos:
            return True
        for requisito in requisitos:
            requisito_cursado = False
            for disciplina_cursada in self.disciplinas_cursadas.values():
                if disciplina_cursada.codigo == requisito.codigo:
                    requisito_cursado = True
                    break
            if not requisito_cursado:
                print(f"\n|Requisito não cumprido: '{requisito.nome}'")
                return False
        return True

    def adicionar_disciplinas_cursadas(self, disciplina: Disciplina):
        chave = disciplina.nome.lower()
        if chave in self.disciplinas_cursadas:
            print("\n|Essa disciplina já foi selecionada!")
            return False
        if not self.gerenciador.checa_disciplina_curso(self.get_curso(), disciplina.nome):
            print(f"\n|A disciplina '{disciplina.nome}' não existe no curso '{self.get_curso()}'")
            return False
        if not self.checa_requisitos(disciplina):
            print(f"\n|Não pode cursar '{disciplina.nome}'. Verifique os pré-requisitos!")
            return False
        self.disciplinas_cursadas[chave] = disciplina
        print(f"\n|A disciplina '{disciplina.nome}' foi selecionada como concluída")
        return True

    def adicionar_disciplinas_cursando(self, disciplina: Disciplina):   
        chave = disciplina.nome.lower()
        if chave in self.disciplinas_cursando:
            print(f"\n|Você já está cursando a disciplina '{disciplina.nome}'!")
            return False
        if chave in self.disciplinas_cursadas:
            print(f"\n|Você já cursou a disciplina '{disciplina.nome}'!")
            return False
        if not self.gerenciador.checa_disciplina_curso(self.get_curso(), disciplina.nome): 
            print(f"\n|A disciplina '{disciplina.nome}' não existe no curso '{self.get_curso()}'")
            return False
        if not self.checa_requisitos(disciplina):
            print(f"\n|Não pode cursar '{disciplina.nome}'. Verifique os pré-requisitos!")
            return False
        self.disciplinas_cursando[chave] = disciplina
        print(f"\n|A disciplina '{disciplina.nome}' foi selecionada como cursando")
        return True

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
        print("\n|Disciplinas Concluídas:")
        if not self.disciplinas_cursadas:
            print("|Você ainda não cursou nenhuma disciplina|")
            return
        for disciplina in self.disciplinas_cursadas.values():
            print(f"- {disciplina.nome} (Código: {disciplina.codigo}, {disciplina.horas}h)")

    def listar_disciplinas_cursando(self):
        print("\n|Disciplinas em Andamento:")
        if not self.disciplinas_cursando:
            print("|Você não está cursando nenhuma disciplina|")
            return
        for disciplina in self.disciplinas_cursando.values():
            requisitos_str = ""
            if disciplina.requisitos:
                reqs = [req.nome for req in disciplina.requisitos]
                requisitos_str = f" | Requisitos: {', '.join(reqs)}"
            print(f"- {disciplina.nome} (Código: {disciplina.codigo}, {disciplina.horas}h){requisitos_str}")

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
        print("\n___Concluir Meta___")
        self.listar_metas()
        try:
            indice = int(input("\nDigite o número da meta a concluir: ").strip())
            if self.concluir_meta(indice):
                self.gerenciador.salvar_dados()
        except ValueError:
            print("\n|Por favor, digite um número válido!")

    def _adicionar_disciplina_cursando_input(self):
        print("\n___Adicionar Disciplina em Andamento___")
        curso_obj = self.gerenciador.retorna_curso(self.get_curso())
        if not curso_obj:
            print(f"\n|Curso '{self.get_curso()}' não encontrado!")
            return 
            
        print(f"\nDisciplinas disponíveis no curso {self.get_curso()}:")
        disciplinas_disponiveis = []
        for disciplina in curso_obj.disciplinas.values():
            chave = disciplina.nome.lower()
            if chave not in self.disciplinas_cursadas and chave not in self.disciplinas_cursando:
                requisitos_str = ""
                if disciplina.requisitos:
                    reqs = [req.nome for req in disciplina.requisitos]
                    requisitos_str = f" | Requisitos: {', '.join(reqs)}"
                print(f"- {disciplina.nome} (Código: {disciplina.codigo}, {disciplina.horas}h){requisitos_str}")
                disciplinas_disponiveis.append(disciplina)  
        if not disciplinas_disponiveis:
            print("\n|Todas as disciplinas já foram cursadas ou estão em andamento!")
            return
        nome_disciplina = input("\nDigite o nome da disciplina: ").strip()
        if not nome_disciplina:
            print("\n|Nome da disciplina não pode estar vazio!")
            return 
        disciplina = self.gerenciador.buscar_disciplina_por_nome(self.get_curso(), nome_disciplina)
        if not disciplina:
            print(f"\n|A disciplina '{nome_disciplina}' não existe no curso '{self.get_curso()}'")
            return
        if self.adicionar_disciplinas_cursando(disciplina):
            self.gerenciador.salvar_dados()

    def _concluir_disciplina_input(self): 
        print("\n___Concluir Disciplina___")
        if not self.disciplinas_cursando:
            print("\n|Você não está cursando nenhuma disciplina!")
            return
        self.listar_disciplinas_cursando()
        nome_disciplina = input("\nDigite o nome da disciplina a concluir: ").strip()
        if not nome_disciplina:
            print("\n|Nome da disciplina não pode estar vazio!")
            return
        if self.concluir_disciplina(nome_disciplina):
            self.gerenciador.salvar_dados()

    def _adicionar_meta_input(self):
        print("\n|Adicionar Meta:")
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
        meta = Metas(texto, tempo_float, False)
        if self.adicionar_metas(meta):
            self.gerenciador.salvar_dados()  
            print("\n|Meta adicionada com sucesso!")

    def rodar_comandos(self):
        while True:
            print("_"*70)
            print(f"\n_______Modo Usuário______")
            print("Lembre-se: a cada passo que você dá, mais perto do seu sonho você está!")
            self.listar_disciplinas_cursando()
            self.listar_metas()
            print("""\n1- Adicionar disciplina em andamento
2- Concluir disciplina
3- Listar disciplinas concluídas
4- Adicionar meta
5- Concluir meta
6- Sair""")
            opcao = input("\nEscolha uma opção: ").strip()
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
                self.gerenciador.salvar_dados()
                break
            else:
                print("\n|Opção inválida!")