class Cdgame:
    def rescount(self, a, b):
        n = len(a)
        sum_a = sum(a)
        sum_b = sum(b)
        exist = []
        for i in range(n):
            for j in range(n):
                new_a = sum_a - a[i] + b[j]
                new_b = sum_b - b[j] + a[i]
                new = new_a * new_b
                if new not in exist:
                    exist.append(new)
        return len(exist)

