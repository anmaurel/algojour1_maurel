# -- coding: utf-8 --

from get_arguments import getArgs
tab = getArgs()
import time
start_time = time.time()
comp = 0
ite = 0
print "Série :", tab
for i in range(len(tab)):
    min = i
    for j in range(i+1, len(tab)):
        if tab[min] > tab[j]:
            min = j
            ite += 1
    tmp = tab[i]
    tab[i] = tab[min]
    tab[min] = tmp
    comp += 1
print "Résultat :", tab
print "Nombre de comparaisons :", comp
print "Nombre d'itérations :", ite
print "Temps (sec) : ", "{:.2f}".format(time.time() - start_time)