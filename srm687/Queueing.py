class Queueing:
    def probFirst(self, len1, len2, p1, p2):
        '''
        dp[i][j] means 1st has i people, 2nd has j people, the possiblity 1st finished earlier than 2nd
        (1/p) * (1 - 1/p)^(k-1) means every second the possiblity of checkout is 1/p
        1s: 1/p
        2s: 1/(1-p) * 1/p
        3s: 1/((1-P)*(1-p)) * 1/p
        ....
        dp[1][0] = 0
        dp[0][1] = 1
        dp[0][0] = 0
        dp[1][1] = (1/p1)*(1/1-p2)dp[0][1] + (1/1-p1)*(1/p2)[1][0] + (1/1-p1)(1/1-p2)dp[1][1] + (1/p1)*(1/p2)dp[0][0]
        dp[i][j] = (1/p1)*(1/1-p2)dp[i-1][j] + (1/1-p1)*(1/p2)dp[i][j-1] + (1/p1)*(1/p2)dp[i-1][j-1] + (1/1-p1)(1/1-p2)dp[i][j]
        dp[1][j] = A / (1 - (1/1-p1)(1/1-p2)
        '''
        dp = [0] * (len1+1)
        for i in range(len(dp)):
            dp[i] = [0] * (len2+1)
        for i in range(1, len1+1):
            dp[i][0] = 0
        for i in range(1, len2+1):
            dp[0][i] = 1
        dp[0][0] = 0
        s1 = 1/p1
        s2 = 1/p2
        f1 = 1-1/p1
        f2 = 1-1/p2
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                dp[i][j] = (s1*f2*dp[i-1][j] + f1*s2*dp[i][j-1] + s1*s2*dp[i-1][j-1])/(1 - f1*f2)
        return dp[len1][len2]
