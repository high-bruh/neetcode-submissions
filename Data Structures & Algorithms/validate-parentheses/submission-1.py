class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        hm = { ")" : "(", "]" : "[", "}" : "{" }

        for char in s:
            if char in hm:
                if stk and stk[-1] == hm[char]:
                    stk.pop()
                else:
                    return False

            else:
                stk.append(char)

        return not stk