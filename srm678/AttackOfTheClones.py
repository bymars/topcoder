class AttackOfTheClones:
    def count(self, firstWeek, lastWeek):
        minDays = [0] * len(firstWeek)
        for i in range(len(firstWeek)):
            j = lastWeek.index(firstWeek[i])
            if i == j:
                minDays[i] = 0
            elif i < j:
                minDays[i] = 1
            else:
                minDays[i] = i - j
        return max(minDays) + 1
