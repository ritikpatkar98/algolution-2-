# Write a program that takes 7 integers as input from the user 
#  then Reverse the order of numbers in the array, then print the numbers.
# question_four


def reverse_array():
    numbers = []
    print("Enter 7 integers:")

    for _ in range(7):
        number = int(input())
        numbers.append(number)

    reversed_numbers = numbers[::-1]
    print("Reversed array:", reversed_numbers)

reverse_array()
