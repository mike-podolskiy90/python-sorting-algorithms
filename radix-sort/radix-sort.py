arr_to_sort = [7, 1, 2, 1, 5]
print(arr_to_sort)


def counting_sort(arr, div):
    count = [0] * 10

    for a in arr:
        count[(a // div) % 10] += 1

    total = 0
    for i in range(len(count)):
        count[i], total = total, count[i] + total

    result = [0] * len(arr)
    for i in range(len(arr)):
        index = (arr[i] // div) % 10
        result[count[index]] = arr[i]
        count[index] += 1

    return result


def radix_sort(arr):
    div = 1
    _max = max(arr)
    while _max // div > 0:
        arr = counting_sort(arr, div)
        div *= 10
    return arr


arr_to_sort = radix_sort(arr_to_sort)

print(arr_to_sort)
