class late_rentals:
    def __init__(self,movieid,delay):
        self.__movieid = movieid
        self.__delay = delay

    @property
    def getId(self):
        return self.__movieid

    @getId.setter
    def getId(self, value):
        pass

    @property
    def getdelay(self):
        return self.__delay

    @getdelay.setter
    def getdelay(self, value):
        pass

    def __str__(self):
        return "movieId:" + str(self.__movieid) + ", " + " delay:" + str(self.__delay)

class moviedto:
    def __init__(self,movieid,movietitle,count):
        self.__movieid = movieid
        self.__movietitle = movietitle
        self.__count = count
    @property
    def id(self):
        return self.__movieid
    
    @id.setter
    def id(self, value):
        pass
    
    @property
    def movietitle(self):
        return self.__movietitle
    
    @movietitle.setter
    def movietile(self, value):
        pass
    
    @property
    def getcount(self):
        return self.__count
    
    @getcount.setter
    def count(self, value):
        pass

    def __str__(self):
        return "movieId:" + str(self.__movieid) + ", " + " movietitle:" + self.__movietitle + ", " + " count:" + str(self.__count)


class clientdto:
    def __init__(self,clientid,name,count):
        self.__clientid = clientid
        self.__name = name
        self.__count = count
        
    @property
    def id(self):
        return self.__clientid

    @id.setter
    def id(self, value):
        pass

    @property
    def gettname(self):
        return self.__name

    @gettname.setter
    def name(self, value):
        pass

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, value):
        pass

    def __str__(self):
        return "clientId:"+  str(self.__clientid) + ", " +" clientName:" + self.__name + ", "  " count:" + str(self.__count)

class rentaldto:
    def __init__(self,movieId,clientId,number_of_rentals,days_rented):
        self.__movieId = movieId
        self.__number_of_rentals = number_of_rentals
        self.__days_rented = days_rented

        self.__clientId = clientId

    @property
    def Id(self):
        return self.__movieId

    @Id.setter
    def Id(self, value):
        pass

    @property
    def getnumber_of_rentals(self):
        return self.__number_of_rentals

    @getnumber_of_rentals.setter
    def setnumber_of_rentals(self,value):
        self.__number_of_rentals = value

    @property
    def getrented_days(self):
        return self.__days_rented

    @getrented_days.setter
    def setrented_days(self, value):
        self.__days_rented = value
