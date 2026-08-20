class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        match = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if not stack:
                if char in ')}]':
                    return False

                stack.append(char)

            else:
                if char in ')}]':
                    if stack[-1] != match[char]:
                        return False

                    stack.pop()
                else:
                    stack.append(char)

        return len(stack) == 0