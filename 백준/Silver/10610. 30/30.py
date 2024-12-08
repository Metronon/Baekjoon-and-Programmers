word = input()

if "0" not in word:
    print(-1)
    
else:
    sum = 0
    for i in range(len(word)):
        sum += int(word[i])
        
    if sum % 3 != 0:
        print(-1)
    else:
        word_list = list(word)
        word_list.sort(reverse=True)
        print("".join(word_list))