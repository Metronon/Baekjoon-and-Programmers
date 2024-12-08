from functools import lru_cache
import sys
input = sys.stdin.readline

@lru_cache(maxsize=78498)
def eratosthenes(num:int = 1000000):
    MAX = num + 1
    LIM = int(num ** 0.5) + 1
    RSET = lambda strt, end, gap: set(range(strt, end, gap))
    
    prime = RSET(5, MAX, 6) | RSET(7, MAX, 6)
    if num > 2: prime.add(3)
    if num > 1: prime.add(2)
    for i in range(5, LIM, 6):
        if i in prime:
            prime -= RSET(i * i, MAX, i * 6) | RSET(i * (i + 2), MAX, i * 6)
        j = i + 2
        if j in prime:
            prime -= RSET(j * j, MAX, j * 6) | RSET(j * (j + 4), MAX, j * 6)

    return prime

prime_list = eratosthenes(1000000)
while (True):
    number = int(input())
    if number == 0:
        break
    else:
        for i in prime_list:
            cache_list = []
            if number - i in prime_list:
                cache_list.append(i)
                cache_list.append(number - i)
                cache_list.sort()
                print(number, "=", cache_list[0], "+", cache_list[1])
                break
            else:
                continue
        if len(cache_list) == 0:
            print("Goldbach's conjecture is wrong.")