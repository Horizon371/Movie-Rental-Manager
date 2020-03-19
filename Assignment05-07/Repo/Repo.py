class repo:
    def __init__(self):
        self.__data=[]

    def add(self,object):
        self.__data.append(object)

    def remove(self,object):
        self.__data.remove(object)

    def update(self,old_object,new_object):
        for index in range (0,len(self.__data)):
            if self.__data[index]==old_object:
                self.__data.remove(old_object)
                self.__data.insert(index,new_object)

    def find (self,objectid):
        for index in range(len(self.__data)):
            if self.__data[index].getId == objectid:
                return self.__data[index]
        return None


    def getAll(self):
        return self.__data








