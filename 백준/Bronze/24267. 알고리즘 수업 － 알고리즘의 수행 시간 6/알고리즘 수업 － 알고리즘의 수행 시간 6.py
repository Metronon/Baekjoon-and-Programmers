N = int(input())

result = 0
repeat = N-2

for i in range(1, N-1):
    result += i * (repeat)
    repeat -= 1

print(result)
print(3)