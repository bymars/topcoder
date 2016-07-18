def inc_c(arr, n, c):
    found = 0
    for i in range(len(arr)):
        if arr[i][0] == n:
            arr[i][1] += c
            found = 1
            break
    if found == 0:
        arr.append([n, c])

def inc(arr, n):
    inc_c(arr, n, 1)

def dec(arr, n):
    for i in range(len(arr)):
        if arr[i][0] == n:
            arr[i][1] -= 1
            if arr[i][1] == 0:
                del(arr[i])
            break

def find(arr, n):
    for i in range(len(arr)):
        if arr[i][0] == n:
            return i
    return -1

class BearDartsDiv2:
    def count(self, w):
        l = len(w)
        a_count = []
        d_count = []
        ab_count = []

        res = 0
        for i in range(2, l):
            inc(d_count, w[i])

        for c_pos in range(2, l - 1):
            dec(d_count, w[c_pos])
            inc(a_count, w[c_pos - 2])
            b_pos = c_pos - 1
            for i in range(len(a_count)):
                inc_c(ab_count, w[b_pos] * a_count[i][0], a_count[i][1])
            for i in range(len(d_count)):
                if d_count[i][0] % w[c_pos] == 0:
                    ab = d_count[i][0] // w[c_pos]
                    j = find(ab_count, ab)
                    if j != -1:
                        res += ab_count[j][1] * d_count[i][1]
        return res
