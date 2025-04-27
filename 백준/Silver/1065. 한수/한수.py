n = int(input())
result = 0

for i in range(n):
    numbers = list(map(int, str(i + 1)))
    if (len(numbers) <= 2):
        result += 1
    else:
        a = int(numbers[2]) - int(numbers[1])
        b = int(numbers[1]) - int(numbers[0])
        if (a == b):
            result += 1
            
print(result)