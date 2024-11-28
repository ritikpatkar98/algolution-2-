def findEquilibriumIndex(arr):
    n = len(arr)
    total_sum = sum(arr)  # Total sum of the array
    left_sum = 0  # Initialize left sum as 0

    for i in range(n):
        # Calculate right sum as total_sum - left_sum - current element
        right_sum = total_sum - left_sum - arr[i]

        # Check if left sum equals right sum
        if left_sum == right_sum:
            return i + 1  # Return 1-based index

        # Update left sum for the next iteration
        left_sum += arr[i]

    return -1  # Return -1 if no equilibrium index exists



arr1 = [-7, 1, 5, 2, -4, 3, 0]
arr2 = [1, 2, 3]
arr3 = [1, 3, 5, 2, 2]

print(findEquilibriumIndex(arr1))  # Output: 4
print(findEquilibriumIndex(arr2))  # Output: -1
print(findEquilibriumIndex(arr3))  # Output: 2