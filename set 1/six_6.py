def search_number(arr, target):
    try:
        index = arr.index(target)
        return index
    except ValueError:
        return -1

numbers = [10, 20, 30, 40, 50]
target = int(input("Enter the number to search: "))
index = search_number(numbers, target)
print(f"The index of the first occurrence of the number is: {index}")
