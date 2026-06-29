class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        tracker = set()
        for num in nums:
            tracker.add(num)

        max_seq = 0
        for num in nums:
            if num - 1 not in nums:
                current_max = 1
                temp = num + 1
                while temp in tracker:
                    current_max += 1
                    temp += 1
                
                max_seq = max(max_seq, current_max)
        
        return max_seq