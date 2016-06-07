class Autohamil:
    def check(self, z0, z1):
        n = len(z0)
        self.z0 = z0
        self.z1 = z1
        self.v_visited = [0] * n
        self.e_visited = [0] * n
        for i in range(len(self.e_visited)):
            self.e_visited[i] = [0] * 2
        return "Exists" if self.bfs(0) == 1 else "Does not exist"
    def bfs(self, v):
        self.v_visited[v] += 1
        if 0 not in self.v_visited:
            return 1
        if self.e_visited[v][0] == 0:
            self.e_visited[v][0] = 1
            if self.bfs(self.z0[v]) == 1:
                return 1
        if self.e_visited[v][1] == 0:
            self.e_visited[v][1] = 1
            if self.bfs(self.z1[v]) == 1:
                return 1
        self.v_visited[v] -= 1
