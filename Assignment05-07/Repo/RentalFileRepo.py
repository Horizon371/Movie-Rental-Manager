

from Domain.Entities import rental
import datetime

class RentalFileRepo:

    def __init__(self, rentalRepository, fileName):
        self.__rentalRepository = rentalRepository
        self.__fileName = fileName
        #self.loadFromFile()

    def add(self, rental):
        if self.find(rental.getId) == None:
            self.__rentalRepository.add(rental)
            self.writeToFile()

    def update(self, oldRental, newRental):
        self.__rentalRepository.update(oldRental, newRental)
        self.writeToFile()


    def find(self, rentalId):
        return self.__rentalRepository.find(rentalId)

    def getAll(self):
        return self.__rentalRepository.getAll()

    def remove(self, rental):
        self.__rentalRepository.remove(rental)
        self.writeToFile()

    def writeToFile(self):

        f = open(self.__fileName, "w")
        try:
            for rental in self.__rentalRepository.getAll():
                stringRental = str(rental.getId) + ";" + str(rental.getclientId) + ";" + str(rental.getmovieId) + ";" + str(rental.getrented_date) + ";" + str(rental.getdue_date) + ";" + str(rental.getreturned_date) + "\n"
                f.write(stringRental)
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
                self.__rentalRepository.add(rental(int(line[0]), int(line[1]), int(line[2]), datetime.date(int(line[3])), datetime.date(int(line[4])), datetime.date(int(line[5]))))
                line = f.readline().strip()
            f.close()
        except IOError as e:
            print("Error: ")
            raise e



