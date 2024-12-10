import sys
import math
import itertools
input = sys.stdin.readline

def comb(n, k):
    if k > n:
        return 0
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

M = int(input())
N = input()   
K = int(input())

rock_list = list(map(int, N.split()))
rock_sum = sum(rock_list)
    
prob_sum = 0.0
for rocks in rock_list:
    if rocks >= K:
        prob_sum += comb(rocks, K) / comb(rock_sum, K)
    
print(prob_sum)