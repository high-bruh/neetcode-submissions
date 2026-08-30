class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        curr = ""
        k = 0

        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == "[":
                stk.append([curr, k])
                curr = ""
                k = 0
            elif c == "]":
                tmp = curr
                curr, count = stk.pop() 
                curr += tmp * count
            else:
                curr += c

        return curr
            
            