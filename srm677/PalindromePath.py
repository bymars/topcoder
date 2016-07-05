class PalindromePath:
    def shortestLength(self, n, a, b, c):
        graph = [0] * n
        dp = [0] * n
        for i in range(n):
            graph[i] = [''] * n
            dp[i] = [-1] * n
            dp[i][i] = 0
        for i in range(len(a)):
            graph[a[i]][b[i]] = c[i]
            graph[b[i]][a[i]] = c[i]
            dp[a[i]][b[i]] = 1
            dp[b[i]][a[i]] = 1
        L = 0
        remain = 2
        while remain > 0:
            change = 0
            for i in range(n):
                for j in range(i, n):
                    if dp[i][j] == L:
                        for u in range(n):
                            for v in range(n):
                                if graph[i][v] != '' and graph[i][v] == graph[j][u]:
                                    if dp[v][u] == -1 or dp[v][u] > 2 + L:
                                        dp[v][u] = 2 + L
                                        dp[u][v] = 2 + L
                                        change = 1
            if change == 0:
                remain -= 1
            else:
                remain = 2
            L += 1
        return dp[0][1]

