# -- coding: utf-8 --

from get_arguments import getArgs
from print_properties import printProperties
tab = getArgs()
import time
start_time = time.time()
comp = 0
ite = 0
for step in range(1, len(tab)):
    key = tab[step]
    j = step - 1  
    while j >= 0 and key < tab[j]:
        tab[j + 1] = tab[j]
        j -= 1
        comp += 1
    tab[j + 1] = key
    ite += 1
printProperties(getArgs(), tab, comp, ite, (time.time() - start_time))