class FreqStack:

    def __init__(self):
        self.cnt  = defaultdict(int)
        self.stk = [[]]

    def push(self, val: int) -> None:
        self.cnt[val] += 1
        if self.cnt[val] == len(self.stk):
            self.stk.append([])
        self.stk[self.cnt[val]].append(val)

    def pop(self) -> int:
        res = self.stk[-1].pop()
        self.cnt[res] -= 1
        if not self.stk[-1]:
            self.stk.pop()
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()