from collections import deque

N = int(input())
num_list = deque(range(1, N+1))

while (len(num_list) != 1):
    num_list.popleft()
    a = num_list.popleft()
    num_list.append(a)

print(*num_list)