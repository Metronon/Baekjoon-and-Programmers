bin_num = bin(int(input()))
num_list = list(bin_num[2:len(bin_num)])
result = 0

for i in num_list:
    if i == "1":
        result += 1

print(result)