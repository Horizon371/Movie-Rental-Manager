class RentalException(Exception):
    def __init__(self,msg):
        self.__msg = msg

    def getMessage(self):
        return self.__msg

    def __str__(self):
        return self.__msg


