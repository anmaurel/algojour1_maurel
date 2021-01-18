import sys

arg = sys.argv

def getArgs():
    if len(arg) == 1:
        raise ValueError("No arguments given")
    elif len(arg) == 2:
        listArguments = arg[1].replace(" ", "").replace(",", ".").split(";")
        listNumber = []
        for i in range(len(listArguments)):
            isNumber = False
            try:
                val = float(listArguments[i])
                if val % 1 == 0:
                    val = int(val)
                isNumber = True
            except ValueError:
                raise ValueError(listArguments[i], 'is not a number.') 
            if isNumber:
                listNumber.append(val)
        return listNumber
    else:
        raise ValueError('Invalid argument. Example of valid argument: "26;89;-3"')