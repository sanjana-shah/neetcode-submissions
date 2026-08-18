class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]
        
        if len(cost) == 2:
            return min(cost[0], cost[1])

        tracker = dict()
        tracker[0] = cost[0]
        tracker[1] = cost[1]

        for i in range(2, len(cost)):
            tracker[i] = cost[i] + min(tracker[i-1], tracker[i-2])


        return min(tracker[len(cost)-1], tracker[len(cost)-2])