# -- coding: utf-8 --
from get_arguments import getArgs
from print_properties import printProperties
import time

array = getArgs()
begin_time = time.time()

def merge_sort(array):
    nb_comparison = 0

    if len(array) > 1:

        middle = len(array) // 2
        left_copy = array[:middle]
        right_copy = array[middle:]

        merge_sort(left_copy)
        merge_sort(right_copy)

        left_copy_index = 0
        right_copy_index = 0
        sorted_index = 0

        while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

            if left_copy[left_copy_index] <= right_copy[right_copy_index]:
                array[sorted_index] = left_copy[left_copy_index]
                nb_comparison += 1
                left_copy_index = left_copy_index + 1

            else:
                array[sorted_index] = right_copy[right_copy_index]
                nb_comparison += 1
                right_copy_index = right_copy_index + 1

            sorted_index = sorted_index + 1

        while left_copy_index < len(left_copy):
            array[sorted_index] = left_copy[left_copy_index]
            nb_comparison += 1
            left_copy_index = left_copy_index + 1
            sorted_index = sorted_index + 1

        while right_copy_index < len(right_copy):
            array[sorted_index] = right_copy[right_copy_index]
            nb_comparison += 1
            right_copy_index = right_copy_index + 1
            sorted_index = sorted_index + 1

    return [nb_comparison]


result = merge_sort(array)
printProperties(getArgs(), array, result[0], None, (time.time() - begin_time))
