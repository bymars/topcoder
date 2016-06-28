from operator import itemgetter, attrgetter
class BearFair2:
    def isFair(self, n, b, upTo, quantity):
        N = n // 3
        q = len(upTo)

        dp = [0] * (q + 1)
        for i in range(q + 1):
            dp[i] = [0] * (N + 1)
            for j in range(N + 1):
                dp[i][j] = [0] * (N + 1)
                for k in range(N + 1):
                    dp[i][j][k] = [-1] * (N + 1)

        hint = [0] * (q + 1)
        to_sort = [0] * (q + 1)
        for i in range(q):
            to_sort[i] = [upTo[i], quantity[i]]
        to_sort[q] = [b, n]
        to_sort = sorted(to_sort)
        x = y = z = t = 0
        for i in range(1, b + 1):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            else:
                z += 1
            while t <= q and i == to_sort[t][0]:
                if t == 0:
                    count = to_sort[t][1]
                else:
                    count = to_sort[t][1] - to_sort[t - 1][1]
                hint[t] = [count, x, y, z]
                x = y = z = 0
                t += 1

        self.hint = hint
        self.dp = dp
        if self.run(q, N, N, N) == 0:
            return "unfair"
        else:
            return "fair"

    def run(self, step, a, b, c):
        if a == 0 and b == 0 and c == 0:
            return 1
        if a < 0 or b < 0 or c < 0:
            return 0
        if self.dp[step][a][b][c] != -1:
            return self.dp[step][a][b][c]

        [quantity, x, y, z] = self.hint[step]
        x = min(x, quantity)
        for i in range(x + 1):
            y = min(y, quantity - i)
            for j in range(y + 1):
                k = quantity - i - j
                if k <= z:
                    if self.run(step - 1, a - i, b - j, c - k) == 1:
                        return 1
        self.dp[step][a][b][c] = 0
        return 0
