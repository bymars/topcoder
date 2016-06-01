class Sunnygraphs2:
    def count(self, a):
        l = len(a)
        visited = [False] * l
        time = [0] * l
        timestamp = 0
        graphs = []
        for i in range(l):
            if visited[i]:
                continue
            pool = [i]
            visited[i] = True
            time[i] = timestamp
            timestamp += 1
            # DFS(i)
            next = a[i]
            while not visited[next]:
                visited[next] = True
                time[next] = timestamp
                timestamp += 1
                pool.append(next)
                next = a[next]

            # at current timestamp, we visited 'next' second time
            # first time we vist 'next' at time[next]
            circle = timestamp - time[next]

            # Found all connected elements
            found = True
            while found:
                found = False
                for i in range(l):
                    if not visited[i] and a[i] in pool:
                        if not i in pool:
                            pool.append(i)
                        visited[i] = True
                        found = True
            n = len(pool)
            graphs.append([circle, n - circle])

        sum = 1
        for x, y in graphs:
            sum *= (2**x - 1) * 2**y
            if len(graphs) == 1:
                sum += 1
        return sum
