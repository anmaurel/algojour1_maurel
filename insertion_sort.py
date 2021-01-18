# -- coding: utf-8 --

from get_arguments import getArgs
tab = getArgs()
import time
start_time = time.time()
comp = 0
ite = 0
print("Série", tab, sep=" : ")
for step in range(1, len(tab)):
    key = tab[step]
    j = step - 1  
    while j >= 0 and key < tab[j]:
        tab[j + 1] = tab[j]
        j -= 1
        ite += 1
    tab[j + 1] = key
    comp += 1
print("Résultat", tab, sep=" : ") 
print("Nombre de comparaisons", comp, sep=" : ")
print("Nombre d'itérations", ite, sep=" : ")
print("Temps (sec)", "{:.2f}".format(time.time() - start_time), sep=" : ")