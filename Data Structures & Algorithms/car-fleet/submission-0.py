class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        from math import ceil
        dp = [[position[i], speed[i]] for i in range(len(position))]
        dp.sort(reverse = True)
        stk = []
        
        for p, s in dp:
            stk.append((target - p)/s)
            if len(stk) > 1 and stk[-1] <= stk[-2]:
                stk.pop()

        return len(stk)