N = int(input())

temp_list = [0, 1, 2]
if N < 3:
    print(temp_list[N-1])
else:
    gift = [0 for _ in range(N + 1)]
    gift[1] = 0
    gift[2] = 1
    gift[3] = 2
    
    for i in range(4, N + 1):
        gift[i] = ((gift[i-1] + gift[i-2]) * (i - 1)) % 1000000000
        
    print(gift[N])