import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
    
result = 0
cache = 0

for i in sorted(num_list):
    result += cache + i
    cache += i
    
print(result)