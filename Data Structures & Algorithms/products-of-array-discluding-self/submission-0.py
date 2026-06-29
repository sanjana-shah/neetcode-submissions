class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]

        for j in range(len(nums)-2, -1, -1):
            postfix[j] = postfix[j+1] * nums[j+1]


        productExceptSelf = [1] * len(nums)

        for i in range(len(nums)):
            productExceptSelf[i] = prefix[i] * postfix[i]

        return productExceptSelf