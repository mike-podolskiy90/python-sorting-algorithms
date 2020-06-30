arr_to_sort = [66, 67, 22, 84, 1, 3, 7, 17, 34, 24, 99, 76, 57]
print(arr_to_sort)


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def partition(arr, low, high):
    pivot_index = (low + high) // 2
    pivot = arr[pivot_index]
    print("Pivot = arr[{}] = {}".format(pivot_index, pivot))
    i, j = low, high

    while True:
        while arr[i] < pivot:
            i += 1

        while arr[j] > pivot:
            j -= 1

        if i >= j:
            print("Partition index: {}".format(j))
            return j

        print("Swapped arr[{}]={} and arr[{}]={}".format(i, arr[i], j, arr[j]))
        swap(arr, i, j)
        print(arr)


def quick_sort(arr, low, high):
    print("_______________________")
    print(arr)
    print("Low: {}, high: {}".format(low, high))
    if low < high:
        print("***Start partitioning***")
        pi = partition(arr, low, high)
        print("***End partitioning***")

        print("After partitioning: {}".format(arr))

        print("Next steps: sort({},{}), sort({},{})".format(low, pi, pi + 1, high))
        quick_sort(arr, low, pi)
        quick_sort(arr, pi + 1, high)


quick_sort(arr_to_sort, 0, len(arr_to_sort) - 1)

print("_______________________")
print(arr_to_sort)
