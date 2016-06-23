# Used 12min
class CoinFlipsDiv2:
    def countCoins(self, state):
        n = len(state)
        interesting = 0
        for i in range(n):
            if i != 0 and state[i] != state[i - 1]:
                interesting += 1
                continue
            if i != n - 1 and state[i] != state[i + 1]:
                interesting += 1
                continue
        return interesting

