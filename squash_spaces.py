def squash_spaces(s):
    result = []
    n = len(s)
    i = 0

    while i < n and s[i] == ' ':
        i += 1

    space = True
    while i < n:
        if s[i]  != ' ':
            result.append(s[i])
            space = True
        elif space:
            result.append(s[i])
            space = False
        i += 1
    if result and result[-1] == ' ':
        result.pop()
    return ''.join(result)

    

s = "   Up,     up,   and  away! "
print(squash_spaces(s))

s = "With great power comes great responsibility."
print(squash_spaces(s))