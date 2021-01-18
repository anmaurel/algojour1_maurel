# -- coding: utf-8 --
from get_arguments import getArgs
from print_properties import printProperties
import time

array = getArgs()
begin_time = time.time()

def quick_sort(array, low, high):
    nb_total_comparaison = 0

    if low < high:
        ps = partition(array, low, high)[0]
        nb_total_comparaison += partition(array, low, high)[1]
        quick_sort(array, low, ps - 1)
        quick_sort(array, ps + 1, high)
    
    return [nb_total_comparaison]

def partition(array, low, high):
    nb_comparison = 0

    pivot = array[high]
    i = low - 1

    for val in range(low, high):
        if array[val] <= pivot:
            i = i + 1
            array[i], array[val] = array[val], array[i]
            nb_comparison += 1

    array[i + 1], array[high] = array[high], array[i + 1]
    nb_comparison += 1

    return [i + 1, nb_comparison]

  
result = quick_sort(array, 0, len(array) - 1)
printProperties(getArgs(), array, result[0], None, (time.time() - begin_time))
