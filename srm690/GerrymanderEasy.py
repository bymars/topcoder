import heapq
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
        start = (B[0]+B[1])/(A[0]+A[1])
        all = (B[0]+B[1])/(A[0]+A[1])
        div = (A[0]+A[1])
        for i in range(2, len(A)):
            c = (B[i-1]+B[i])/(A[i-1]+A[i])
            newStart = (start*div+B[i])/(div+A[i])
            if (c > newStart):
                start = c
                div = (A[i-1]/A[i])
            else:
                start = newStart
                div = div + A[i]

            if (all < start):
               all = start
        return all
