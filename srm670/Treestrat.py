from collections import deque
class Treestrat:
    def roundcnt(self, tree, A, B):
        n = len(tree) + 1
        graph = [0] * n
        for i in range(n):
            graph[i] = [0] * n
        for i in range(len(tree)):
            graph[i+1][tree[i]] = 1
            graph[tree[i]][i+1] = 1

        visited = [0] * n
        distance = [0] * n

        q = deque()
        for blue in B:
            q.append(blue)

        while len(q) > 0:
            v = q.popleft()
            visited[v] = 1
            for i in range(len(graph[v])):
                if visited[i] != 1 and graph[v][i] == 1:
                    q.append(i)
                    distance[i] = distance[v] + 1

        minimum = n
        for red in A:
            q2 = deque()
            visited2 = [0] * n
            q2.append([red, 0])
            maximum = 0
            while len(q2) > 0:
                [v, dis] = q2.popleft()
                visited2[v] = 1
                if dis < distance[v]:
                    maximum = max(distance[v], maximum)
                    for i in range(len(graph[v])):
                        if visited2[i] != 1 and graph[v][i] == 1:
                            q2.append([i, dis + 1])
            minimum = min(minimum, maximum)
        return minimum
