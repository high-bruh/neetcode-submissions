class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen:
            if n == 1:
                return True

            seen.add(n)
            num = 0
            while n:
                digit = n % 10
                num += digit ** 2
                n //= 10
            n = num

        return False
