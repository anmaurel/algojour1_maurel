# -- coding: utf-8 --
from get_arguments import getArgs
import time

array = getArgs()
begin_time = time.time()

def quick_sort(array, low, high):
    
    if low < high:
        ps = partition(array, low, high)
        quick_sort(array, low, ps - 1)
        quick_sort(array, ps + 1, high)

def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for val in range(low, high):
        if array[val] <= pivot:
            i = i + 1
            array[i], array[val] = array[val], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1


print("Série", array, sep=" : ")
quick_sort(array, 0, len(array) - 1)
print("Résultat", array, sep=" : ")
print("Nombre de comparaisons", '0', sep=" : ")
print("Temps (sec)", time.time() - begin_time, sep=" : ")