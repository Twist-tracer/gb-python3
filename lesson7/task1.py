import random

size = 10
array = [random.randint(-100, 100) for i in range(size)]
sorted_array = array.copy()


n = 1
while n < len(sorted_array):
    for i in range(len(sorted_array) - n):
        if sorted_array[i] < sorted_array[i+1]:
            sorted_array[i], sorted_array[i + 1] = sorted_array[i + 1], sorted_array[i]
    n += 1

print(array)
print(sorted_array)
