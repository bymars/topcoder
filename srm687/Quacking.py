class Quacking:
    def quack(self, s):
        sound = "quack"
        count = 0
        while len(s) != 0:
            j = 0
            temp = ""
            for i in range(len(s)):
                if s[i] == sound[j]:
                    j = (j + 1) % 5
                else:
                    temp += s[i]
            if len(temp) != 0:
                if temp[0] != 'q' or j != 0:
                    return -1
            count += 1
            s = temp
        return count
