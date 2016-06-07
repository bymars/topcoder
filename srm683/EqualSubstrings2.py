class EqualSubstrings2:
    def get(self, s):
        n = len(s)
        sum = 0
        for num in range(1, n // 2 + 1):
            for i in range(n - num + 1):
                left = s[i:i+num]
                for j in range(i + num, n - num + 1):
                    right = s[j:j+num]
                    if left == right:
                        sum += 1
        return sum
