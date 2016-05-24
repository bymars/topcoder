import heapq

def arraySum(A, start, end):
    sum = 0
    for i in range(start, end):
        sum += A[i]
    return sum
class GerrymanderEasy:
    '''
    def getmax(self, A, B, K):
        C = []
        for i in range(0, len(A) - 1):
            temp = B[i] / A[i]
            if len(C) >= K and temp > C[0]:
                heapq.heapreplace(C, temp)
            else:
                heapq.heappush(C, temp)
        print(C)
        sum = 0
        for item in C:
            sum += item
        return sum / len(C)
    '''
    def getmax(self, A, B, K):
        div = arraySum(A, 0, K)
        start = arraySum(B, 0, K)/ div
        all = start
        for i in range(K, len(A)):
            c = arraySum(B, i+1-K, i+1) / arraySum(A, i+1-K, i+1)
            newStart = (start*div+B[i])/(div+A[i])
            if (c > newStart):
                start = c
                div = arraySum(A, i+1-K, i+1)
            else:
                start = newStart
                div = div + A[i]

            if (all < start):
               all = start
        return all
