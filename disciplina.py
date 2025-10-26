class Disciplina:
    def __init__(self, nome: str, horas: int, codigo: str, requisitos = None):
        self.nome = nome
        self.horas = horas 
        self.codigo = codigo 
        self.requisitos = requisitos if requisitos else []
    def __str__(self):
        return f"{self.nome}|{self.codigo} ({self.horas}h)"    