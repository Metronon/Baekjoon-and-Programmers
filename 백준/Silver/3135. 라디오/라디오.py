import sys
input = sys.stdin.readline

cnt, goal = map(int, input().split())
N = int(input())
ratio_list = []

for _ in range(N):
    ratio_list.append(int(input()))
    
wanted_ratio = 0
cache = 1000

for i in ratio_list:
    if cache > abs(i - goal):
        cache = abs(i - goal)
        wanted_ratio = i
        
if abs(goal - cnt) <= abs(wanted_ratio - goal):
    print(abs(goal - cnt))
else:
    print(abs(wanted_ratio - goal) + 1)