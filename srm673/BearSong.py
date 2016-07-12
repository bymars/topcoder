class BearSong:
    def countRareNotes(self, notes):
        count = 0
        for item in notes:
            if notes.count(item) == 1:
                count += 1
        return count

