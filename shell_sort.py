# -- coding: utf-8 --
from get_arguments import getArgs
import time

array = getArgs()
begin_time = time.time()

def shell_sort(array, length):
    nb_comparison = 0
    nb_iteration = 0
    
    interval = length // 2

    while interval > 0:
        nb_iteration += 1

        for i in range(interval, length):
            nb_iteration += 1

            temp = array[i]
            val = i

            while val >= interval and array[val - interval] > temp:
                nb_iteration += 1

                array[val] = array[val - interval]
                val -= interval

            array[val] = temp

        interval //= 2
        nb_comparison += 1
    
    return [nb_comparison, nb_iteration]


print("Série", array, sep=" : ")
shell_sort(array, len(array))
print("Résultat", array, sep=" : ")
print("Nombre de comparaison", shell_sort(array, len(array))[0], sep=" : ")
print("Nombre d'itération", shell_sort(array, len(array))[1], sep=" : ")
print("Temps (sec)", time.time() - begin_time, sep=" : ")