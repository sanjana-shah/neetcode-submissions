class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        current_profit = 0
        left = 0
        for right in range(len(prices)):
            if prices[left] > prices[right]:
                max_profit = max(max_profit, current_profit)
                left = right

            else:
                current_profit = prices[right] - prices[left]
                max_profit = max(max_profit, current_profit)

        return max_profit