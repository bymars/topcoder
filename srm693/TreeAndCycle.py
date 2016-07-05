class TreeAndCycle:
    def minimize(self, costV, pre, costE):
        n = len(costV)
        child = [0] * n
        for i in range(n):
            child[i] = []
        for i in range(n-1):
            child[pre[i]].append(i+1)
        dp = [0] * n
        for i in range(n):
            dp[i] = [0,0]
        for i in range(n)[::-1]:
            dp[i][0] = costV[i] * 2
            max_1 = 0
            max_2 = 0
            for j in child[i]:
                dp[i][0] += dp[j][0]
                change = costV[i] + costV[j] + costE[j-1] - dp[j][1]
                [max_1, min_1] = [change, max_1] if change > max_1 else [max_1, change]
                max_2 = max(max_2, min_1)
            if max_1 > 0:
                dp[i][0] -= max_1
            if max_2 > 0:
                dp[i][0] -= max_2
                dp[i][1] = max_2
        return dp[0][0] + sum(costE)
