class Metas:
    def __init__(self, texto: str, tempo_estimado: float, concluida: bool = False):
        self.texto = texto
        self.tempo_estimado = tempo_estimado
        self.concluida = concluida
    
    @property
    def tempo(self):
        return self.tempo_estimado
    
    def status(self):
        return "Concluída" if self.concluida else "Pendente"
    
    def to_dict(self):
        return {
            "texto": self.texto,
            "tempo_estimado": self.tempo_estimado,
            "concluida": self.concluida
        }
    
    @classmethod
    def from_dict(cls, dados):
        return cls(
            texto=dados["texto"],
            tempo_estimado=dados["tempo_estimado"],
            concluida=dados["concluida"]
        )
    
    def __str__(self):
        tempo_str = f" ({self.tempo_estimado}h)" if self.tempo_estimado > 0 else ""
        status = "✓ Concluída" if self.concluida else "Pendente"
        return f"{self.texto}{tempo_str} - {status}"