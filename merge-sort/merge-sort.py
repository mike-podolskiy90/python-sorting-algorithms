from common.common import arr_to_sort

print(arr_to_sort)


def merge(arr, left, right):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2

        left = arr[:middle]
        right = arr[middle:]

        merge_sort(left)
        merge_sort(right)
        merge(arr, left, right)


merge_sort(arr_to_sort)
print(arr_to_sort)
