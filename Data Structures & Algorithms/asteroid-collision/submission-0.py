class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []

        for i in range(len(asteroids)):
            if i == 0 or asteroids[i] >= 0:
                stk.append(asteroids[i])
            else:
                alive = True
                while alive and stk and stk[-1] > 0:
                    if -asteroids[i] == stk[-1]:
                        stk.pop()
                        alive = False
                    elif -asteroids[i] > stk[-1]:
                        stk.pop()
                    else:
                        alive = False

                if alive:
                    stk.append(asteroids[i])

        return stk
            