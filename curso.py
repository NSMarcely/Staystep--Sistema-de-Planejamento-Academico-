from disciplina import Disciplina

class Curso:
    def __init__(self, nome: str, semestres: int):
        self.nome = nome 
        self.semestres = semestres
        self.disciplinas: dict[str, Disciplina] = {}
    
    def to_dict(self):
        return {
            "nome": self.nome,
            "semestres": self.semestres,
            "disciplinas": {
                codigo: disciplina.to_dict()
                for codigo, disciplina in self.disciplinas.items()
            }
        }
    
    @classmethod
    def from_dict(cls, dados):
        curso = cls(dados["nome"], dados["semestres"])
        disciplinas_dict = dados.get("disciplinas", {})
        for codigo, disc_dados in disciplinas_dict.items():
            disciplina = Disciplina.from_dict(disc_dados)
            curso.disciplinas[codigo] = disciplina
        for codigo, disc_dados in disciplinas_dict.items():
            requisitos_codigos = disc_dados.get("requisitos", [])
            for req_codigo in requisitos_codigos:
                if req_codigo in curso.disciplinas:
                    curso.disciplinas[codigo].requisitos.append(curso.disciplinas[req_codigo])
        return curso

    def __str__(self):
        return f"{self.nome} ({self.semestres} semestres)"
    
    def adicionar_disciplina(self, disciplina: Disciplina):
        if disciplina.codigo in self.disciplinas:
            print(f"\n|A disciplina '{disciplina.nome}' já existe no curso '{self.nome}'.")
            return False
        self.disciplinas[disciplina.codigo] = disciplina
        print(f"\n|Disciplina '{disciplina.nome}' adicionada com sucesso ao curso '{self.nome}'.")
        return True
    
    def remover_disciplina(self, codigo: str):
        if codigo not in self.disciplinas:
            print(f"\n|A disciplina com código '{codigo}' não foi encontrada no curso '{self.nome}'.")
            return False  
        for disciplina in self.disciplinas.values():
            for req in disciplina.requisitos[:]:
                if req.codigo == codigo:
                    disciplina.requisitos.remove(req)
        
        removida = self.disciplinas.pop(codigo)
        print(f"\n|Disciplina '{removida.nome}' removida do curso '{self.nome}' com sucesso!")
        return True
    
    def listar_disciplinas(self):
        if not self.disciplinas:
            print(f"\n|O curso '{self.nome}' ainda não possui disciplinas cadastradas.")
            return
        print(f"\n|Disciplinas do curso '{self.nome}':")
        for disciplina in self.disciplinas.values():
            reqs = [d.nome for d in disciplina.requisitos]
            reqs_str = ", ".join(reqs) if reqs else "Nenhum"
            print(f"- {disciplina.codigo} - {disciplina.nome} ({disciplina.horas}h), Requisitos: {reqs_str}")
    
    def obter_disciplina_por_codigo(self, codigo: str):
        return self.disciplinas.get(codigo)
    
    def obter_disciplina_por_nome(self, nome: str):
        nome_lower = nome.lower()
        for disciplina in self.disciplinas.values():
            if disciplina.nome.lower() == nome_lower:
                return disciplina
        return None