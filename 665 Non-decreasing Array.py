'''
Problem 4: Non-decreasing Array
    Given an array nums with n integers,
    write a function non_decreasing() that checks if nums could become non-decreasing by modifying at most one element.

    We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).
'''

def non_decreasing(nums):
        count = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                count += 1
                if count > 1:
                    return False

                if i == 0 or nums[i-1] <= nums[i+1]:
                    nums[i] = nums[i+1]
                else:
                    nums[i+1] = nums[i]
        return True

nums = [3,4,2,3] 
print(non_decreasing(nums)) 

nums = [2,2,2,1] 
print(non_decreasing(nums))

nums = [1,4,2,3] 
print(non_decreasing(nums))

