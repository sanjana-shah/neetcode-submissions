class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        if n == 0:
            return 0
        while n:
            n = (n) & (n-1)
            count += 1

        return count