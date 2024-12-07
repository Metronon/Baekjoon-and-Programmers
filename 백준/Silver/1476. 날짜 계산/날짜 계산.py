E, S, M = map(int, input().split())
result = 1

while (not (E == 1 and S == 1 and M == 1)):
    if E == 0:
        E += 15
    if S == 0:
        S += 28
    if M == 0:
        M += 19
    E -= 1
    S -= 1
    M -= 1
    result += 1

print(result)