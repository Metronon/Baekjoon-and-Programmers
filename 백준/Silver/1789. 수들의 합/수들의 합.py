import sys
input = sys.stdin.readline

N = int(input())
result = 0
cnt = 1

while (N >= 0):
    N -= cnt
    result += 1
    cnt += 1
    if N < 0:
        result -= 1
        
print(result)