from disciplina import Disciplina 
class Metas:
    def __init__(self, texto: str, tempo_estimado: float, concluida: bool):
        self.__texto = texto
        self.__tempo_estimado = tempo_estimado
        self.__concluida = concluida
    def get_texto(self):
        return self.__texto
    def set_texto(self,texto):
        self.__texto = texto    
    def get_tempo_estimado(self):
        return self.__tempo_estimado 
    def set_tempo_estimado(self, tempo_estimado):
        self.__tempo_estimado = tempo_estimado
    def get_concluida(self):
        return self.__concluida
    def set_concluida(self, concluida):
        self.__concluida = concluida    
