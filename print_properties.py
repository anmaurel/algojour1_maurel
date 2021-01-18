def printProperties(args, tab, comp, ite, temps):
    print("Série :", args)
    print("Résultat :", tab) 
    print("Nombre de comparaisons :", comp)
    if ite :
        print("Nombre d'itérations :", ite)
    print("Temps (sec) :", "{:.2f}".format(temps))