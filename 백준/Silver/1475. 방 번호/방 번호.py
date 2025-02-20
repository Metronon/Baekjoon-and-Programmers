import math
numbers = input()
num_list = [0] * 10

for n in numbers:
    num_list[int(n)] += 1
    
conf_count = num_list[6] + num_list[9]
num_list[6] = math.ceil(conf_count / 2)
num_list[9] = math.ceil(conf_count / 2)
        
result = max(num_list)
print(result)