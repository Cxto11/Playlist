class Programas:
    def __init__(self,Nome,Ano):
        self._nome = Nome.title()
        self.ano = Ano
        self._like = 0
    
    @property
    def likes(self):
        return self._like
    @property
    def nome(self):
        return self._nome
    
    def dar_like(self):
        self._like += 1
    @nome.setter
    def nome (self,nome):
        self._nome = nome
    
    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - Likes:{self.likes}'
    
class Filme(Programas):
    def __init__(self, Nome, Ano, Duração):
        super().__init__(Nome, Ano)
        self.duração = Duração

    def __str__(self):     
        return f'Nome: {self._nome} - Ano: {self.ano} - Duração:{self.duração}min - Likes:{self.likes}'
    
class Serie(Programas):
    def __init__(self, Nome, Ano, Temporadas):
        super().__init__(Nome, Ano)
        self.temporadas = Temporadas

    def __str__(self):     
        return f'Nome: {self._nome} - Ano: {self.ano} - Temporadas:{self.temporadas} - Likes:{self.likes}'

class Playlist():
    def __init__(self,nome,programas):
        self.nome = nome
        self.programas = programas

    def __getitem__(self,item):
        return self.programas[item]

    @property
    def listagem(self):
        return self.programas

    @property
    def tamanho(self):
        return len(self.programas)

vingadores = Filme('vingadores: guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('todo mundo em panico', 1999, 100)
demolidor = Serie('demolidor', 2016, 3)

def chama_likes():
    vingadores.dar_like()
    vingadores.dar_like()
    vingadores.dar_like()
    atlanta.dar_like()
    atlanta.dar_like()
    atlanta.dar_like()
    atlanta.dar_like()
    tmep.dar_like()
    tmep.dar_like()
    tmep.dar_like()
    demolidor.dar_like()
    demolidor.dar_like()

chama_likes()

filmes_series = [vingadores,atlanta,tmep,demolidor]
Playlist_fim_semana = Playlist("Playlist - Fim de Semana: ",filmes_series)

print( vingadores in Playlist_fim_semana)
print(Playlist_fim_semana.tamanho)
for programa in Playlist_fim_semana:
    print(programa)
