from common.common import swap
from common.common import arr_to_sort

print(arr_to_sort)


def heapify(arr, n, i):
    _max = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[i]:
        _max = left

    if right < n and arr[right] > arr[_max]:
        _max = right

    if _max != i:
        swap(arr, _max, i)
        heapify(arr, n, _max)


def heap_sort(arr):
    n = len(arr)

    i = (n - 1) // 2
    while i >= 0:
        heapify(arr, n, i)
        i -= 1

    i = n - 1
    while i > 0:
        swap(arr, i, 0)
        heapify(arr, i, 0)
        i -= 1


heap_sort(arr_to_sort)

print(arr_to_sort)

print((7 - 1) // 2)
print(7 // 2 - 1)
