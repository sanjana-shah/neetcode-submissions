class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
    
        def choices(i, selling):
            if (i, selling) in cache:
                return cache[((i, selling))]

            if i >= len(prices):
                return 0
            if i==(len(prices) - 1):
                if selling:
                    cache[(i, True)] = prices[i]
                    return cache[(i, True)]
                else:
                    cache[(i, False)] = 0
                    return cache[(i, False)]

            if selling:
                sell = choices(i+2, False) + prices[i]
                cooldown = choices(i+1, True) 
                cache[(i, True)] = max(sell, cooldown)
                return cache[(i, True)]

            else:
                buy = choices(i+1, True) - prices[i]
                cooldown = choices(i+1, False) 
                cache[(i, False)] = max(buy, cooldown)
                return cache[(i, False)]

        return choices(0, False)