from collections import deque
import sys
input = sys.stdin.readline

N = int(input().strip())
cmd = deque(map(int, input().strip().split()))
compare_list = deque([i + 1 for i in range(N)])
result = []

for i in range(N):
    result.append(compare_list.popleft())
    a = cmd.popleft()
    
    if a > 0:
        a -= 1
    cmd.rotate(-a)
    compare_list.rotate(-a)
    
print(*result)