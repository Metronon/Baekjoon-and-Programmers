n = int(input())

for i in range(1, n + 1):
    num = sum(map(int, str(i)))
    summary = num + i
    
    if(summary == n):
        print(i)
        break
    if(i == n):
        print(0)