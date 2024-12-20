def factorial(num):
    if num == 1 or num == 0:
        return 1
    return num * factorial(num-1)

import sys
input = sys.stdin.readline

N = int(input())
cnt = 0

result_num = factorial(N)
result_list = list(str(result_num))
result_list.reverse()

for i in result_list:
    if i == "0":
        cnt += 1
    else:
        break
    
print(cnt)