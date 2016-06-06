class RGBTree:
    def exist(self, G):
        self.n = len(G)
        self.dp = []
        self.G = G
        for i in range(1 << self.n):
            self.dp.append([])
            for r in range((self.n - 1) // 3 + 1):
                self.dp[i].append([])
                for g in range((self.n - 1) // 3 + 1):
                    self.dp[i][r].append([])
                    for b in range((self.n - 1) // 3 + 1):
                        self.dp[i][r][g].append([])
                        self.dp[i][r][g][b] = 0
        if self.run(1,0,0,0) == 1:
            return "Exist"
        else:
            return "Does not exist"
    def run(self, A, nr, ng, nb):
        n = self.n
        G = self.G
        if nr > (n-1)//3 or ng > (n-1)//3 or nb > (n-1)//3:
            return -1
        if nr + ng + nb == n - 1:
            return 1
        if self.dp[A][nr][ng][nb] == -1:
            return -1
        for i in range(self.n):
            if A | (1 << i) != A:
                continue
            for j in range(self.n):
                if A | (1 << j) == A:
                    continue
                if G[i][j] == 'R':
                    if self.run(A | (1 << j), nr + 1, ng, nb) == 1:
                        return 1
                if G[i][j] == 'G':
                    if self.run(A | (1 << j), nr, ng + 1, nb) == 1:
                        return 1
                if G[i][j] == 'B':
                    if self.run(A | (1 << j), nr, ng, nb + 1) == 1:
                        return 1
        self.dp[A][nr][ng][nb] = -1
        return -1
