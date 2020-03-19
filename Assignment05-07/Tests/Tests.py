
from Controller.ClientController import *
from Controller.MovieController import *
from Controller.RentalController import *
from Validators.Validators import *
from Repo.Repo import *
import unittest

class test(unittest.TestCase):

    def setUp(self):
        Validatormovie = movie_validator()
        Validatorclient = client_validator()
        Validatorrental = rental_validator()

        Repositorymovie = repo()
        Repositoryclient = repo()
        Repositoryrental = repo()

        self.__movie_controller = MovieController(Repositorymovie, Validatormovie)
        self.__client_controller = ClientController(Repositoryclient, Validatorclient)
        self.__rental_controller = RentalController(Repositoryrental, Validatorrental, self.__movie_controller, self.__client_controller)

    def test_Movie(self):
        Movie = movie(1,"title","description","genre")
        self.assertEqual(Movie.getId,1)
        self.assertEqual(Movie.gettitle,"title")
        self.assertEqual(Movie.getdescription,"description")
        self.assertEqual(Movie.getgenre,"genre")

    def test_Client(self):
        Client = client(1,"name")
        self.assertEqual(Client.getId,1)
        self.assertEqual(Client.gettname,"name")

    def test_repo(self):
        Repository = repo()
        Movie = movie(1, "It`s a wonderful life", "description", "drama")
        Movie2 = movie(2, "Lol", "Lol", "Lolxd")
        Repository.add(Movie)
        all = Repository.getAll()
        self.assertEqual(len(all), 1)

        Repository.update(Movie,Movie2)
        all = Repository.getAll()
        self.assertEqual(len(all),1)

        Repository.remove(Movie2)
        all = Repository.getAll()
        self.assertEqual(len(all), 0)

############Movie##############################

    def test_create_movie(self):
        self.__movie_controller.createmovie(1,"a","b","c")
        allmov = self.__movie_controller.getAll()
        self.assertEqual(len(allmov),1)

    def test_remove_movie(self):
        self.__movie_controller.createmovie(1, "a", "b", "c")
        self.__movie_controller.remove(1)
        allmov = self.__movie_controller.getAll()
        self.assertEqual(len(allmov), 0)

    def test_update_movie(self):
        self.__movie_controller.createmovie(1, "a", "b", "c")
        self.__movie_controller.update(1,"d","e","f")
        allmov = self.__movie_controller.getAll()
        self.assertEqual(allmov[0].gettitle,"d")
        self.assertEqual(allmov[0].getdescription, "e")
        self.assertEqual(allmov[0].getgenre, "f")

    def test_search(self):
        self.__movie_controller.createmovie(1,"d","e","f")
        allmov = self.__movie_controller.searchid(1)
        self.assertEqual(allmov.gettitle, "d")
        self.assertEqual(allmov.getdescription, "e")
        self.assertEqual(allmov.getgenre, "f")

###############Client####################

    def test_create_client(self):
        self.__client_controller.createclient(1,"name")
        all = self.__client_controller.getAll()
        self.assertEqual(len(all), 1)


    def test_remove_client(self):
        self.__client_controller.createclient(1,"name")
        self.__client_controller.remove(1)
        all = self.__client_controller.getAll()
        self.assertEqual(len(all), 0)

    def test_update_client(self):
        self.__client_controller.createclient(1,"name")
        self.__client_controller.update(1,"newname")
        all = self.__client_controller.getAll()
        self.assertEqual(all[0].gettname,"newname")

    def test_find(self):
        self.__client_controller.createclient(1, "name")
        client = self.__client_controller.searchid(1)
        self.assertEqual(client.gettname, "name")

###############Rentals########################

    def test_add_rental(self):
        rent_date = datetime.date(1, 1, 1)
        due_date = datetime.date(5, 5, 5)
        self.__rental_controller.createRental(2, 2, 2, rent_date, due_date)
        allrent = self.__rental_controller.getAll()
        self.assertEqual(len(allrent),1)

    def test_remove_rental(self):
        rent_date = datetime.date(1, 1, 1)
        due_date = datetime.date(5, 5, 5)
        self.__rental_controller.createRental(2, 2, 2, rent_date, due_date)
        allrent = self.__rental_controller.getAll()
        self.assertEqual(len(allrent), 1)
        self.__rental_controller.removeRental(2)
        allrent = self.__rental_controller.getAll()
        self.assertEqual(len(allrent), 0)


