from get_arguments import getArgs

tab = getArgs()

gap = len(tab)
swaps = True
while gap > 1 or swaps:
    gap = max(1, int(gap / 1.3))
    swaps = False
    for i in range(len(tab) - gap):
        j = i+gap
        if tab[i] > tab[j]:
            tab[i], tab[j] = tab[j], tab[i]
            swaps = True
 
print (tab)