# Used 15min
class BearPair:
    def bigDistance(self, s):
        l = len(s)
        max = -1
        for i in range(l):
            if s[i] != s[l - 1]:
                max = l - i - 1  if max < l - i - 1 else max
                break
        for i in range(l)[::-1]:
            if s[i] != s[0]:
                max = i if max < i else max
        return max
