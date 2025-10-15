class Pessoa:
    def __init__(self, nome: str, matricula: str, senha: str):
        self.nome = nome
        self.matricula = matricula
        self.senha = senha

    def __str__(self):
        return f"{self.nome} ({self.matricula})"