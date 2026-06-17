def coin_no_of_ways(coins, amount):
    dp = [0] * (amount+1)
    dp[0] = 1

    for coin in coins:
        for x in range(coin, amount+1):
            dp[x] += dp[x - coin]
    return dp[amount]

coins = [2,3,5,10]
amount = 15
print(coin_no_of_ways(coins, amount))