class SubstitutionCipher:
    def decode(self, a, b, y):
        table = [""] * 26
        for i in range(len(a)):
            p = ord(b[i]) - ord("A")
            table[p] = a[i]

        miss = ""
        for i in range(26):
            c = chr(i+ord("A"))
            if c not in table:
                if miss == "":
                    miss = c
                else:
                    miss = ""
                    break
        if miss != "":
            p = table.index("")
            table[p] = miss

        x = ""
        for i in range(len(y)):
            p = ord(y[i]) - ord("A")
            if table[p] != "":
                x += table[p]
            else:
                x = ""
                break
        return x

