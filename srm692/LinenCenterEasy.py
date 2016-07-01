# Stupid modulo. different from usual one.
modulo = 1000000009
class LinenCenterEasy:
    def countStrings(self, S, N, K):
        L = len(S)
        forbid = [False] * (L)
        for i in range(1, L):
            s = S[0:i] + S[:]
            if s[0:L] == S:
                forbid[i] = True
        transform = [0] * L
        for i in range(L):
            transform[i] = [0] * 26
        for i in range(L):
            target = S[0:i]
            pos = S.find(target)
            while pos != -1:
                if pos+i < L:
                    transform[pos+i][ord(S[i])-ord('a')] = i+1
                pos = S.find(target, pos+1)

        dp = [0] * (L+1)
        for i in range(L+1):
            dp[i] = [0] * (N+1)
            for j in range(N+1):
                dp[i][j] = [-1] * (K+1)

        self.L = L
        self.S = S
        self.forbid = forbid
        self.transform = transform
        self.dp = dp
        self.run(0, K, N)

        return dp[0][N][K]


    def run(self, p, k, n):
        dp = self.dp
        L = self.L
        S = self.S
        forbid = self.forbid
        transform = self.transform

        res = dp[p][n][k]
        if res == -1:
            res = 0
            if p != L:
                if k == 0:
                    res += 1
                if n > 0:
                    for i in range(26):
                        res += self.run(transform[p][i], k, n-1)
                if k > 0 and not forbid[p]:
                    res += self.run(0, k-1, n)
            res %= modulo
            dp[p][n][k] = res
        return res


