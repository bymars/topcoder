class BiconnectedDiv2:
    def minimize(self, w1, w2):
        sum = 0
        for i in range(len(w1)):
            if w1[i] <= 0 or i == 0 or i == len(w1) - 1:
                sum += w1[i]
        for i in range(len(w2)):
            sum += w2[i]
        return sum
