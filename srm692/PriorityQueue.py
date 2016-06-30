# Used 10min
class PriorityQueue:
    def findAnnoyance(self, S, a):
        cur = 0
        result = 0
        for i in range(len(S)):
            if S[i] == 'b':
                result += cur
            cur += a[i]
        return result
