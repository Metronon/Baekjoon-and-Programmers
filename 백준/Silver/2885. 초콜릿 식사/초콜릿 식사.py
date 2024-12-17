import sys
input = sys.stdin.readline

N = int(input())

size = 1
while size < N:
    size *= 2

bin_N = bin(N)[2:]
piece_list = [int(digit) for digit in bin_N]
piece_list.reverse() 

cache = 0
for i in range(len(piece_list)):
    if piece_list[i] == 1:
        cache = i
        break

if N == size:
    print(size, 0)
else:
    print(size, len(piece_list) - cache)