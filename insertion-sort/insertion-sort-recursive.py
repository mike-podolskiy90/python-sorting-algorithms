from common.common import arr_to_sort

print(arr_to_sort)


def insertion_sort(arr, n):
    if n > 0:
        insertion_sort(arr, n - 1)
        x = arr[n]
        j = n - 1
        while j >= 0 and arr[j] > x:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = x


insertion_sort(arr_to_sort, len(arr_to_sort) - 1)
print(arr_to_sort)
