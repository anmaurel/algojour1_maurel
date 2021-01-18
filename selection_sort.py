# -- coding: utf-8 --

from get_arguments import getArgs
from print_properties import printProperties
tab = getArgs()
import time
start_time = time.time()
comp = 0
ite = 0
for i in range(len(tab)):
    min = i
    for j in range(i+1, len(tab)):
        if tab[min] > tab[j]:
            min = j
        comp += 1
    tmp = tab[i]
    tab[i] = tab[min]
    tab[min] = tmp
    ite += 1
printProperties(getArgs(), tab, comp, ite, (time.time() - start_time))