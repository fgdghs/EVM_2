class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] хранит минимальное число монет для суммы i
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                # Монета больше чем сумма то нет
                if i - coin >= 0:
                    # либо оставить текущий минимум для суммы i,
                    # либо взять текущую монету и добавить её к оптимальному решению для остатка (i - coin)
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        # Если значение осталось прежним, значит собрать сумму невозможно
        return dp[amount] if dp[amount] != amount + 1 else -1