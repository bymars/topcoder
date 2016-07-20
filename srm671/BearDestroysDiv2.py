class BearDestroysDiv2:
    def sumUp(self, W, H, MOD):
        dp = [0] * (W*H)
        for i in range(len(dp)):
            dp[i] = [-1] * (1 << W)

        self.W = W
        self.H = H
        self.dp = dp
        self.MOD = MOD
        return self.run(0, 0, 0)

    def run(self, x, y, mask):
        H = self.H
        W = self.W
        dp = self.dp
        MOD = self.MOD
        if y == H:
            return 0

        if x == W:
            return self.run(0, y+1, mask)

        pos = y*W+x
        if dp[pos][mask] != -1:
            return dp[pos][mask]

        down = right = -1
        if mask & 1 << x == 0:
            if x != W-1 and mask & 1 << (x+1) == 0:
                right = self.run(x+1, y, mask | 1 << (x+1)) % MOD
            if y != H-1:
                down = self.run(x+1, y, mask | 1 << x) % MOD

        if down == -1 and right == -1:
            res = 2 * self.run(x+1, y, mask & ~(1<<x)) % MOD
        else:
            res = (1 << (W*H-pos)) % MOD
            # E option
            if right != -1:
                res += right
            else:
                res += down
            # S option
            if down != -1:
                res += down
            else:
                res += right
        dp[pos][mask] = res % MOD
        return dp[pos][mask]
