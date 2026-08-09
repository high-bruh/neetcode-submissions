class MinStack:

    def __init__(self):
        self.minn = float('inf')
        self.stk = []

    def push(self, val: int) -> None:
        if val <= self.minn:
            self.stk.append(self.minn)
            self.minn = val
        self.stk.append(val)

    def pop(self) -> None:
        if self.stk.pop() == self.minn:
            self.minn = self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minn
