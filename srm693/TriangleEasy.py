#Used 1 hour
class TriangleEasy:
    def find(self, n, x, y):
        graph = [0] * n
        for i in range(n):
            graph[i] = [0] * n
        for i in range(len(x)):
            graph[x[i]][y[i]] = 1
            graph[y[i]][x[i]] = 1

        best = 3
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    need = 0
                    if graph[i][j] == 0:
                        need += 1
                    if graph[i][k] == 0:
                        need += 1
                    if graph[j][k] == 0:
                        need += 1
                    best = min(best, need)
        return best




