class undoRedoOperations:

    def __init__(self,undoOperation,redoOperation):
        self.__undoOperation = undoOperation
        self.__redoOperation = redoOperation

    def undoOperation(self):
        self.__undoOperation.execute()

    def redoOperation(self):
        self.__redoOperation.execute()

class operation:
    def __init__(self,operation,*parameters):
        self.__operation = operation
        self.__paramteres = parameters

    def execute(self):
        self.__operation(*self.__paramteres)

class operationManager:
    def __init__(self):
        self.__undoList = []
        self.__redoList = []


    def addOperation(self,operation):
        self.__undoList.append(operation)
        self.__redoList = []

    def undo(self):
        if len(self.__undoList) == 0:
            raise Exception("Cannot undo")
        operation = self.__undoList.pop()
        print(len(self.__undoList))
        operation.undoOperation()
        self.__redoList.append(operation)


    def redo(self):
        if len(self.__redoList) == 0:
            raise Exception("Cannot redo")
        print(len(self.__redoList))
        operation = self.__redoList.pop()
        operation.redoOperation()
        self.__undoList.append(operation)



