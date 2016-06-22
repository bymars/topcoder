# Used 15min
class DNASequence:
    def longestDNASequence(self, sequence):
        max = 0
        current = 0
        DNA = "ACGT"
        for i in range(len(sequence)):
            if sequence[i] in DNA:
                current += 1
            else:
                max = current if current > max else max
                current = 0
        max = current if current > max else max
        return max
