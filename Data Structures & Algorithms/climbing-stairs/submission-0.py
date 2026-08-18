class Solution:
    def climbStairs(self, n: int) -> int:
        tracker = dict()
        tracker[1] = 1
        tracker[2] = 2

        def dp(n: int) -> int:

            if n in tracker:
                return tracker[n]
            
            tracker[n] = dp(n-1) + dp(n-2)
            return tracker[n]

        return dp(n)