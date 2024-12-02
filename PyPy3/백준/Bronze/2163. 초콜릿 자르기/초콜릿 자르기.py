import sys
input = sys.stdin.readline

N, M = map(int, input().split())

if N == 1 and M == 1:
    print(0)
elif N == 1 or M == 1:
    if N == 1:
        print(M - 1)
    else:
        print(N - 1)
else:
    print((N - 1) + N * (M - 1))