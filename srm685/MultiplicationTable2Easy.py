import math
class MultiplicationTable2Easy:
    def isGoodSet(self, table, t):
        n = int(math.sqrt(len(table)))
        for i in t:
            for j in t:
                if not table[i*n+j] in t:
                    return "Not Good"
        return "Good"
