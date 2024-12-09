import sys
input = sys.stdin.readline

N = int(input())
num_list = set(map(int, input().split()))
    
M = int(input())
comp_list = list(map(int, input().split()))

for i in comp_list:
    if i in num_list:
        print(1)
    else:
        print(0)