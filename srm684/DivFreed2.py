modulo = 1000000007
def add(a, b):
    a += b
    if a >= modulo:
        a -= modulo
    return a
class DivFreed2:
    def count(self, n, k):
        dp = [0] * n
        for i in range(len(dp)):
            dp[i] = [0] * (k + 1)
        divid = [0] * (k + 1)
        for i in range(k + 1):
            divid[i] = []

        for i in range(1, (k + 1) // 2 + 1):
            j = 2 * i
            while j <= k:
                divid[j].append(i)
                j += i
        for i in range(1, k + 1):
            dp[n - 1][i] = 1
        for p in range(n - 1)[::-1]:
            sum = 0
            for i in range(1, k + 1):
                sum = add(sum, dp[p + 1][i])
            for i in range(1, k + 1):
                dp[p][i] = sum
                for item in divid[i]:
                    dp[p][i] -= dp[p + 1][item]
                dp[p][i] = dp[p][i] % modulo
        result = 0
        for item in dp[0]:
            result = add(result, item)
        return result
