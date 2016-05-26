class ParenthesesDiv2Hard:
    def minSwaps(self, s, L, R):
        extra_l = 0
        extra_r = 0
        sum_l = 0
        sum_r = 0
        j = 0
        for i in range(len(s)):
            if j < len(L) and i == L[j]:
                i = R[j] + 1
                j += 1
            else:
                if s[i] == '(':
                    extra_l += 1
                if s[i] == ')':
                    extra_r += 1
        for i in range(len(L)):
            temp = s[L[i] : R[i]+1]
            [l, r] = self.correct(temp)
            sum_l += l
            sum_r += r
#        print("extra_l:" + str(extra_l) + " extra_r:" + str(extra_r) + " sum_l:" + str(sum_l) + " sum_r:" + str(sum_r))
        if sum_r - sum_l > 0:
            if extra_r >= sum_r - sum_l:
                return sum_r
            else:
                return -1
        else:
            if extra_l >= sum_l - sum_r:
                return sum_l
            else:
                return -1

    def correct(self, s):
        stack = 0
        temp = 0
        l = 0
        r = 0
        for i in range(len(s)):
            if s[i] == '(':
                temp = stack + 1
            if s[i] == ')':
                temp = stack - 1
            if temp < 0:
                s = s[:i]+'('+s[i+1:]
                temp = stack + 1
                l += 1
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
                r += 1
            stack = temp
        return [l, r]
