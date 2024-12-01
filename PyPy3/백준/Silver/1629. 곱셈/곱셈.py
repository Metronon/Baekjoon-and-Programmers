import sys
input = sys.stdin.readline
A, B, C = map(int, input().split())

def remainder(num1, num2):
    if num2 == 1:
        return A % C
    else:
        temp = remainder(num1, num2//2)
        if num2 % 2 == 0:
            return (temp * temp) % C
        else:
            return (temp * temp * num1) % C
        
print(remainder(A, B))