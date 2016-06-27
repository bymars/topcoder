from operator import itemgetter, attrgetter
class BearFair2:
    def isFair(self, n, b, upTo, quantity):
        self.N = n // 3
        q = len(upTo)
        self.hint = [0] * (q + 1)
        sum = 0
        for i in range(q):
            self.hint[i] = [upTo[i], quantity[i]]
            sum += quantity[i]
        self.hint[q] = [b, n - sum]
        # sort hint by upTo
        self.hint = sorted(self.hint, key=itemgetter(1,0))
        self.dp = [0] * (q + 1)
        for i in range(q + 1):
            self.dp[i] = [0] * (self.N + 1)
            for j in range(self.N + 1):
                self.dp[i][j] = [0] * (self.N + 1)
                for k in range(self.N + 1):
                    self.dp[i][j][k] = [-1] * (self.N + 1)
        if self.run(q, self.N, self.N, self.N) == 0:
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

        start = (self.hint[step - 1][0] if step > 0 else 0) + 1
        end = self.hint[step][0]
        number = end - start + 1
        quantity = self.hint[step][1]
        x = y = z = number // 3
        if number % 3 == 1:
            if start % 3 == 0:
                x += 1
            elif start % 3 == 1:
                y += 1
            else:
                z += 1
        elif quantity % 3 == 2:
            if start % 3 == 0:
                x += 1
                y += 1
            elif start % 3 == 1:
                y += 1
                z += 1
            else:
                z += 1
                x += 1

        for i in range(x):
            if i > quantity:
                break
            for j in range(y):
                if i + j > quantity:
                    break
                k = quantity - i - j
                if k > z:
                    break
                if self.run(step - 1, a - i, b - j, c - k) == 1:
                    return 1
        self.dp[step][a][b][c] = 0
