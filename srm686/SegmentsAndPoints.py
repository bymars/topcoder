from operator import itemgetter, attrgetter
class SegmentsAndPoints:
    def isPossible(self, p, l, r):
        p = sorted(p)
        v = []
        for i in range(len(l)):
            v.append([l[i], r[i], 0])
        v = sorted(v, key=itemgetter(1,0))
        for point in p:
            found = 0
            for segments in v:
                if segments[2] == 0 and point >= segments[0] and point <= segments[1]:
                    segments[2] = 1
                    found = 1
                    break
            if found == 0:
                return "Impossible"
        return "Possible"
