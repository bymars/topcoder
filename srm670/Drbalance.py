class Drbalance:
    def lesscng(self, s, k):
        neg_count = 0
        balance = [0] * len(s)
        bal = 0
        for i in range(len(s)):
            if s[i] == '-':
                bal -= 1
            elif s[i] == '+':
                bal += 1
            if bal < 0:
                neg_count += 1
            balance[i] = bal
        res = 0
        while neg_count > k:
            for i in range(len(balance)):
                balance[i] += 2
                if balance[i] < 2 and balance[i] >= 0:
                    neg_count -= 1
            res += 1

        return res

