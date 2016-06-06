class DoubleWeights:
    def minimalCost(self, weight1, weight2):
        self.weight1 = weight1
        self.weight2 = weight2
        self.l = len(weight1[0])
        self.visited = [0] * self.l

        w1 = w2 = 0
        return self.dfs(0, w1, w2)

    def dfs(self, node, w1, w2):

        if node == 1:
            return w1 * w2

        if self.visited[node] == 1:
            return -1

        self.visited[node] = 1

        path = []
        for i in range(self.l):
            if self.weight1[node][i] != '.':
                ret = self.dfs(i, w1+int(self.weight1[node][i]), w2+int(self.weight2[node][i]))
                if ret != -1:
                    path.append(ret)
        if len(path) == 0:
            return -1

        result = path[0]
        for i in range(1,len(path)):
            result = path[i] if path[i] < result else result

        return result
