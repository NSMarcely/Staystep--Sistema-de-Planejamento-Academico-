from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome: str, senha: str):
        self.__nome = nome
        self.__senha = senha

    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome = nome

    def get_senha(self):
        return self.__senha 
    def set_senha(self, senha):
        self.__senha = senha    
    @abstractmethod 
    def rodar_comandos(self):
        pass
    
    def __str__(self):
        return f"{self.__nome}"