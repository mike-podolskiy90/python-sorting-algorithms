arr_to_sort = [7, 1, 2, 1, 5]
print(arr_to_sort)


def counting_sort(arr):
    k = max(arr)

    count = [0] * (k + 1)
    for x in arr:
        count[x] += 1

    total = 0
    for i in range(k + 1):
        count[i], total = total, count[i] + total

    output = [0] * len(arr)
    for x in arr:
        output[count[x]] = x
        count[x] += 1

    return output


arr_to_sort = counting_sort(arr_to_sort)

print(arr_to_sort)
