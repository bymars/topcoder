class SetPartialOrder:
    def compareSets(self, a, b):
        a_has_b = 1
        b_has_a = 1
        for i in range(len(a)):
            if a[i] not in b:
                b_has_a = 0
                break
        for i in range(len(b)):
            if b[i] not in a:
                a_has_b = 0
                break
        if a_has_b == 1 and b_has_a == 1:
            return "EQUAL"
        elif a_has_b == 0 and b_has_a == 0:
            return "INCOMPARABLE"
        elif a_has_b == 1:
            return "GREATER"
        else:
            return "LESS"


