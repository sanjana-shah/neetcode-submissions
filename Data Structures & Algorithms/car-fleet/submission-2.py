class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        track = []
        n = len(speed)
        for i in range(n):
            track.append([position[i], speed[i]])

        track.sort(key= lambda x: -x[0])
        stack = deque()
        for i in range(n):
            if not stack:
                stack.append((target - track[i][0]) / track[i][1])


            elif stack[-1] < ((target - track[i][0])/track[i][1]):
                stack.append((target - track[i][0]) / track[i][1] )
                
        return len(stack)