import sys
input = sys.stdin.readline
print = sys.stdout.write

A = 0
B = 0

def fibonacci(N):
    A = [0] * (N + 1)
    B = [0] * (N + 1)
    if N >= 0:
        A[0] = 1
    if N >= 1:
        B[1] = 1
    for i in range(2, N + 1):
        A[i] = A[i-1] + A[i-2]
        B[i] = B[i-1] + B[i-2]
        
    return A[N], B[N]
    
R = int(input())
for _ in range(R):
    num = int(input())
    result_A, result_B = fibonacci(num)
    print(f"{result_A} {result_B}\n")