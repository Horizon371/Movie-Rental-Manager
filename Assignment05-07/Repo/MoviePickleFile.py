from Repo.Repo import repo
import pickle


class MoviePickleRepo(repo):

    def __init__(self, fileName):

        super().__init__()
        self.__fileName = fileName

    def writeToFile(self):
        f = open(self.__fileName, "wb")
        pickle.dump(self.__data, f)
        f.close()

    def loadFromFile(self):
        f = open(self.__fileName, "rb")
        try:
            self.__data = pickle.load(f)
        except EOFError:
            self.__data = []
        except Exception as e:
            raise e
        finally:
            f.close()

    def add(self,movie):
        self.loadFromFile()
        self.__data.append(movie)
        self.writeToFile()
        self.__data = []


    def remove(self,movie):
        self.loadFromFile()
        self.__data.remove(movie)
        self.writeToFile()
        self.__data = []

    def update(self,old_movie,new_movie):
        self.loadFromFile()
        for index in range (0,len(self.__data)):
            if self.__data[index]==old_movie:
                self.__data.remove(old_movie)
                self.__data.insert(index,new_movie)
        self.writeToFile()
        self.__data = []

    def find (self,movieid):
        self.loadFromFile()
        for index in range(len(self.__data)):
            if self.__data[index].getId == movieid:
                return self.__data[index]
        return None


    def getAll(self):
        self.loadFromFile()
        return self.__data


    def cleanFile(self):
        f = open(self.__fileName, "wb")
        pickle.dump([], f)
        f.close()

