import time
from get_arguments import getArgs
from print_properties import printProperties
tab = getArgs()

start_time = time.time()

ite=0
comp=0

for i in range(len(tab)):
    ite+=1
    for j in range(0, len(tab)-i-1):
        ite+=1
        if tab[j] > tab[j+1] :
            tab[j], tab[j+1] = tab[j+1], tab[j]
            comp+=1
 
printProperties(getArgs(), tab, comp, ite, (time.time() - start_time))