class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        for key in freq.keys():
            if not heap or len(heap) < k:
                heapq.heappush(heap, [freq[key], key])

            elif len(heap) == k and heap[0][0] < freq[key]:
                heapq.heappop(heap)
                heapq.heappush(heap, [freq[key], key])

             
        ans = []
        while heap:
            ans.append(heapq.heappop(heap)[1])

        return ans