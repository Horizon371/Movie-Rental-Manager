
from Domain.Entities import movie

class MovieFileRepo:

    def __init__(self, movieRepository, fileName):
        self.__fileName = fileName
        self.__movieRepository = movieRepository
        self.loadFromFile()

    def add(self, movie):
        if self.find(movie.getId) == None:
            self.__movieRepository.add(movie)
            self.writeToFile()

    def update(self,oldMovie,newMovie):
        self.__movieRepository.update(oldMovie, newMovie)
        self.writeToFile()

    def find(self, movieId):
        return self.__movieRepository.find(movieId)

    def getAll(self):
        return self.__movieRepository.getAll()

    def remove(self,movie):
        self.__movieRepository.remove(movie)
        self.writeToFile()


    def writeToFile(self):

        f = open(self.__fileName, "w")
        try:
            for movie in self.__movieRepository.getAll():
                stringMovie = str(movie.getId) + ";" + movie.gettitle + ";" + movie.getdescription + ";" + movie.getgenre + "\n"
                f.write(stringMovie)
            f.close()

        except IOError as e:
            print("Error: ")
            raise e

    def loadFromFile(self):
        try:
            f = open(self.__fileName, "r")
            line = f.readline().strip()
            while len(line) > 0:
                line = line.split(";")
                self.__movieRepository.add(movie(int(line[0]), line[1], line[2], line[3]))
                line = f.readline().strip()
            f.close()
        except IOError as e:
            print("Error: ")
            raise e





