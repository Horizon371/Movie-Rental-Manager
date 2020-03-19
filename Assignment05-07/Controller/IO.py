def readfile(fileName):
    result = []
    try:
        f = open(fileName,"r")
        line = f.readline().strip()
        while len(line) > 0
            line = line.split(" ")
            result.append(obj)
            line = f.readline().strip()

        f.close()
    except IOError:
        print("dfsdf")

    return result


    def readFile(fileName):
        result = []
        try:
            f = open(fileName, "r")
            line = f.readline().strip()
            while len(line) > 0:
                line = line.split(",")
                result.append(student(int(line[0]), line[1], int(line[2]), int(line[3])))
                line = f.readline().strip()
            f.close()
        except IOError as e:
            print("An error accured" + str(e))
            raise e

        return result