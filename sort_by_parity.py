def sort_by_parity(nums):
    l = 0
    r = len(nums)-1
    while l < r:
        if nums[l] % 2 == 1 and nums[r] %2 == 0:
            nums[l], nums[r] = nums[r], nums[l]
        
        if nums[l] % 2 == 0:
            l += 1
        if nums[r] %2 != 0:
            r -= 1        
    return nums

nums = [3, 1, 2, 4]
print(sort_by_parity(nums))

nums = [0]
print(sort_by_parity(nums))