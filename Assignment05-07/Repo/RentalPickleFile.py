from Repo.Repo import repo
from Domain.Entities import client
import pickle


class RentalPickleRepo(repo):

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

    def add(self,rental):
        self.loadFromFile()
        self.__data.append(rental)
        self.writeToFile()
        self.__data = []


    def remove(self,rental):
        self.loadFromFile()
        self.__data.remove(rental)
        self.writeToFile()
        self.__data = []

    def update(self,old_rental,new_rental):
        self.loadFromFile()
        for index in range (0,len(self.__data)):
            if self.__data[index] == old_rental:
                self.__data.remove(old_rental)
                self.__data.insert(index, new_rental)
        self.writeToFile()
        self.__data = []

    def find (self,rentalid):
        self.loadFromFile()
        for index in range(len(self.__data)):
            if self.__data[index].getId == rentalid:
                return self.__data[index]
        return None


    def getAll(self):
        self.loadFromFile()
        return self.__data


    def cleanFile(self):
        f = open(self.__fileName, "wb")
        pickle.dump([], f)
        f.close()

