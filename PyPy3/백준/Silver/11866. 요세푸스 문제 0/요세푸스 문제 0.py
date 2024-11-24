from collections import deque

N, M = map(int, input().split())
num_list = deque(range(1, N+1))
result = []

while num_list:
    num_list.rotate(-(M-1))
    result.append(num_list.popleft())

print("<" + ", ".join(map(str, result)) + ">")