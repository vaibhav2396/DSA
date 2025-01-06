def insert_interval(intervals, new_interval):
    result = []
    merging = False
    for i, interval in enumerate(intervals):
        if not merging:
            if new_interval[0] > interval[1]:
                result.append(interval)
            else:
                if new_interval[1] < interval[0]:
                    result.append(new_interval)
                    result += intervals[i:]
                    return result
                else:
                    result.append([min(interval[0], new_interval[0]), max(interval[1], new_interval[1])])
                    merging = True
        else:
            if interval[0] > result[-1][1]:
                result.append(interval)
            else:
                result[-1] = [min(interval[0], result[-1][0]), max(interval[1], result[-1][1])]
    if not merging:
        result.append(new_interval)
    return result
     
intervals = [[1, 3], [6, 9]]
new_interval = [-4, -1]
print(insert_interval(intervals, new_interval))

intervals = [[1, 3], [6, 9]]
new_interval = [2, 5]
print(insert_interval(intervals, new_interval))

intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
new_interval = [4, 8]
print(insert_interval(intervals, new_interval))

intervals = [[1, 3], [7, 9]]
new_interval = [4, 5]
print(insert_interval(intervals, new_interval))