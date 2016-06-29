maxInt = 10001
class ForbiddenStreets:
    def find(self, N, A, B, time):
        # make the graph
        graph = [0] * N
        for i in range(N):
            graph[i] = [[-1, maxInt]] * N
            graph[i][i] = [-1, 0]

        for i in range(len(A)):
            graph[A[i]][B[i]] = [i, time[i]]
            graph[B[i]][A[i]] = [i, time[i]]

        # find all shortest path from every i and j
        path = [0] * N
        result = [0] * len(A)
        for i in range(N):
            path[i] = self.dijkstra(N,i,graph)
        for l in range(len(A)):
            for i in range(N-1):
                for j in range(i+1, N):
                    result[l] += 1
                    for item in path[i][j]:
                        if l not in item:
                            result[l] -= 1
                            break
        return result

    # return the pathes for every i and j
    def dijkstra(self, N, start, graph):
        dist = [maxInt] * N
        prev = [[]] * N
        s = [0] * N

        for i in range(N):
            if graph[start][i][0] != -1:
                dist[i] = graph[start][i][1]
                prev[i] = [[graph[start][i][0]]]
        dist[start] = 0
        s[start] = 1

        for t in range(N-1):
            # find min
            min_time = maxInt
            min_v = -1
            for i in range(N):
                if s[i] == 0 and dist[i] < min_time:
                    min_time = dist[i]
                    min_v = i
            s[min_v] = 1
            # update dist
            for i in range(N):
                if s[i] == 0 and graph[min_v][i][0] != -1:
                    new_dist = dist[min_v] + graph[min_v][i][1]
                    new_prev = []
                    for j in range(len(prev[min_v])):
                        path = prev[min_v][j] + [graph[min_v][i][0]]
                        new_prev.append(path)
                    if new_dist < dist[i]:
                        dist[i] = new_dist
                        prev[i] = new_prev
                    elif new_dist == dist[i]:
                        prev[i] += new_prev
        return prev
