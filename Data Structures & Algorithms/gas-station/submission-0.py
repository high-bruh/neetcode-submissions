class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        def check(i):
            fuel = gas[i:] + gas[:i + 1]
            cst = cost[i:] + cost[:i + 1]
            tank = 0
            for j in range(len(fuel)):
                tank += fuel[j]
                tank -= cst[j]
                if tank < 0:
                    return False

            return True

        for i in range(len(gas)):
            if gas[i] < cost[i]:
                continue
            if check(i):
                return i

        return -1