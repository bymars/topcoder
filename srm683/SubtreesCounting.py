modulo = 1000000007
class SubtreesCounting:
    def sumOfSizes(self, n, a0, b, c, m):
        dp = [0] * n
        for i in range(len(dp)):
            dp[i] = [0] * 2
        a = [0] * n
        a[0] = a0
        for i in range(1, len(a) - 1):
            a[i] = (b * a[i-1] + c) % m
        tree = [0] * n
        for i in range(n):
            tree[i] = []
        for i in range(1, n):
            j = a[i - 1] % i
            tree[j].append(i)
        for i in range(n)[::-1]:
            size = 1
            count = 1
            for item in tree[i]:
                size = (size + dp[item][1] * size + count * dp[item][0]) % modulo
                count = count * (dp[item][1] + 1) % modulo
            dp[i][0] = size
            dp[i][1] = count
        sum = 0
        for item in dp:
            sum += item[0]
        return sum % modulo
