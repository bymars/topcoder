import heapq
class Istr:
    def count(self, s, k):
        c = [0] * 26
        for ch in s:
           i = ord(ch) - ord('a')
           c[i] -= 1
        heapq.heapify(c)
        for i in range(k):
            heapq.heapreplace(c,c[0] + 1)
        sum = 0
        for i in c:
            sum += i * i
        return sum
