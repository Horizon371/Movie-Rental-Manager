
from Domain.Entities import client

class ClientFileRepo:


    def __init__(self, clientRepository, fileName):
        self.__fileName = fileName
        self.__clientRepository = clientRepository
        self.loadFromFile()



    def add(self,client):
        if self.find(client.getId) == None:
            self.__clientRepository.add(client)
            self.writeToFile()

    def update(self,oldClient,newClient):
        self.__clientRepository.update(oldClient,newClient)
        self.writeToFile()

    def find(self,clientId):
        return self.__clientRepository.find(clientId)


    def getAll(self):
        return self.__clientRepository.getAll()


    def remove(self,client):
        self.__clientRepository.remove(client)
        self.writeToFile()


    def loadFromFile(self):
        try:
            f = open(self.__fileName, "r")
            line = f.readline().strip()
            while len(line) > 0:
                line = line.split(";")
                self.__clientRepository.add(client(int(line[0]),line[1]))
                line = f.readline().strip()
            f.close()

        except IOError as e:
            print("Error: ")
            raise e

    def writeToFile(self):
        f = open(self.__fileName, "w")
        try:
            for client in self.__clientRepository.getAll():
                stringClient = str(client.getId) + ";" + client.gettname + "\n"
                f.write(stringClient)
            f.close()
            
        except IOError as e:
            print("Error: ")
            raise e





