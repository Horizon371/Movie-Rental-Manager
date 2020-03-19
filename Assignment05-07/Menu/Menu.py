from Domain.Entities import *
import datetime


class UI:
    def __init__(self, movie_controller, client_controlller, rental_controller, repositorymovie, repositoryclient,repositoryrental,operationManager):
        self.__repositorymovie = repositorymovie
        self.__repositoryclient = repositoryclient
        self.__repositoryrental = repositoryrental
        self.__movie_controller = movie_controller
        self.__client_controller = client_controlller
        self.__rental_controller = rental_controller
        self.__operationManager = operationManager

    def menu(self):

        while True:
            try:
                UI.print_menu()

                command_menu = input("Enter a command: ")
                if command_menu == "0":
                    print("Exited")
                    return False

                if command_menu == "1":
                    UI.print_movie_menu()
                    command = input("Enter another command: ")

                    if command == "1":
                        UI.create_movie(self)

                    if command == "2":
                        print(" ")
                        for index in self.__movie_controller.getAll():
                            print(str(index))
                        print(" ")

                    if command == "3":
                        movieId = int(input("Enter movie Id: "))
                        self.__movie_controller.remove(movieId)


                    if command == "4":
                        movieId = int(input("Enter movie Id: "))
                        newtitle = input("Enter new title: ")
                        newgenre = input("Enter new genre: ")
                        newdescription = input("Enter new description: ")
                        self.__movie_controller.update(movieId, newtitle, newgenre, newdescription)

                elif command_menu == "2":

                    UI.print_client_menu()
                    command = input("Enter another command: ")

                    if command == "1":
                        UI.create_client(self)

                    if command == "2":
                        print(" ")
                        for index in self.__client_controller.getAll():
                            print(str(index))
                        print(" ")

                    if command == "3":
                        clientId = int(input("Enter client Id: "))
                        self.__client_controller.remove(clientId)

                    if command == "4":
                        clientId = int(input("Enter client Id: "))
                        newname = input("Enter new name: ")
                        self.__client_controller.update(clientId, newname)


                elif command_menu == "3":

                    UI.print_rental_menu()
                    command = input("Enter another command: ")

                    if command == "1":
                        UI.create_rental(self)

                    if command == "3":
                        rentalId = int(input("Rental id: "))
                        self.__rental_controller.removeRental(rentalId)

                    if command == "2":
                        rentalId = int(input("Rental id: "))
                        date = datetime.date.today()
                        print(date)
                        self.__rental_controller.returnmovie(rentalId, date)

                    if command == "4":
                        for index in self.__rental_controller.getAll():
                            print(index)
                        print(" ")


                elif command_menu == "4":
                    UI.search_menu()
                    command = input("Enter a command: ")

                    if command == "1":
                        movieid = int(input("Enter movie id: "))
                        print(self.__movie_controller.searchid(movieid))
                        print(" ")

                    if command == "2":
                        movietitle = input("Enter movie title: ")
                        for index in self.__movie_controller.getAll():
                            if movietitle.lower() in index.gettitle.lower():
                                print(index)
                        print(" ")

                    if command == "3":
                        moviegenre = input("Enter movie genre: ")
                        for index in self.__movie_controller.getAll():
                            if moviegenre.lower() in index.getgenre.lower():
                                print(str(index))
                        print(" ")

                    if command == "4":
                        moviedescription = input("Enter movie description: ")
                        for index in self.__movie_controller.getAll():
                            if moviedescription.lower() in index.getdescription.lower():
                                print(str(index))
                        print(" ")

                    if command == "5":
                        clientid = int(input("Enter client id: "))
                        print(self.__client_controller.searchid(clientid))
                        print(" ")

                    if command == "6":
                        clientName = input("Enter client name: ")
                        for index in self.__client_controller.getAll():
                            if clientName.lower() in index.gettname.lower():
                                print(str(index))

                        print(" ")
                elif command_menu == "5":
                    UI.print_statistics_menu()
                    command = input("Enter a command: ")

                    if command == "1":
                        print(" ")
                        for index in self.__rental_controller.most_times_rented_movie():
                            print(index)

                    if command == "2":
                        print(" ")
                        for index in self.__rental_controller.most_days_rented_movie():
                            print(index)

                    if command == "3":
                        print(" ")
                        for index in self.__rental_controller.all_rentals():
                            print(index)

                    if command == "4":
                        print(" ")
                        for index in self.__rental_controller.late_rentals():
                            print(index)

                    if command == "5":
                        print(" ")
                        for index in self.__rental_controller.most_active_clients():
                            print(index)

                elif command_menu == "6":
                    self.__operationManager.undo()

                elif command_menu == "7":
                    self.__operationManager.redo()


                else:
                    print("Invalid command")
            except Exception as exception:
                print("Please try again: " + str(exception))

###############################################################################################################################################


    def create_client(self):
        try:
            clientId = int(input("Enter client Id: "))
            if self.__repositoryclient.find(clientId) != None:
                print("Client id already exists")
                raise Exception
            name = input("Enter client name: ")

        except ValueError:
            print("ValueError")

        self.__client_controller.createclient(clientId, name)


    def create_movie(self):
        try:
            movieId = int(input("Enter movie Id: "))
            if self.__repositorymovie.find(movieId) != None:
                print("Movie id already exists")
                raise Exception
            title = input("Enter movie title: ")
            description = input("Enter movie description: ")
            genre = input("Enter movie genre: ")

        except ValueError:
            print("Value Error")

        self.__movie_controller.createmovie(movieId, title, description, genre)


    def create_rental(self):
        rentalId = int(input("Rental id: "))
        if self.__repositoryrental.find(rentalId) != None:
            print("rental id already exists")
            raise Exception
        clientId = int(input("Client id: "))
        movieId = int(input("Movie id: "))
        for index in self.__repositoryrental.getAll():
            if index.getmovieId == movieId and index.getrented_date == None:
                print("Movie is rented")
                raise Exception

        test =False
        for index in self.__repositorymovie.getAll():
            if index.getId == movieId:
                test = True
        if test == False:
            print("Movie doesn`t exist")
            raise Exception

        test = False
        for index in self.__repositoryclient.getAll():
            if index.getId == clientId:
                test = True
        if test == False:
            print("Client doesn`t exist")
            raise Exception

        print("Enter rented date: ")
        year = int(input("Enter year: "))
        month = int(input("Enter month: "))
        day = int(input("Enter day: "))
        rented_date = datetime.date(year, month, day)

        print("Enter due date: ")
        year1 = int(input("Enter year: "))
        month1 = int(input("Enter month: "))
        day1 = int(input("Enter day: "))
        due_date = datetime.date(year1, month1, day1)

        self.__rental_controller.createRental(rentalId, clientId, movieId, rented_date, due_date)



    def print_movies(self, seq):
        for movieId in seq:
            Movie = self.__repositorymovie.find(movieId)
            print(str(Movie))


    def print_clients(self, seq):
        for clientId in seq:
            Client = self.__repositoryclient.find(clientId)
            print(str(Client))

    @staticmethod
    def search_menu():
        print("1:Search movies by id")
        print("2:Search movies by title")
        print("3:Search movies by genre")
        print("4:Search movies by description")
        print("5:Search clients by id")
        print("6:Search clients by name")

    @staticmethod
    def print_menu():

        print(" ")
        print("1:Manage Movies")
        print("2:Manage Clients")
        print("3:Manage Rentals")
        print("4:Search")
        print("5:Statistics")
        print("6:Undo")
        print("7:Redo")
        print("0:Exit")
        print(" ")

    @staticmethod
    def print_statistics_menu():
        print("1:Most rented movies (times)")
        print("2:Most rented movies (days)")
        print("3:All rentals")
        print("4:Late rentals")
        print("5:Most active clients")


    @staticmethod
    def print_movie_menu():
        print("1:Add movie")
        print("2:List movies")
        print("3:Remove movie")
        print("4:Update movie")
        print(" ")

    @staticmethod
    def print_client_menu():
        print("1:Add client")
        print("2:List clients")
        print("3:Remove client")
        print("4:Update client")
        print(" ")

    @staticmethod
    def print_rental_menu():
        print("1:Rent movie")
        print("2:Return movie")
        print("3:Remove rental")
        print("4:List Rentals")
        print(" ")