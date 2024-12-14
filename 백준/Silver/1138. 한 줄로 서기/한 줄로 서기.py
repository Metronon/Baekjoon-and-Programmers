N = int(input())

num_list = list(map(int, input().split()))
answer_list = [0]*N

for i in range(N):   
    cache = 0
    for j in range(N):
        if cache == num_list[i] and answer_list[j] == 0:
            answer_list[j] = i + 1
            break
        elif answer_list[j] == 0:
            cache += 1
                
print(' '.join(map(str, answer_list)))