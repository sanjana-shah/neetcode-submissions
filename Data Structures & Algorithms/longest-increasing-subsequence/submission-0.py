class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums)-2, -1, -1):
            max_sub = 1
            for j in range(i+1, len(nums)):
                if nums[i]<nums[j]:
                    max_sub = max(max_sub, 1 + dp[j])

            dp[i] = max_sub
        return max(dp)