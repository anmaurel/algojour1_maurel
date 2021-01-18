import time
from get_arguments import getArgs
from print_properties import printProperties
tab = getArgs()

start_time = time.time()

ite=0
comp=0

gap = len(tab)
swaps = True
while gap > 1 or swaps:
    gap = max(1, int(gap / 1.3))
    swaps = False
    ite+=1
    for i in range(len(tab) - gap):
        j = i+gap
        ite+=1
        if tab[i] > tab[j]:
            tab[i], tab[j] = tab[j], tab[i]
            swaps = True
            comp+=1
 
printProperties(getArgs(), tab, comp, ite, (time.time() - start_time))
