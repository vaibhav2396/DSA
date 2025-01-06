def three_sum(nums):
    #Step 1: Sort the array
    #Step 2: fix the first position lets say i, put left in front of i and roght at the end of array
    #        target would be 0 - nums[i], perform 2 sum between left and right with the new target,
    #        find all the targets
    #        setup new i, make sure to skip the element if i is same as the previous value

    nums.sort()
    i = 0
    n = len(nums)
    result = []
    while i < n-2:
        l = i + 1
        r = n-1
        while l < r:
            triplet = [nums[i], nums[l], nums[r]]
            current_sum = sum(triplet)
            if current_sum == 0:
                result.append(triplet)
                while l<r and nums[l] == triplet[1]:
                    l += 1
                while l<r and nums[r] == triplet[2]:
                    r -= 1
            elif current_sum > 0:
                r -= 1
            else:
                l += 1

        while i < n-1 and nums[i] == nums[i+1]:
            i += 1
        i += 1
    return result 

nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))

nums = [0, 1, 1]
print(three_sum(nums))

nums = [0, 0, 0]
print(three_sum(nums))
