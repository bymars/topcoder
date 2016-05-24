modulo = 1000000007
class WolfHockeyTeamEasy:
    factorial_array = []
    def count(self, N, K):
        # 1. total number: 2N
        # 2. max in 2nd row: range (max(N-1,K), 2N-2)
        # 3. unknown numbers: max
        # 4. (max in 2nd row) swapped to 1st row:
        #    unknown number: 1st: max - N, 2nd: N (max > N - 1)
        # 5. (max in 2nd row) not swapped to 1st row:
        #    unknown number: 1st: max - N + 1, 2nd: N - 1 (max >= N - 1)
        # 6. max!/(1st!*(2nd+1)!)*(2nd-1st+1)
        self.N = N
        self.factorial_array = [0] * 2 * N
        max_2nd = max(K, N - 1)
        sum = 0
        for i in range(max_2nd, 2 * N - 1):
            sum += self.young_tableaus_count(i - N + 1, N - 1)
            if i > N - 1:
                sum += self.young_tableaus_count(i - N, N)
        return sum * 2 * self.factorial(N) % modulo
    def young_tableaus_count(self, first, second):
        a = self.factorial(first + second)
        b = self.factorial(first)
        c = self.factorial(second+1)
        d = second - first + 1
        return (a * d) // (b * c) % modulo
    def factorial(self, N):
        if self.factorial_array[N] == 0:
            self.factorial_array[0] = 1
            for i in range(1, self.N * 2):
                self.factorial_array[i] = i * self.factorial_array[i - 1]
        return self.factorial_array[N]


