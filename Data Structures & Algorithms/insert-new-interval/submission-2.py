class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        stack = deque()

        i = 0
        used_interval = False

        if not intervals:
            stack.append(newInterval)
        while i < len(intervals) or not used_interval:
            curr = []

            if i == len(intervals):
                curr = newInterval
                used_interval = True
            # first we decide which element is going to go next
            elif intervals[i][0] <= newInterval[0] or used_interval:
                curr = intervals[i]
                i+=1
            
            else:
                curr = newInterval
                used_interval = True

            if not stack:
                stack.append(curr)

            else:
                top = stack[-1]
                if top[1] >= curr[0]: # overlapping
                    top = stack.pop()
                    stack.append([top[0], max(top[1], curr[1])])
                else:
                    stack.append(curr)

        return list(stack)

            
