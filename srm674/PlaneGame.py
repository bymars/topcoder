class PlaneGame:
    def bestShot(self, x, y):
        # i j m n
        l = len(x)
        maximum = 0
        if l <= 2:
            return l
        for i in range(l):
            for j in range(l):
                if i == j:
                    continue
                dx1 = x[i] - x[j]
                dy1 = y[i] - y[j]
                for m in range(l):
                    if m == i or m == j:
                        continue
                    count = 0
                    for n in range(l):
                        dx2 = x[i] - x[n]
                        dy2 = y[i] - y[n]
                        if dx1 * dy2 == dx2 * dy1:
                            count += 1
                        else:
                            dx3 = x[m] - x[n]
                            dy3 = y[m] - y[n]
                            if dx1 * dx3 == -(dy3 * dy1):
                                count += 1
                    maximum = max(count, maximum)
        return maximum


