# Used 40min
from collections import deque
class TopBiologist:
    def findShortestNewSequence(self, sequence):
        DNA = "ACGT"
        q = deque()
        while True:
            prev = ["", sequence]
            if len(q) > 0:
                prev = q.popleft()
            for item in DNA:
                target = prev[0] + item
                pos = prev[1].find(target)
                if pos == -1:
                    return target
                else:
                    q.append([target, sequence[pos:]])
