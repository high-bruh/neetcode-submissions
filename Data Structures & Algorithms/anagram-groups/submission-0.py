class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)

        for s in strs:
            a = [0] * 26
            for char in s:
                a[ord(char) - ord('a')] += 1
            hm[tuple(a)].append(s)

        return list(hm.values())