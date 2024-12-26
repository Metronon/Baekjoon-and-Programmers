import sys
input = sys.stdin.readline

X, Y, W, S = map(int, input().split())

min_xy = min(X, Y)
max_xy = max(X, Y)
diff = max_xy - min_xy

straight = (X + Y) * W

diagonal_straight = min_xy * S + diff * W

diagonal_only = 0
if (X + Y) % 2 == 0:
    diagonal_only = max(X, Y) * S
else:
    diagonal_only = (max_xy - 1) * S + W

result = min(straight, diagonal_straight, diagonal_only)
print(result)