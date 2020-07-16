arr_to_sort = [66, 67, 22, 84, 13, 15, 7, 17, 34, 24, 99, 76, 56, 14, 1, 3, 57, 98, 93, 92, 32, 37, 90, 73, 75, 74, 2, 0, 5, 11, 80, 45, 54, 55, 59, 29, 100, 97, 8, 12, 9, 6, 4]


def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        x = arr[i]
        j = i - 1
        while arr[j] > x and j >= left:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = x


def merge(arr, left_arr, right_arr):
    i = j = k = 0

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1


def tim_sort(arr):
    run = 32
    n = len(arr)

    for i in range(0, n, run):
        insertion_sort(arr, i, min(i + 31, n - 1))

    size = run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = left + size - 1
            right = min(left + 2 * size - 1, n - 1)

            left_arr = arr[left:mid + 1]
            right_arr = arr[mid + 1:right + 1]

            merge(arr, left_arr, right_arr)

        size = 2 * size


tim_sort(arr_to_sort)

print(arr_to_sort)
