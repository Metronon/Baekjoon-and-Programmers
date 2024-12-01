N = int(input())
result = 0
    
result += (N // 5)
if ((N % 5 == 1) or (N % 5 == 3)):
    result += 1
elif ((N % 5 == 2) or (N % 5 == 4)):
    result += 2

if (N == 4 or N == 7):
    print(-1)
else:
    print(result)