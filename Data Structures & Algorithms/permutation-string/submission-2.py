class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count = defaultdict(int)

        for c in s1:
            count[c] += 1

        for r in range(0, len(s1)):
            count[s2[r]] -= 1

        l = 0
        for r in range(len(s1), len(s2)):
            if all([val <= 0 for val in count.values()]):
                return True
            count[s2[r]] -= 1
            count[s2[l]] += 1
            l += 1

        if all([val <= 0 for val in count.values()]):
                return True

        return False

