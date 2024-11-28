# question_5

def is_palindrome():
    numbers = []
    print("Enter 5 integers:")

    for _ in range(5):
        number = int(input())
        numbers.append(number)

    if numbers == numbers[::-1]:
        print("The array is in palindrome order.")
    else:
        print("The array is not in palindrome order.")


is_palindrome()
