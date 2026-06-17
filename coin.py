def coin_change(coins, amount):
    dp = [float('inf')]*(amount +1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin,amount +1):
            dp[x] = min(dp[x], 1 + dp[x - coin])

    return dp[amount] if dp[amount] != float('inf') else -1

coins = [1,5,6,9]
amount = 10

print(coin_change(coins, amount))