def sqrtLast(a, b):
    if a % 10 != 0:
        firstNum = a % 10
        secondNum = (a ** 2) % 10
        thirdNum = (a ** 3) % 10
        fourthNum = (a ** 4) % 10
        if (b % 4 == 0):
            return fourthNum
        elif (b % 4 == 1):
            return firstNum
        elif (b % 4 == 2):
            return secondNum
        else:
            return thirdNum
    else:
        return 10
    
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(sqrtLast(a, b))