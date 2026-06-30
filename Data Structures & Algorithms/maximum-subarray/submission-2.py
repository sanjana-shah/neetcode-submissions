class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        prefix_sum = [0] * (len(nums) + 1)
        min_sum = [0] * (len(nums) + 1)
        for i in range(1, len(nums)+1):
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1]
            min_sum[i] = min(min_sum[i-1], prefix_sum[i-1])

        max_diff = float('-inf')
        for i in range(1, len(nums)+1):
            max_diff = max(max_diff, prefix_sum[i] - min_sum[i])

        return int(max_diff)