
from UndoRedo.Managers import *
from UndoRedo.Handlers import *

class ClientController:
    def __init__(self, repository, validator,operationManager):
        self.__repository = repository
        self.__validator = validator
        self.__operationManager = operationManager
        self.__handler = handler(repository)

    def createclient(self,clientId, name):
        Client = client(clientId, name)
        self.__validator.validate_client(Client)
        self.__repository.add(Client)


        undoOperation = operation(self.__handler.removeClientHandler, clientId)
        redoOperation = operation(self.__handler.createClientHandler, clientId, name)
        operations = undoRedoOperations(undoOperation, redoOperation)
        self.__operationManager.addOperation(operations)


    def remove(self,clientId):
        client = self.__repository.find(clientId)
        self.__repository.remove(client)

        undoOperation = operation(self.__handler.createClientHandler, clientId, client.gettname)
        redoOperation = operation(self.__handler.removeClientHandler, clientId)
        operations = undoRedoOperations(undoOperation, redoOperation)
        self.__operationManager.addOperation(operations)


    def getAll(self):
        return self.__repository.getAll()

    def update(self,clientId,newname):
        oldclient = self.__repository.find(clientId)
        newclient = client(clientId,newname)
        self.__repository.update(oldclient,newclient)

    def searchid(self,clientId):
        return self.__repository.find(clientId)