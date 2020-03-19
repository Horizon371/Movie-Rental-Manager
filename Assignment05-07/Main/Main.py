import configparser
import random
from Menu.Menu import*
from Controller.MovieController import *
from Controller.ClientController import *
from Controller.RentalController import *
from Validators.Validators import *
from UndoRedo.Managers import *
from Repo.ClientFileRepo import *
from Repo.MovieFileRepo import *
from Repo.RentalFileRepo import *
from Repo.RentalPickleFile import*
from Repo.MoviePickleFile import*
from Repo.ClientPickleRepo import*


OperationManager = operationManager()

config = configparser.ConfigParser()
config.read("config.ini")

Validatormovie = movie_validator()
Validatorclient = client_validator()
Validatorrental = rental_validator()

Repositorymovie = repo()
Repositoryclient = repo()
Repositoryrental = repo()
clientRepo = None
movieRepo = None
rentalRepo = None
config = configparser.ConfigParser()
config.read("D:\PycharmProjects\Assignment05-07\config.ini")

memory = 0
if config['DEFAULT']["repository"] == "inmemory":
    memory = 1
    clientRepo = Repositoryclient
    movieRepo = Repositorymovie
    rentalRepo = Repositoryrental


elif config['DEFAULT']["repository"] == "file":

    clientRepo = ClientFileRepo(Repositoryclient, config["DEFAULT"]["clients"])
    movieRepo = MovieFileRepo(Repositorymovie, config["DEFAULT"]["movie"])
    rentalRepo = RentalFileRepo(Repositoryrental, config["DEFAULT"]["rental"])


elif config['DEFAULT']["repository"] == "binary":

    clientRepo = ClientPickleRepo(config["DEFAULT"]["clients"])
    movieRepo = MoviePickleRepo(config["DEFAULT"]["movie"])
    rentalRepo = RentalPickleRepo(config["DEFAULT"]["rental"])




movie_controller = MovieController(movieRepo, Validatormovie, OperationManager)
client_controller = ClientController(clientRepo, Validatorclient, OperationManager)
rental_controller = RentalController(rentalRepo, Validatorrental, movie_controller, client_controller)

if memory == 1 :
    name1 = ["Cristian ", "Andreea ", "John ", "Laurentiu ", "Andrei ", "Ionut "]
    name2 = ["Pop", "Smith", "Papascadopulus", "Sorescu", "Popescu", "Trandafir"]
    title1 = ["The life of ", "The adventures of ", "Get ", "After ", "Captain "]
    title2 = ["John", "Narnia", "Earth", "Spiderman", "Papascadopulus", "Unknown"]
    descripitionn = ["cool", "coolest movie ever", "dramatic", "esquisite", "best movie in hisory"]
    genree = ["Action", "Anime", "Adventure", "Mistery", "Fantastic"]


    for i in range (1,101):
        title = random.choice(title1) + random.choice(title2)
        descripition = random.choice(descripitionn)
        genre = random.choice(genree)
        name = random.choice(name1) + random.choice(name2)


        year = random.randint(2016, 2018)
        month = random.randint(1, 7)
        day = random.randint(1, 28)
        rented_date = datetime.date(year, month, day)

        if month < 12:
            due_date = datetime.date(year,month + 1,day)
        else:
            due_date = datetime.date(year + 1,1,day)

        movie_controller.createmovie(i, title, descripition, genre)
        client_controller.createclient(i, name)
        rental_controller.createRental(i, i, i, rented_date, due_date)


ui=UI(movie_controller,client_controller,rental_controller,movieRepo,clientRepo,Repositoryrental,OperationManager)

ui.menu()

