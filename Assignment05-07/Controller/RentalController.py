from Domain.Entities import rental
from Validators.RentalException import *
from Repo.Dto import *
import datetime

class RentalController:

    def __init__(self,repository,validator,moviecontroller,clientcontroller):
        self.__repository = repository
        self.__validaor = validator
        self.__moviecontroller = moviecontroller
        self.__clientcontroller = clientcontroller


    def can_client_rent(self, rented_date, clientId):

        for index in self.__repository.getAll():
            if index.getclientId == clientId:
                if index.getreturned_date == None:
                    return False
        return True


    def getAll(self):
        return self.__repository.getAll()


    def createRental(self,rentalId,clientId,movieId,rented_date,due_date):

        if self.can_client_rent(rented_date,clientId) == False:
            raise RentalException("Client has to return movies")


        Rental = rental(rentalId,clientId,movieId,rented_date,due_date,returned_date = None)
        self.__repository.add(Rental)




    def most_times_rented_movie_dto(self):
        movies = self.__moviecontroller.getAll()
        rentals = self.getAll()

        dictionary = {}
        for Movie in movies:
            dictionary[Movie.getId] = 0

        for Movie in movies:
            for Rental in rentals:
                if Rental.getmovieId == Movie.getId:
                    dictionary[Movie.getId] = dictionary[Movie.getId] + 1

        dto = []
        for key,value in dictionary.items():
            movie = self.__moviecontroller.searchid(key)
            movied_dto = moviedto(key,movie.gettitle,value)
            dto.append(movied_dto)

        return dto


    def number_of_rented_days(self,movieId,rentalId):


        Rental = self.__repository.find(rentalId)
        if Rental.getmovieId == movieId:
            if Rental.getreturned_date != None:
                number_of_days = Rental.getdue_date - Rental.getrented_date
            else:
                number_of_days = datetime.date.today() - Rental.getrented_date

        return number_of_days.days

    def most_days_rented_movie_dto(self):

        movies = self.__moviecontroller.getAll()
        rentals = self.getAll()

        dictionary = {}
        for Movie in movies:
            dictionary[Movie.getId] = 0

        for Movie in movies:
            for Rental in rentals:
                if Rental.getmovieId == Movie.getId:
                    number_of_rented_days = self.number_of_rented_days(Rental.getmovieId,Rental.getId)
                    dictionary[Movie.getId] = dictionary[Movie.getId] + number_of_rented_days
        dto = []
        for key, value in dictionary.items():

            movie = self.__moviecontroller.searchid(key)
            movie_dto = moviedto(key, movie.gettitle,value)
            dto.append(movie_dto)

        return dto

    def all_rentals(self):
        rentals = self.getAll()
        dto = []
        for Rental in rentals:
            movie = self.__moviecontroller.searchid(Rental.getmovieId)
            dto.append("Id:" + str(movie.getId) + " title:" + movie.gettitle)

        return dto


    def most_days_rented_movie(self):
        dto = self.most_days_rented_movie_dto()
        return sorted(dto, reverse=True, key=lambda x: x.getcount)

    def most_times_rented_movie(self):
        dto = self.most_times_rented_movie_dto()
        return sorted(dto, reverse=True, key=lambda x: x.getcount)

    def most_active_clients_dto(self):
        clients = self.__clientcontroller.getAll()
        rentals = self.getAll()


        dictionary = {}
        for Client in clients:
            dictionary[Client.getId] = 0

        for Rental in rentals:
            dictionary[Rental.getclientId] = dictionary[Rental.getclientId] + self.number_of_rented_days(Rental.getmovieId,Rental.getId)

        dto = []
        for key, value in dictionary.items():
            client = self.__clientcontroller.searchid(key)
            client_dto = clientdto(key, client.gettname, value)
            dto.append(client_dto)

        return dto

    def most_active_clients(self):
        dto = self.most_active_clients_dto()
        return sorted(dto, reverse=True, key=lambda x: x.count)

    def late_rentals_dto(self):
        rentals = self.getAll()
        dto = []
        for Rental in rentals:
            if Rental.getreturned_date == None:
                delay = datetime.date.today() - Rental.getdue_date
                Late_Rental = late_rentals(Rental.getmovieId,delay.days)
                dto.append(Late_Rental)
        return dto


    def late_rentals(self):
        dto = self.late_rentals_dto()
        return sorted(dto, reverse=True, key=lambda x: x.getdelay)

    def removeRental(self,rentalId):
        rental = self.__repository.find(rentalId)
        self.__repository.remove(rental)

    def returnmovie(self,rentalId,Date):
        Rentall = self.__repository.find(rentalId)
        Rentall.setreturned_date(Date)



