def findMax(s, start, end):
    if end - start == 1:
        return s[start]
    left = findMax(s, start, start + (end - start) // 2)
    right = findMax(s, start + (end - start) // 2, end)
    return left if left > right else right

class TreeAndVertex:
    def get(self, tree):
        record = [0] * 99
        for i in range(len(tree)):
            record[tree[i]] += 1
            record[i+1]+=1
        return findMax(record, 0, len(record))
