# question one 
def count_negative_numbers(array):
    negative_count = sum(1 for num in array if num < 0)
    return negative_count


array = [-1, 2, -3, 4, -5, 6]
print("Total number of negative numbers:", count_negative_numbers(array))
