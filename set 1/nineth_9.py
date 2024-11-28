def count_duplicates(arr):
    unique_elements = set()
    duplicates = set()
    
    for num in arr:
        if num in unique_elements:
            duplicates.add(num)
        else:
            unique_elements.add(num)
    
    return len(duplicates)

array = [1, 2, 2, 3, 3, 3, 4, 5, 5, 6]

duplicate_count = count_duplicates(array)

print(f"Total number of duplicate numbers: {duplicate_count}")
