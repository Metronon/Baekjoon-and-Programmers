import sys
input = sys.stdin.readline

N, change = map(int, input().split())
c_list = []

for _ in range(N):
    c_list.append(int(input()))

c_list.reverse()
result = 0

for i in c_list:
    if change >= i:
        result += change // i
        change = change % i
        
print(result)