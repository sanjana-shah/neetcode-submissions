class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        ans = 0

        for token in tokens:
            if token in '+-*/':
                o1 = stack.pop()
                o2 = stack.pop()
                if token == '+':
                    stack.append(o1 + o2)

                elif token == '-':
                    stack.append(o2 - o1)

                elif token == '*':
                    stack.append(o2 * o1)

                elif token == '/':
                    temp = o2/o1
                    if temp < 0:
                        stack.append(int(temp))
                    else:
                        stack.append(o2//o1)

            else:
                stack.append(int(token))


        return stack[-1]