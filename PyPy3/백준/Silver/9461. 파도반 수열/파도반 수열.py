import sys
input = sys.stdin.readline
cache = [0] * 101

def triangle(num):
    if (num <= 3):
        return 1
    elif (num <= 5):
        return 2
    
    if cache[num] != 0:
        return cache[num]
    
    cache[num] = triangle(num - 1) + triangle(num - 5)
    return cache[num]
    

N = int(input())

for i in range(N):
    print(triangle(int(input())))