#Used 15min
class ExplodingRobots:
    def canExplode(self, x1, y1, x2, y2, instructions):
        xd = abs(x1 - x2)
        yd = abs(y1 - y2)
        x = 0
        y = 0
        for item in instructions:
            if item == 'U' or item == 'D':
                y += 1
            if item == 'L' or item == 'R':
                x += 1
        if xd <= x and yd <= y:
            return "Explosion"
        else:
            return "Safe"
