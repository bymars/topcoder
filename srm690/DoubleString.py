class DoubleString:
    def check(self, S):
        l = len(S)
        if l % 2 == 0:
            if S[:(l // 2)] == S[-(l // 2):]:
                return "square"
            else:
                return "not square"
        else:
            return "not square"
