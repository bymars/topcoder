maxInt = 1000 * 1000 * 50
class RevengeOfTheSith:
    def move(self, steps, T, D):
        N = len(steps)
        dp = [0] * N
        for i in range(N):
            dp[i] = [0] * (T + 1)
            for j in range(T + 1):
                dp[i][j] = [-1] * 2001
        # dp[i][j][1000] means prev move is 1000 - 1000 = 0.
        # dp[i][j][0] means prev move is 0 - 1000 = -1000
        # dp[i][j][2000] means prev move is 2000 - 1000 = 1000

        self.dp = dp
        self.D = D
        self.steps = steps
        self.N = N

        return self.run(0, T, 0)

    def run(self, n, t, prev_move):
        dp = self.dp
        D = self.D
        steps = self.steps
        N = self.N

        if n == N - 1:
            H = steps[n] - prev_move
            if H <= D:
                damadge = 0
            else:
                damadge = (H - D) * (H - D)
            return damadge

        if dp[n][t][prev_move+1000] != -1:
            return dp[n][t][prev_move+1000]
        minimum = maxInt
        possible_move_low = 0
        possible_move_high = 0
        if t > 0:
            possible_move_low = -(steps[n] - prev_move - 1)
            for i in range(1, t+1):
                if i+n < N:
                    possible_move_high += (steps[n+i] - 1)
        for i in range(possible_move_low, possible_move_high + 1):
            H = steps[n] -prev_move + i
            if H <= D:
                damage = 0
            else:
                damage = (H - D) * (H - D)
            if i == 0:
                result = damage + self.run(n+1, t, i)
            else:
                result = damage + self.run(n+1, t-1, i)
            minimum = result if result < minimum else minimum
        dp[n][t][prev_move] = minimum
        return minimum


