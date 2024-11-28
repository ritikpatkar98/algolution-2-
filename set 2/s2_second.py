def merge_and_count(arr, temp_arr, left, mid, right):
    """
    Function to merge two halves of the array and count the inversions during merging.
    """
    i = left       # Starting index for the left subarray
    j = mid + 1    # Starting index for the right subarray
    k = left       # Starting index to place sorted elements in temp array
    inv_count = 0  # Count of inversions

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1

    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return inv_count

def merge_sort_and_count(arr, temp_arr, left, right):
    
    inv_count = 0
    if left < right:
        mid = (left + right) // 2

        inv_count += merge_sort_and_count(arr, temp_arr, left, mid)

        inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)

        inv_count += merge_and_count(arr, temp_arr, left, mid, right)

    return inv_count

def count_inversions(arr):
    """
    Main function to count inversions in the array.
    """
    n = len(arr)
    temp_arr = [0] * n
    return merge_sort_and_count(arr, temp_arr, 0, n - 1)

arr = [7, 2, 6, 3]
print("Number of inversions:", count_inversions(arr))  # Output: 4
