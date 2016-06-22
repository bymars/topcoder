# Used 40min
from queue import Queue
class TopBiologist:
    def findShortestNewSequence(self, sequence):
        q = Queue()
        while True:
            prev = ["", sequence]
            if not q.empty():
                prev = q.get()
            target = prev[0] + "A"
            pos = prev[1].find(target)
            if pos == -1:
                return target
            else:
                q.put([target, sequence[pos:]])
            target = prev[0] + "C"
            pos = prev[1].find(target)
            if pos == -1:
                return target
            else:
                q.put([target, sequence[pos:]])
            target = prev[0] + "G"
            pos = prev[1].find(target)
            if pos == -1:
                return target
            else:
                q.put([target, sequence[pos:]])
            target = prev[0] + "T"
            pos = prev[1].find(target)
            if pos == -1:
                return target
            else:
                q.put([target, sequence[pos:]])
