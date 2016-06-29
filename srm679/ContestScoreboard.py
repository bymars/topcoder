class ContestScoreboard:
    def findWinner(self, scores):
        # 1. parse scores
        teams = []
        for item in scores:
            submissions = item.split(" ")
            for i in range(1, len(submissions)):
                sub = submissions[i].split("/")
                submissions[i] = [int(sub[0]), int(sub[1])]
            teams.append(submissions)

        # 2. get all time point
        times = []
        for item in teams:
            for i in range(1, len(item)):
                if not item[i][1] in times:
                    times.append(item[i][1])
        times = sorted(times)
        times.append(times[-1] + 1)

        # 3. make a table n_times * n_teams
        n_times = len(times)
        n_teams = len(teams)

        table = [0] * n_teams
        for i in range(n_teams):
            table[i] = [0] * (n_times + 1)
        for i in range(n_teams):
            table[i][0] = teams[i][0]
            for j in range(1, len(teams[i])):
                t = times.index(teams[i][j][1])
                table[i][t + 2] = teams[i][j][0]
            for k in range(1, len(table[i]) - 1):
                table[i][k + 1] += table[i][k]
        table = sorted(table)

        # 4. mark all winners
        winners = [0] * n_teams
        for i in range(n_times):
            #index = self.findMax(table, i)
            m = max(table, key=lambda x: x[i+1])
            pos = table.index(m)
            winners[pos] = 1
        return winners
