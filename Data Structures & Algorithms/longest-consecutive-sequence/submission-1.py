class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        for item in nums:
            seen.add(item)

        longest = 0
        

        for item in nums:
            if item-1 not in seen:
                count = 0
                temp = item
                while temp in seen:
                    count += 1
                    temp += 1

                longest = max(longest, count)


        return longest