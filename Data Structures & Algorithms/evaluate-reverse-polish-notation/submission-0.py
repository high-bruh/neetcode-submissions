class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for token in tokens:
            if token == '+':
                stk.append(stk.pop() + stk.pop())
            elif token == '-':
                a, b = stk.pop(), stk.pop()
                stk.append(b - a)
            elif token == '*':
                stk.append(stk.pop() * stk.pop())
            elif token == '/':
                a, b = stk.pop(), stk.pop()
                stk.append(int(b / a))
            else:
                stk.append(int(token))

        return stk[0]
