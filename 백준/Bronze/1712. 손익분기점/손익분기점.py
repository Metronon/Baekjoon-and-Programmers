list = list(map(int, input().split(" ")))

n = list[2] - list[1]
if n <= 0:
    print(-1)
else:
    print((list[0] // n) + 1)