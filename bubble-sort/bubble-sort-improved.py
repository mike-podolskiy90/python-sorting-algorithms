from common.common import arr_to_sort
from common.common import swap

print(arr_to_sort)


def bubble_sort(arr):
    n = len(arr)
    for j in range(n - 1):
        for i in range(0, n - j - 1):
            if arr[i] > arr[i + 1]:
                swap(arr, i, i + 1)


bubble_sort(arr_to_sort)
print(arr_to_sort)
