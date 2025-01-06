def most_honey(height):
    left = 0
    right = len(height) - 1
    honey = 0
    while left < right:
        honey = max(honey, (right-left) * min(height[left], height[right]))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return honey


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(most_honey(height))

height = [1, 1]
print(most_honey(height))