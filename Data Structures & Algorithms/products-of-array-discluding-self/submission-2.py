class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_prod = [1] * (n + 1)
        right_prod = [1] * (n + 1)

        # 2 3 4
        # 1 2 6 24
        # 0 1 2 3 
        for i in range(len(nums)):
            left_prod[i+1] = left_prod[i] * nums[i]
        # 24 12 4 1
        for i in range(len(nums)-1, -1, -1):
            right_prod[i] = right_prod[i+1] * nums[i]

        ans = [1] * (n)

        for i in range(n):
            ans[i] = left_prod[i] * right_prod[i + 1]

        return ans