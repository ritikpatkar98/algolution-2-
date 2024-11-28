def count_frequency(arr):
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    return frequency


array = [1, 2, 2, 3, 3, 3, 4, 5, 5, 6]
frequency = count_frequency(array)
print("Frequency of each number:", frequency)
