import sys
input = sys.stdin.readline

number = map(int, input().split())
num_list = list(number)
result = 0

for i in num_list:
    result += i ** 2
    
print(result % 10)