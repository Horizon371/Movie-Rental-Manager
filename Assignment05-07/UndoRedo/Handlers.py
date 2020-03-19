from Domain.Entities import *
class handler:
    def __init__(self,repository):
        self.__repository = repository

    def createClientHandler(self,clientId, name):
        Client = client(clientId, name)
        self.__repository.add(Client)

    def createMovieHandler(self, movieId, title, description, genre):
        Movie = movie(movieId, title, description, genre)
        self.__repository.add(Movie)

    def removeClientHandler(self, clientId):
        client = self.__repository.find(clientId)
        self.__repository.remove(client)

    def removeMovieHandler(self, movieId):
        movie = self.__repository.find(movieId)
        self.__repository.remove(movie)
