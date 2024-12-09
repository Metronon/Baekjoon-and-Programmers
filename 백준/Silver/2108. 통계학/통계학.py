import sys
from collections import Counter
input = sys.stdin.readline

def find_most(arr):
    counter = Counter(arr)
    max_count = max(counter.values())
    mosts = [k for k, v in counter.items() if v == max_count]
    if len(mosts) > 1:
        mosts.sort()
        return mosts[1]
    else:
        return mosts[0]

N = int(input())
num_list = []
sum = 0

for _ in range(N):
    num = int(input())
    num_list.append(num)
    sum += num
    
num_list.sort()
    
print(round(sum / len(num_list)))
print(num_list[int((N / 2) - 0.5)])
print(find_most(num_list))
print(max(num_list) - min(num_list))