import math

list = list(map(int, input().split(" ")))

a, b = list[0], list[1]
max = math.gcd(a, b) 

print(math.gcd(a, b))
print(a * (b // max))