class RailroadSwitchOperator:
    def minEnergy(self, N, x, t):
        depth = 0
        div = N
        state = [0] * (N)
        for i in range(N):
            state[i] = [-1, 0]
        change = []
        switches = []

        while div // 2 > 0:
            depth += 1
            div = div // 2
        for i in range(len(x)):
            target = x[i]
            for d in range(depth)[::-1]:
                direction = target % 2
                sw = (target+1) // 2 + pow(2, d) - 1
                if state[sw][0] != direction and state[sw][0] != -1:
                    if sw in switches:
                        pos = switches.index(sw)
                        change[pos].append([state[sw][1]+1, t[i] + d])
                    else:
                        switches.append(sw)
                        change.append([])
                        change[-1].append([state[sw][1]+1, t[i] + d])
                state[sw] = [direction, t[i] + d]
                target = (target+1) // 2
        result = 0
        for t in range(t[-1] + depth):
            need = 0
            for item in change:
                if len(item) > 0 and item[0][1] == t:
                    need = 1
                    result += 1
                    break
            if need == 1:
                for i in range(len(change)):
                    if len(change[i]) > 0 and change[i][0][0] <= t:
                        change[i] = change[i][1:]

        return result
