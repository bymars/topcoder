class FarmvilleDiv2:
    def minTime(self, time, cost, budget):
        l = len(time)
        plants = [0] * l
        for i in range(l):
            plants[i] = [cost[i], time[i]]
        plants = sorted(plants)
        for i in range(l):
            while plants[i][1] > 0 and budget - plants[i][0] >= 0:
                budget -= plants[i][0]
                plants[i][1] -= 1
        sum = 0
        for i in range(l):
            sum += plants[i][1]
        return sum
