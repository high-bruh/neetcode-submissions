class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        l, r = 0, n - 1
        count = 0

        while l <= r:
            if people[r] == limit or people[l] + people[r] > limit:
                count += 1
                r -= 1

            elif people[l] + people[r] <= limit:
                count += 1
                l += 1
                r -= 1

        return count