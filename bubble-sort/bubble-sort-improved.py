arr_to_sort = [66, 67, 22, 84, 1, 3, 7, 17, 34, 24, 99, 76, 57]
print(arr_to_sort)


def bubble_sort(arr):
    n = len(arr)
    for j in range(n - 1):
        for i in range(0, n - j - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


bubble_sort(arr_to_sort)
print(arr_to_sort)
