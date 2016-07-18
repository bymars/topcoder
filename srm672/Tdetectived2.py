maxInt = 50
class Tdetectived2:
    def reveal(self, s):
        n = len(s)
        x = [0] * n
        for i in range(n):
            x[i] = [0] * n
            for j in range(n):
                x[i][j] = int(s[i][j])

        visited = [0] * (2 << n)
        result = [maxInt] * n
        y = [0] * n
        self.visited = visited
        self.result = result
        self.n = n
        self.x = x
        self.dfs(0, 0, y, 0)
        r = 0
        print(result)
        for i in range(n):
            r += i * result[i]
        return r

    def dfs(self, prev, cur, y, depth):
        c = prev | 1 << cur
        visited = self.visited
        result = self.result
        n = self.n
        x = self.x
        if visited[c] == 1 or depth == n:
            return

        visited[c] = 1
        if result[cur] > depth:
            result[cur] = depth

        new_y = [0] * n
        for i in range(n):
            if c & 1 << i == 0:
                new_y[i] = max(x[cur][i], y[i])

        maximum = max(new_y)
        for i in range(n):
            if new_y[i] == maximum:
                self.dfs(c, i, new_y, depth + 1)
