class ParenthesesDiv2Easy:
    def getDepth(self, s):
        stack = 0
        depth = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack+=1
            if s[i] == ')':
                stack-=1
            if depth < stack:
                depth = stack
        return depth

