class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        min_val = float('inf')
        while low <= high:
            mid = low + (high-low)//2
            min_val = min(nums[mid], min_val)
            if nums[mid] < nums[high]:
                high = mid - 1
            
            else:
                low = mid + 1

        return min_val