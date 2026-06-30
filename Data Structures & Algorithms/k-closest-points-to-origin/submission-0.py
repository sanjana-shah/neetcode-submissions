class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        def calculateDistance(x, y):
            return (x**2 + y**2)**0.5

        for point in points:
            if not heap or len(heap) < k:
                heapq.heappush(heap, [-calculateDistance(point[0], point[1]), [point[0], point[1]]])
                
            elif len(heap) == k and heap[0][0] < -calculateDistance(point[0], point[1]):
                heapq.heappop(heap)
                heapq.heappush(heap, [-calculateDistance(point[0], point[1]), [point[0], point[1]]])

        ans = []
        while heap:
            ans.append(heapq.heappop(heap)[1])

        return ans