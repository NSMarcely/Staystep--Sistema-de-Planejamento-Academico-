from disciplina import Disciplina 
class Curso:
    def __init__(self, nome: str,semestres):
        self.nome = nome 
        self.semestres = semestres
        self.disciplinas: dict[str, Disciplina] = {}
    def __str__(self):
        return f"{self.nome} ({self.semestres} semestres)"
    
    def adicionar_disciplina(self, disciplina: Disciplina):
        if disciplina.codigo in self.disciplinas:
            print(f"\n|A disciplina '{disciplina.nome}' já existe no curso '{self.nome}'.")
            return
        self.disciplinas[disciplina.codigo] = disciplina
        print(f"\n|Disciplina '{disciplina.nome}' adicionada com sucesso ao curso '{self.nome}'.")
    
    def remover_disciplina(self, codigo: str):
        if codigo not in self.disciplinas:
            print(f"\n|A disciplina com código '{codigo}' não foi encontrada no curso '{self.nome}'.")
            return
        removida = self.disciplinas.pop(codigo)
        print(f"\n|Disciplina '{removida.nome}' removida do curso '{self.nome}' com sucesso!")
    def listar_disciplinas(self):
        if not self.disciplinas:
            print(f"\n|O curso '{self.nome}' ainda não possui disciplinas cadastradas.")
            return
        print(f"\n|Disciplinas do curso '{self.nome}':")
        for disciplina in self.disciplinas.values():
            reqs = [d.nome for d in disciplina.requisitos]
            reqs_str = ", ".join(reqs) if reqs else "Nenhum"
            print(f"- {disciplina.codigo} - {disciplina.nome} ({disciplina.horas}h), Requisitos: {reqs_str}")    
    