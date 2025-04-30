def fibonacci(number):
    dp = [0] * (number + 1)
    dp[0], dp[1] = 0, 1
    
    for i in range(2, number + 1):
        dp[i] = dp[i - 1] + dp [i - 2]
    return dp[number]

n = int(input())
print(fibonacci(n))