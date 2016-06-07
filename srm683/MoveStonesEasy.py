class MoveStonesEasy:
    def get(self, a, b):
        steps = 0
        n = len(a)
        for i in range(n - 1):
            delta = a[i] - b[i]
            a[i+1] += delta
            if delta < 0:
                delta = -delta
            steps += delta
        if a[n-1] != b[n-1]:
            return -1
        return steps

