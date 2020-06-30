from common.common import arr_to_sort
from common.common import swap

print(arr_to_sort)


def selection_sort(arr):
    for i in range(len(arr) - 1):
        j_min = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[j_min]:
                j_min = j

        if j_min != i:
            swap(arr, i, j_min)


selection_sort(arr_to_sort)
print(arr_to_sort)
