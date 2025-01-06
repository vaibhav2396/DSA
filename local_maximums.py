def local_maximums(grid):
    rows = len(grid)
    cols = len(grid[0])

    result = []
    for i in range(1, rows-1):
        temp = []
        for j in range(1, cols-1):
            maxV = max(
                    grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1],
                    grid[i][j-1], grid[i][j], grid[i][j+1],
                    grid[i+1][j-1], grid[i+1][j], grid[i+1][j+1]
                )
            temp.append(maxV)
        result.append(temp)
    return result



grid = [
	[9, 9, 8, 1],
	[5, 6, 2, 6],
	[8, 2, 6, 4],
	[6, 2, 2, 2]
]
print(local_maximums(grid))

grid = [
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 2, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1]
]
print(local_maximums(grid))