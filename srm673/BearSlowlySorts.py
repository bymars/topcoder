class BearSlowlySorts:
    def minMoves(self, w):
        maximum = max(w)
        minimum = min(w)
        sort = 1
        for i in range(len(w) - 1):
            if w[i] > w[i+1]:
                sort = 0
                break
        if sort == 1:
            return 0
        if maximum == w[0] and minimum == w[-1]:
            return 3
        if maximum == w[-1] or minimum == w[0]:
            return 1
        return 2
