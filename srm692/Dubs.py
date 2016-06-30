# Used 15min
class Dubs:
    def count(self, L, R):
        a = self.countAll(R)
        b = self.countAll(L - 1)
        return a - b
    def countAll(self, N):
        tail = N % 100
        extra = tail // 11 + 1
        pre = N // 100
        return pre * 10 + extra
