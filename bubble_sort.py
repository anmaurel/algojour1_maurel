from get_arguments import getArgs

tab = getArgs()

for i in range(len(tab)):
    for j in range(0, len(tab)-i-1):
        if tab[j] > tab[j+1] :
            tab[j], tab[j+1] = tab[j+1], tab[j]
 
print (tab)