class Metas:
    def __init__(self, texto: str, tempo_estimado: float, concluida: bool):
        self.texto = texto
        self.tempo_estimado = tempo_estimado
        self.concluida = concluida
    def status(self):
        return "Concluída" if self.concluida else "Pendente"
    