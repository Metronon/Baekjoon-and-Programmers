N = int(input())
result = 0

while (N > 0):
    result += 1
    if N >= 7 and N % 3 != 0:
        N -= 3
    else:
        N -= 1
        
if result % 2 != 0:
    print("SK")
else:
    print("CY")