class XorLists:
    def countLists(self, s, m):
        l = len(s)
        # get n
        n = 0
        while n * n < l:
            n += 1

        self.n = n
        self.dp = [0] * 31
        for i in range(len(self.dp)):
            self.dp[i] = [-1] * (1 << self.n)

        self.s = s
        self.m = m

        # validte s
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if s[i*n+k] ^ s[j*n+k] != s[i*n+j]:
                        return 0

        # count every bit from high to low
        # if previous bit is lower than bit in m, then everything is OK
        # if previous bit is equal to bit in m, then current bit cannot greater than bit in m
        # prev_bit_cmp_mask represents this. 1 means lower, 0 means equal.
        # 1,000,000,000 has 30 bits most
        # dp[bit][mask] means for current bit and previous bits cmp mask compute the count
        # dp[bit][mask] = sum of dp[bit - 1][new_mask]. new_mask is determined by current bit of n numbers
        return self.run(30, 0)

    def run(self, bit, mask):
        if bit < 0:
            return 1
        if self.dp[bit][mask] != -1:
            return self.dp[bit][mask]
        a = [0] * self.n
        bm = (self.m >> bit) & 1
        for i in range(self.n):
            a[i] = (self.s[i] >> bit) & 1
        count = 0
        for t in range(2):
            nmask = mask
            flag = 1
            for i in range(self.n):
                if a[i] > bm and (mask >> i) & 1 == 0:
                    flag = 0
                if a[i] < bm:
                    nmask |= 1 << i
            if flag == 1:
                count += self.run(bit - 1, nmask)
            for i in range(self.n):
                a[i] ^= 1
        self.dp[bit][mask] = count
        return count
