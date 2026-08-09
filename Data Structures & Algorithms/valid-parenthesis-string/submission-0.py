class Solution:
    def checkValidString(self, s: str) -> bool:
        l = []
        star = []

        for i in range(len(s)):
            if s[i] == '(':
                l.append(i)
            elif s[i] == '*':
                star.append(i)
            else:
                if not l and not star:
                    return False
                else:
                    if l:
                        l.pop()
                    else:
                        star.pop()

        if len(l) > len(star):
            return False
        
        while l:
            if l[-1] > star[-1]:
                return False
            l.pop()
            star.pop()

        return True
