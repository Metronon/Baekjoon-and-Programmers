import sys
import math
input = sys.stdin.readline

def round_up(number):
    return math.ceil(number)

N = int(input())
if N == 0:
    print(0)
else:
    level_list = []

    for i in range(N):
        level_list.append(int(input()))
        
    level_list.sort()

    sum = 0
    repeat = 0
    if N * 0.15 -(int(N * 0.15)) == 0.5:
        limit = round_up(N * 0.15)
    else:
        limit = round(N * 0.15)

    for i in level_list[limit : N - limit]:
        sum += i
        repeat += 1
        
    if (sum / repeat) - int(sum / repeat) == 0.5:
        result = round_up(sum / repeat)
    else:
        result = round(sum / repeat)
    print(result)