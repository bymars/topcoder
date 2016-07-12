class BearPermutations2:
    def getSum(self, N, MOD):
        _sum = [0] * N
        perm = [1] * N
        c = [0] * N
        dp = [0] * (N+1)
        for i in range(1, N):
            _sum[i] = _sum[i-1] + i
            perm[i] = perm[i-1] * i % MOD
            c[i] = [1] * (i + 1)
            c[i][1] = i
            for j in range(2, len(c[i])):
                c[i][j] = c[i][j-1] * (i-j+1) // j
        for i in range(N+1):
            if i <= 2:
                dp[i] = 0
                continue
            res = 0
            for j in range(i):
                if j == 0 or j == i-1:
                    root_score = 0
                else:
                    root_score = perm[j-1]*perm[i-j-2]*(j*_sum[i-j-1]+(i-j-1)*_sum[j])
                child_score = dp[j]*perm[i-j-1]+dp[i-j-1]*perm[j]
                res += (c[i-1][j] * (root_score + child_score)) % MOD
            dp[i] = res % MOD
        return dp[N]


