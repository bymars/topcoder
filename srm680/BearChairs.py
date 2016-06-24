# Used 35min
class BearChairs:
    def findPositions(self, atLeast, d):
        l = len(atLeast)
        seat = [0] * l
        sort = [0] * l
        seat[0] = sort[0] = atLeast[0]
        for i in range(1, l):
            find = 0
            for p in range(i):
                if sort[p] > atLeast[i]:
                    find = 1
                    break
            if find == 1 and (sort[p] >= atLeast[i] + d and (p == 0 or sort[p - 1] + d <= atLeast[i])):
                seat[i] = atLeast[i]
                for t in range(p,i)[::-1]:
                    sort[t+1] = sort[t]
                sort[p] = seat[i]
            else:
                seat[i] = max(sort[i-1] + d, atLeast[i])
                sort[i] = seat[i]
        return seat
