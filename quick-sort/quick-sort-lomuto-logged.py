arr_to_sort = [3, 5, 11, 9, 0, 7, 1, 6, 23]
print(arr_to_sort)


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def partition(arr, low, high):
    pivot = arr[high]
    print("Pivot = arr[{}] = {}".format(high, pivot))
    i = low

    for j in range(low, high):
        print("Check arr[j] is less than pivot: arr[{}] = {} < {}? => {}".format(j, arr[j], pivot, arr[j] < pivot))
        if arr[j] < pivot:
            print("Swapped arr[{}]={} and arr[{}]={}".format(i, arr[i], j, arr[j]))
            swap(arr, i, j)
            print(arr)
            i += 1

    print("Last swap, swapped arr[{}]={} and arr[{}]={}".format(i, arr[i], high, arr[high]))
    swap(arr, i, high)
    print(arr)

    print("Partition index: {}".format(i))
    return i


def quick_sort(arr, low, high):
    print("_______________________")
    print(arr)
    print("Low: {}, high: {}".format(low, high))
    if low < high:
        print("***Start partitioning***")
        pi = partition(arr, low, high)
        print("***End partitioning***")

        print("After partitioning: {}".format(arr))

        print("Next steps: sort({},{}), sort({},{})".format(low, pi - 1, pi + 1, high))
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


quick_sort(arr_to_sort, 0, len(arr_to_sort) -1)
print(arr_to_sort)
