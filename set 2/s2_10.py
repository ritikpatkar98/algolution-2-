def maxLengthSubarray(nums, target):
    
    sum_map = {}
    max_len = 0
    current_sum = 0
    start_index = -1

    for i in range(len(nums)):
        
        current_sum += nums[i]

        
        if current_sum == target:
            max_len = i + 1
            start_index = 0

        
        if (current_sum - target) in sum_map:
            if max_len < i - sum_map[current_sum - target]:
                max_len = i - sum_map[current_sum - target]
                start_index = sum_map[current_sum - target] + 1

        
        if current_sum not in sum_map:
            sum_map[current_sum] = i

    
    if max_len > 0:
        return nums[start_index: start_index + max_len]
    else:
        return []

nums = [5, 6, -5, 5, 3, 5, 3, -2, 0]
target = 9
print(maxLengthSubarray(nums, target))  # Output: [-5, 5, 3, 5]