modulo = 1000000007
class ColorfulGardenHard:
    def count(self, garden, forbid):
        self.dp = [0] * len(forbid) # depth dimension
        for i in range(len(self.dp)):
            self.dp[i] = [0] * len(garden) # garden dimension
            for j in range(len(self.dp[i])):
                self.dp[i][j] = [-1] * (1 << len(garden))
        self.garden = sorted(garden)
        self.forbid = forbid
        return self.run(1, 0, (1 << len(garden)) - 1) % modulo

    def run(self, depth, before, left):
        ret = 0
        if depth == len(self.garden):
            return 1
        if self.dp[depth][before][left] != -1:
            return self.dp[depth][before][left]
        for flower in range(len(self.garden)):
            if left & (1 << flower) != 0:
                #print("flower: " + str(flower) + " depth: " + str(depth) + " before: " + str(before) + " left: " + bin(left))
                if depth == 0 or self.garden[flower] != self.garden[before]:
                    if self.garden[flower] != self.forbid[depth]:
                        if flower == 0 or self.garden[flower] != self.garden[flower-1] or left & (1 << flower - 1) == 0:
                            ret += self.run(depth+1, flower, left & ~(1 << flower))
        self.dp[depth][before][left] = ret
        return ret

