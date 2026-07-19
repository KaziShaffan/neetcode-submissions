class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        val = self.stack[-1]
        return val

    def getMin(self) -> int:
        conv = set(self.stack)
        small = min(conv)
        return small
