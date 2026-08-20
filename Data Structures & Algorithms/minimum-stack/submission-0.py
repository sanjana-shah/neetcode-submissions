class MinStack:

    def __init__(self):
        self.stack = deque()
        self.minstack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minstack or val < self.minstack[-1]:
            self.minstack.append(val)

        else:
            self.minstack.append(self.minstack[-1])

        

    def pop(self) -> None:
        if not self.stack:
            return

        self.stack.pop()
        self.minstack.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

        return -1
        

    def getMin(self) -> int:
        if self.minstack:
            return self.minstack[-1]

        return -1
        
