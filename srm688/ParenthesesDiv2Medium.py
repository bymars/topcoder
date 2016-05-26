class ParenthesesDiv2Medium:
    def correct(self, s):
        print(s)
        flip = []
        stack = 0
        temp = 0
        for i in range(len(s)):
            if s[i] == '(':
                temp = stack + 1
            if s[i] == ')':
                temp = stack - 1
            if temp < 0:
                s = s[:i]+'('+s[i+1:]
                temp = stack + 1
                flip.append(i)
            stack = temp
        stack = 0
        for i in range(len(s))[::-1]:
            if s[i] == ')':
                temp = stack + 1
            if s[i] == '(':
                temp = stack - 1
            if temp < 0:
                s = s[:i]+')'+s[i+1:]
                temp = stack + 1
                flip.append(i)
            stack = temp
        return flip
