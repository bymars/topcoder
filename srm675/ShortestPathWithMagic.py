import heapq
maxInt = 500
class ShortestPathWithMagic:
    def getTime(self, dist, k):
        n = len(dist)
        graph = [0] * n
        for i in range(n):
            graph[i] = [0] * n
            for j in range(n):
                graph[i][j] = int(dist[i][j]) * 2

        ret = self.dijkstra(graph, 0, 1, k)
        if ret == maxInt:
            return 0
        else:
            return ret / 2

    def dijkstra(self, graph, start, end, k):
        n = len(graph)
        visited = [0] * n
        for i in range(n):
            visited[i] = [0] * (k+1)
        dist = [0] * n
        for i in range(n):
            dist[i] = [maxInt] * (k+1)

        visited[start][k] = 1
        for i in range(n):
            if graph[start][i] != 0:
                dist[i][k] = graph[start][i]
                if k > 0:
                    dist[i][k-1] = graph[start][i] // 2

        for t1 in range(n - 1):
            for t2 in range(k+1):
                v = [start, k] # to avoid unreachable case
                minimum = maxInt
                for i in range(n):
                    for j in range(k+1):
                        if visited[i][j] == 0 and dist[i][j] < minimum:
                            minimum = dist[i][j]
                            v = [i, j]
                visited[v[0]][v[1]] = 1
                for i in range(n):
                    if graph[v[0]][i] != 0:
                        if visited[i][v[1]] == 0:
                            new_dist = dist[v[0]][v[1]] + graph[v[0]][i]
                            if new_dist < dist[i][v[1]]:
                                dist[i][v[1]] = new_dist
                        if v[1] > 0 and visited[i][v[1] - 1] == 0:
                            new_dist = dist[v[0]][v[1]] + graph[v[0]][i] // 2
                            if new_dist < dist[i][v[1]-1]:
                                dist[i][v[1]-1] = new_dist
        return min(dist[end])
