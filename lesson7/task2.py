import random

size = 11
array = [round(random.uniform(0, 50), 2) for i in range(size)]


def merge_sort(array):
    result = [0] * len(array)

    if len(array) <= 1:
        return array

    left, right = array[:len(array) // 2], array[len(array) // 2:]

    left = merge_sort(left)
    right = merge_sort(right)

    n = m = k = 0
    while n < len(left) and m < len(right):
        if left[n] <= right[m]:
            result[k] = left[n]
            n += 1
        else:
            result[k] = right[m]
            m += 1
        k += 1

    while n < len(left):
        result[k] = left[n]
        n += 1
        k += 1

    while m < len(right):
        result[k] = right[m]
        m += 1
        k += 1

    return result


print(array)
print(merge_sort(array))
