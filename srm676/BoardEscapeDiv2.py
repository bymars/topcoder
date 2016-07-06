def up(pos):
    return [pos[0] - 1, pos[1]]
def down(pos):
    return [pos[0] + 1, pos[1]]
def left(pos):
    return [pos[0], pos[1] - 1]
def right(pos):
    return [pos[0], pos[1] + 1]

def moveable(s, pos):
    rows = len(s)
    columns = len(s[0])
    i = pos[0]
    j = pos[1]
    if i < 0 or j < 0 or i >= rows or j >= columns or s[i][j] == '#':
        return False
    else:
        return True

def stuck(s, pos):
    return not (moveable(s, up(pos)) or moveable(s, down(pos)) or moveable(s, left(pos)) or moveable(s, right(pos)))

def nextToExit(s, pos):
    return (exitable(s, up(pos)) or exitable(s, down(pos)) or exitable(s, left(pos)) or exitable(s, right(pos)))

def exitable(s, pos):
    return moveable(s, pos) and s[pos[0]][pos[1]] == 'E'

class BoardEscapeDiv2:
    def findWinner(self, s, k):
        x = -1
        y = -1
        for i in range(len(s)):
            for j in range(len(s[i])):
                if s[i][j] == 'T':
                    x = i
                    y = j
                    break
            if x != -1 and y != -1:
                break
        pos = [x, y]
        if stuck(s, pos):
            return "Bob"
        if k % 2 == 0:
            return "Alice" if nextToExit(s, pos) else "Bob"
        else:
            if not moveable(s, up(pos)) or nextToExit(s, up(pos)):
                if not moveable(s, down(pos)) or nextToExit(s, down(pos)):
                    if not moveable(s, left(pos)) or nextToExit(s, left(pos)):
                        if not moveable(s, right(pos)) or nextToExit(s, right(pos)):
                            return "Bob"
            return "Alice"
