class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = set()
        for i in range(n):
            target = -nums[i]

            seen = {}
            for j in range(i+1, n):
                if target - nums[j] in seen:
                    temp = [nums[i], target - nums[j], nums[j]]
                    temp.sort()

                    ans.add(tuple(temp))

                else:
                    seen[nums[j]] = j
        
        ans = list(ans)

        result = []
        for item in ans:
            result.append(list(item))

        return result