def sort_performers(performer_names, performance_times):
    combine = list(zip(performer_names, performance_times))
    combine = sorted(combine, key= lambda pair: pair[1], reverse=True)
    result = []
    for item in combine:
        result.append(item[0])
    return result

performer_names1 = ["Mary", "John", "Emma"]
performance_times1 = [180, 165, 170]

performer_names2 = ["Alice", "Bob", "Bob"]
performance_times2 = [155, 185, 150]

print(sort_performers(performer_names1, performance_times1)) 
print(sort_performers(performer_names2, performance_times2))