arr_to_sort = [66, 67, 22, 84, 1, 3, 7, 17, 34, 24, 99, 76, 57]
print(arr_to_sort)


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


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
