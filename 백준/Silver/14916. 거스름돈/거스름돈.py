N = int(input())
result = 0

if N == 1 or N == 3:
    print(-1)
elif N == 2 or N == 5:
    print(1)
elif N == 4:
    print(2)
else:
    while (N > 10):
        result += 1
        N -= 5
    match N:
        case 6:
            result += 3
        case 7:
            result += 2
        case 8:
            result += 4
        case 9:
            result += 3
        case 10:
            result += 2
    print(result)