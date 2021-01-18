import sys

arg = sys.argv

def getArgs():
    if len(arg) == 1:
        raise ValueError("No arguments given")
    elif len(arg) == 2:
        listArguments = arg[1].replace(" ", "").replace(",", ".").split(";")
        listInt = []
        for i in range(len(listArguments)):
            isInt = False
            try:
                val = float(listArguments[i])
                isInt = True
            except ValueError:
                raise ValueError(listArguments[i], 'is not a number.') 
            if isInt:
                listInt.append(val)
        return listInt
    else:
        raise ValueError('Invalid argument. Example of valid argument: "26;89;-3"')
