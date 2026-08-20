class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        brute force n^2
        optimization 1: using a seen set: will still take O(n) space complexity
        """

        seen = set()

        for item in nums:
            if item in seen:
                return True

            else:
                seen.add(item)


        return False