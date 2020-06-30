from common.common import arr_to_sort
from common.common import swap

print(arr_to_sort)


def insertion_sort(arr):
    i = 1
    while i < len(arr):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            swap(arr, j, j - 1)
            j -= 1
        i += 1


insertion_sort(arr_to_sort)
print(arr_to_sort)
