import math
class PalindromePrime:
    def count(self, L, R):
        c = 0
        if L == 1:
            L = 2
        for i in range(L, R+1):
            div = int(math.sqrt(i))
            prime = True
            for j in range(2, div+1):
                if i % j == 0:
                    prime = False
                    break
            if prime == True:
                num = []
                p = i
                while p != 0:
                    num.append(p % 10)
                    p = p // 10
                palindrome = True
                for j in range(len(num) // 2):
                    if num[j] != num[-(j+1)]:
                        palindrome = False
                        break
                if palindrome == True:
                    c += 1
        return c


