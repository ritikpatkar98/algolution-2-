# question two
def find_max():
    numbers = []
    print("Enter 5 integers:")

    for _ in range(5):
        number = int(input())
        numbers.append(number)

    max_number = max(numbers)
    print(f"The maximum number is: {max_number}")


find_max()  #find maximum number

