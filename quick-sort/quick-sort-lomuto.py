arr_to_sort = [66, 67, 22, 84, 1, 3, 7, 17, 34, 24, 99, 76, 57]
print(arr_to_sort)


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def partition(arr, low, high):
    i = low
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            swap(arr, i, j)
            i += 1

    swap(arr, i, high)
    return i


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


quick_sort(arr_to_sort, 0, len(arr_to_sort) - 1)

print(arr_to_sort)

