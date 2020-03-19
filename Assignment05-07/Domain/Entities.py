
class movie:
    def __init__(self, movieId, title, description, genre):
        self.__movieId = movieId
        self.__title = title
        self.__description = description
        self.__genre = genre

    @property
    def getId(self):
        return self.__movieId

    @property
    def gettitle(self):
        return self.__title


    def set_title(self, value):
        self.__title=value

    @property
    def getdescription(self):
        return self.__description


    def set_description(self, value):
        self.__description=value

    @property
    def getgenre(self):
        return self.__genre


    def set_genre(self, value):
        self.__genre=value

    def __str__(self):
        return "Id:" + str(self.__movieId) +", " +" Title:"+ self.__title  +", " + " Genre:"+self.__genre +", "  + " Desciption:"+self.__description


class client:
    def __init__(self, clientId, name):
        self.__clientId = clientId
        self.__name = name

    @property
    def getId(self):
        return self.__clientId

    @property
    def gettname(self):
        return self.__name

    def __str__(self):
        return "Id:" + str(self.__clientId) + " ," + " Name:" + self.__name

class rental:
    def __init__(self, rentalId, clientId, movieId, rented_date, due_date, returned_date):
        self.__rentalId = rentalId
        self.__rented_date = rented_date
        self.__due_date = due_date
        self.__clientId = clientId
        self.__movieId = movieId
        self.__returned_date = returned_date

    @property
    def getmovieId(self):
        return self.__movieId


    @property
    def getId(self):
        return self.__rentalId


    @property
    def getrented_date(self):
        return self.__rented_date

    @property
    def getdue_date(self):
        return self.__due_date

    @property
    def getreturned_date(self):
        return self.__returned_date

    def setreturned_date(self,value):
        self.__returned_date = value

    @property
    def getclientId(self):
        return self.__clientId

    def __str__(self):
        return "rentalId:" + str(self.__rentalId) + " clientId:" + str(self.__clientId) + " movieId:" + str(self.__movieId) + " rented_date:" + str(self.__rented_date) + " due_date:" + str(self.__due_date) + " returned_date:" + str(self.__returned_date)