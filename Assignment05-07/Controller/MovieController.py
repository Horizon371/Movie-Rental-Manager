
from UndoRedo.Managers import *
from UndoRedo.Handlers import *


class MovieController:
    def __init__(self,repository,validator,operationsManager):
        self.__repository=repository
        self.__validator=validator
        self.__operationsManager = operationsManager
        self.__handler = handler(self.__repository)


    def createmovie(self,movieId, title, description, genre):
        Movie = movie(movieId,title,description,genre)
        self.__validator.validate_movie(Movie)
        self.__repository.add(Movie)

        undoOperation = operation(self.__handler.removeMovieHandler, movieId)
        redoOperation = operation(self.__handler.createMovieHandler, movieId, title, description, genre)
        operations = undoRedoOperations(undoOperation,redoOperation)
        self.__operationsManager.addOperation(operations)

    def remove(self,movieId):
        movie = self.__repository.find(movieId)
        self.__repository.remove(movie)

        undoOperation = operation(self.__handler.createMovieHandler, movieId, movie.gettitle, movie.getdescription, movie.getgenre)
        redoOperation =  operation(self.__handler.removeMovieHandler, movieId)
        operations = undoRedoOperations(undoOperation, redoOperation)
        self.__operationsManager.addOperation(operations)


    def getAll(self):
        return self.__repository.getAll()

    def update(self,movieId,newTitle,newGenre,newDescription):
        oldmovie = self.__repository.find(movieId)
        newmovie = movie(movieId,newTitle,newGenre,newDescription)
        self.__repository.update(oldmovie,newmovie)

    def searchid(self,movieId):
        return self.__repository.find(movieId)