arr_to_sort = [66, 67, 22, 84, 1, 3, 7, 17, 34, 24, 99, 76, 57]
print(arr_to_sort)


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


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
