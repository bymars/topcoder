class NonDeterministicSubstring:
    def ways(self, A, B):
        C = []
        base = int(A, 2)
        length = len(A)
        bits = len(B)
        b_0 = B.replace('1', '?').replace('0', '1').replace('?', '0')
        b_1 = B.replace('0', '?').replace('1', '0').replace('?', '1')
        b_and = int(b_0, 2)
        b_or = int(b_1, 2)
        mask = (1 << bits) - 1
        for i in range(0, length - bits +1):
            t = base >> i & mask
            if t & b_and == 0 and t | b_or == mask:
                find  = 0
                for v in C:
                    if v == t:
                        find = 1
                        break
                if find == 0:
                    C.append(t)
        return len(C)
