def two_sum(nums, target):
    left = 0
    right = len(nums) -1

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        
        if current_sum > target:
            right -= 1
        else:
            left += 1
    
    return None


nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))

nums = [2, 7, 11, 15]
target = 18
print(two_sum(nums, target))