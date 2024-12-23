def selfNum(num):
    result = 0
    cache = list(str(num))
    for i in range(len(cache)):
        result += int(cache[i])
    result += num
    return result

comp = set()
for i in range(10000):
    comp.add(selfNum(i))
for j in range(1, 10001):
    if j not in comp:
        print(j)