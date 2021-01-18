import sys

arg = sys.argv

def getArgs():
    if len(arg) == 1:
        raise ValueError("No arguments given")
    elif len(arg) == 2:
        listArguments = arg[1].replace(" ", "").replace(",", ".").split(";")
        listFloat = []
        for i in range(len(listArguments)):
            isFloat = False
            try:
                val = float(listArguments[i])
                isFloat = True
            except ValueError:
                raise ValueError(listArguments[i], 'is not a number.') 
            if isFloat:
                listFloat.append(val)
        return listFloat
    else:
        raise ValueError('Invalid argument. Example of valid argument: "26;89;-3"')
