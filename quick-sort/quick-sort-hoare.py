arr_to_sort = [66, 67, 22, 84, 1, 3, 7, 17, 34, 24, 99, 76, 57]
print(arr_to_sort)


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def partition(arr, low, high):
    pivot = arr[(low + high) // 2]
    i,j  = low, high

    while True:
        while arr[i] < pivot:
            i += 1

        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        swap(arr, i, j)


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi)
        quick_sort(arr, pi + 1, high)


quick_sort(arr_to_sort, 0, len(arr_to_sort) - 1)

print(arr_to_sort)
