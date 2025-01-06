def merge_intervals(intervals):
    sorted_intervals = sorted(intervals, key= lambda interval: interval[0])
    merged_intervals = []
    for interval in sorted_intervals:
        if merged_intervals:
            if merged_intervals[-1][1] >= interval[0]:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])
            else:
                merged_intervals.append(interval)
        else:
            merged_intervals.append(interval)

    
    return merged_intervals

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals))

intervals = [[1, 4], [4, 5]]
print(merge_intervals(intervals))

intervals = [[1,4],[2,3]]
print(merge_intervals(intervals))
