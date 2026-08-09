class CountSquares:

    def __init__(self):
        self.points = defaultdict(lambda :defaultdict(int))

    def add(self, point: List[int]) -> None:
        self.points[point[0]][point[1]] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        res = 0

        for y2 in self.points[x1]:
            side  = y2 - y1
            if side == 0:
                continue

            x3, x4 = x1 + side, x1 - side

            res += (self.points[x1][y2] * self.points[x3][y1] *
                    self.points[x3][y2])

            res += (self.points[x1][y2] * self.points[x4][y1] *
                    self.points[x4][y2])

        return res

        
