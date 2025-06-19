from collections import defaultdict

def find_coins_greedy(coins, amount):
    # Жадібний алгоритм
    coins = sorted(coins, reverse=True)
    result = defaultdict(int)
    for coin in coins:
        while amount >= coin:
            amount -= coin
            result[coin] += 1
    if amount != 0:
        return {}  # Не можна видати суму точно
    return dict(result)

def find_min_coins(coins, amount):
    # Алгоритм динамічного програмування
    max_val = amount + 1
    dp = [max_val] * (amount + 1)
    dp[0] = 0
    prev = [-1] * (amount + 1)

    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                prev[x] = coin

    if dp[amount] == max_val:
        return {}  # Неможливо знайти розв'язок

    result = defaultdict(int)
    current = amount
    while current > 0:
        coin = prev[current]
        result[coin] += 1
        current -= coin

    return dict(result)


# --- Демонстрація ---
if __name__ == "__main__":
    coins = [50, 25, 10, 5, 2, 1]
    amount = 113

    greedy = find_coins_greedy(coins, amount)
    dp = find_min_coins(coins, amount)

    print("Greedy result:", greedy)
    print("DP result:", dp)
