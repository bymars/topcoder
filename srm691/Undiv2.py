def gcd(x,y):
    return x if y == 0 else gcd(y,x%y)

def lcm(x,y):
    return x // gcd(x,y) * y

class Undiv2:
    def getsum(self, n):
        '''
        Make two for loop, for i, for j. i = 2...n, j = i+1....n
        means find the number 'x' can't be divided by both i and j.
        and j is the number we want to calculate. then sum += j*x
        for example: find x when n = 220 and i = 4, j = 7.
        This means find number CAN be divided by 1,2,3,5,6 and
        CANNOT be divieded by 4,7
        number can divided by 1,2,3,5,6 = all number can divided by lcm(1,2,3,5,6) = 30
            we can get 30,60,90,120,150,180,210
        number can't be divided by 4 at meantime: all number divided by gcd(30,4) = 60
            we can get 60,120,180
        number can't be divided by 7 at meantime: all number divided by gcd(30,7) = 210
            we can get 210, 420, 630
        number gcd(30,4*7) was calculated twice
        Finally, we get 30, 90
        '''
        sum = 0
        div1 = 1
        i = 2
        while div1 <= n:
            div2 = div1
            j = i + 1

            while div2 <= n:
                sum += (n//div2 - n//lcm(div2,i) - n//lcm(div2,j) + n//lcm(div2, lcm(i,j))) * j
                div2 = lcm(div2, j)
                j += 1

            div1 = lcm(div1, i)
            i += 1
        return sum
