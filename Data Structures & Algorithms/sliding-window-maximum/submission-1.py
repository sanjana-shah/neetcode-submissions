class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        left = 0
        ans = []

        for right in range(len(nums)):
            heapq.heappush(heap, (-nums[right], right))
            if right - left + 1 == k:
                while left > heap[0][1]:
                    heapq.heappop(heap)

                ans.append(-heap[0][0])

                if left == heap[0][1]:
                    heapq.heappop(heap)
                
                left += 1

        return ans