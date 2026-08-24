class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = float('inf')
        while left <= right:
            mid = (left + right)//2
            hours = 0
            for item in piles:
                hours += int(math.ceil(item/mid))

            if hours > h:
                left = mid + 1

            else:
                ans = min(ans, mid)
                right = mid - 1

        return ans