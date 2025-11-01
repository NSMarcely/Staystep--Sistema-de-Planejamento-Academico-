class Disciplina:
    def __init__(self, nome: str, horas: int, codigo: str, requisitos=None):
        self.nome = nome
        self.horas = horas
        self.codigo = codigo
        self.requisitos = requisitos if requisitos else []

    def __str__(self):
        return f"{self.nome} | {self.codigo} ({self.horas}h)"

    def to_dict(self):
        return {
            "nome": self.nome,
            "horas": self.horas,
            "codigo": self.codigo,
            "requisitos": [req.codigo for req in self.requisitos]
        }
    @classmethod
    def from_dict(cls, dados):
        return cls(
            dados["nome"],
            dados["horas"],
            dados["codigo"],
            []
        )
