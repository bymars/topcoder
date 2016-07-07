class TreeAndPathLength2:
    def possible(self, n, s):
        visited = [0] * (n+1)
        for i in range(n+1):
            visited[i] = [0] * (s+1)
        self.s = s
        self.n = n
        self.visited = visited

        for i in range(1, n):
            ns = i * (i - 1) // 2
            if ns <= s:
                self.dfs(1+i, ns)

        if visited[n][s] == 1:
            return "Possible"
        else:
            return "Impossible"

    def dfs(self, nodes, s):
        S = self.s
        n = self.n
        visited = self.visited

        if visited[nodes][s] != 1:
            visited[nodes][s] = 1
            for i in range(1, n - nodes + 1):
                ns = i * (i - 1) // 2 + i + s
                if ns <= S:
                    self.dfs(nodes + i, ns)
