import datetime
from Domain.Entities import *



class movie_validator:


    def validate_movie(self,movie):


        if len(movie.gettitle) == 0:
            raise ValueError

        if len(movie.getdescription) == 0:
            raise ValueError

        if len(movie.getgenre) == 0:
            raise ValueError

class client_validator:

    def validate_client(self,client):

        if type(client.getId) is not int:
            raise ValueError
        if len(client.gettname) == 0:
            raise ValueError


class rental_validator:
    def validate_rental(self,rental):
        if len(rental.getId) == 0:
            raise ValueError

        if type(rental.getrented_date)is not datetime:
            raise ValueError

        if type(rental.getdue_date)is not datetime:
            raise ValueError

        if type(rental.getreturned_date) is not datetime:
            raise ValueError

        if type(rental.getclientId) is not int:
            raise ValueError

        if type(rental.getmovieId) is not int:
            raise ValueError

