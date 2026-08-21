class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        n = len(temperatures)
        ans = [0] * n
        # [30,38,30,36,35,40,28]
        for i in range(n-1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
                    
            if stack:
                ans[i] = stack[-1] - i

            stack.append(i)

        return ans