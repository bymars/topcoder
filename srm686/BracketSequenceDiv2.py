modulo = 1000000007
def add(a, b):
    a += b
    if a >= modulo:
        a -= modulo
    return a

class BracketSequenceDiv2:
    def count(self, s):
        n = len(s)
        dp = [0] * (n + 2)
        for i in range(len(dp)):
            dp[i] = [0] * 2

        dp[0][0] = 1
        for i in range(len(s)):
            if s[i] == '(':
                for j in range(1, len(dp))[::-1]:
                    dp[j][0] = add(dp[j-1][0], dp[j-1][1])
            if s[i] == ')':
                for j in range(0, len(dp) - 1):
                    dp[j][1] = add(dp[j+1][0], dp[j+1][1])
        return dp[0][1]

