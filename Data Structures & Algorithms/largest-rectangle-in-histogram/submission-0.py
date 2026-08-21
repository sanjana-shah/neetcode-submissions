class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [-1] * (n)

        stack = deque()
        for i in range(n):
            if not stack:
                stack.append(i)

            else:
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()

                if stack:
                    left[i] = stack[-1]
                stack.append(i)

        right = [n] * n
        stack = deque()
        for i in range(n-1, -1, -1):
            if not stack:
                stack.append(i)

            else:
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()

                if stack:
                    right[i] = stack[-1]

                stack.append(i)

        maxArea = 0
        for i in range(n):
            left[i] += 1
            right[i] -= 1
            area = (right[i] - left[i] + 1) * heights[i]
            maxArea = max(maxArea, area)

        return maxArea
                