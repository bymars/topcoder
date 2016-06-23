# Used 75min
class FriendlyRobot:
    def findMaximumReturns(self, instructions, changesAllowed):
        n = len(instructions)
        dp = [0] * (n + 1)
        for i in range(len(dp)):
            dp[i] = [0] * (changesAllowed + 1)
        for i in range(n-1)[::-1]:
            if i % 2 != 0:
                continue
            # calculate dp[i][0....changesAllowed]
            for c in range(changesAllowed + 1):
                # calculate dp[i][c]
                dp[i][c] = 0
                x = 0
                y = 0
                for p in range(i, n):
                    if instructions[p] == 'U':
                        x -= 1
                    if instructions[p] == 'D':
                        x += 1
                    if instructions[p] == 'R':
                        y += 1
                    if instructions[p] == 'L':
                        y -= 1
                    if (abs(x) + abs(y)) % 2 == 0:
                        need = (abs(x) + abs(y)) // 2
                        if need <= c:
                            t = dp[p+1][c-need]
                            dp[i][c] = 1 + t if dp[i][c] < 1 + t else dp[i][c]
        return dp[0][changesAllowed]
