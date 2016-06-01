class Plusonegame:
    def getorder(self, s):
        record = [0] * 10
        count = 0
        output = ""
        for i in s:
            if i == '+':
                count += 1
            else:
                record[int(i)] += 1
        for i in range(len(record)):
            for j in range(record[i]):
                output += str(i)
            if count > 0:
                output += '+'
                count -= 1
        for i in range(count):
            output += '+'
        return output
