arr_to_sort = [66, 67, 22, 84, 1, 3, 7, 17, 34, 24, 99, 76, 57]
print(arr_to_sort)


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


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
