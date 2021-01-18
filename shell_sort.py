# -- coding: utf-8 --
from get_arguments import getArgs
from print_properties import printProperties
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
            nb_comparison += 1

        interval //= 2
    
    return [nb_comparison, nb_iteration]


result = shell_sort(array, len(array))
printProperties(getArgs(), array, result[0], result[1], (time.time() - begin_time))