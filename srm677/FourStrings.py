class FourStrings:
    def shortestLength(self, a, b, c, d):
        s = [a,b,c,d]
        result = 40
        for i in range(4):
            for j in range(4):
                if i == j:
                    continue
                s_i_j = self.combine(s[i], s[j])
                for m in range(4):
                    if i == m or j == m:
                        continue
                    s_i_j_m = self.combine(s_i_j, s[m])
                    for n in range(4):
                        if i == n or j == n or m == n:
                            continue
                        s_i_j_m_n = self.combine(s_i_j_m, s[n])
                        result = min(result, len(s_i_j_m_n))
        return result

    def combine(self, x, y):
        if x.find(y) != -1:
            return x
        l = min(len(x), len(y))
        n = 0
        for i in range(l):
            if x[-(i+1):] == y[:i+1]:
                n = i + 1
        return x[:] + y[n:]


