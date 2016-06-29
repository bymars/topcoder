class ThePhantomMenace:
    def find(self, doors, droids):
        level = [0] * len(doors)
        for i in range(len(doors)):
            minimum = min(droids, key=lambda x: abs(x - doors[i]))
            level[i] = abs(minimum - doors[i])
        return max(level)
