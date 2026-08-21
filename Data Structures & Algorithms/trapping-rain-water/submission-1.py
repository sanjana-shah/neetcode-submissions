class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0] * n

        stack = deque()
        for i in range(n):
            while stack and stack[-1] < height[i]:
                stack.pop()

            if stack:
                left[i] = stack[-1]
            else:
                stack.append(height[i])

        stack = deque()
        right = [0] * n
        for i in range(n-1, -1, -1):
            while stack and stack[-1] < height[i]:
                stack.pop()

            if stack:
                right[i] = stack[-1]
            else:
                stack.append(height[i])
        ans = 0

        for i in range(n):
            water = min(left[i], right[i])
          
            if water - height[i] > 0:
                ans += water - height[i]


        return ans

            