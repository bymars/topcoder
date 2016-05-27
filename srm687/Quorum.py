import heapq
class Quorum:
    def count(self, arr, k):
        heap = []
        for item in arr:
            item = -item
            if len(heap) < k:
                heapq.heappush(heap, item)
            else:
                if heap[0] < item:
                    heapq.heapreplace(heap, item)
        sum = 0
        for item in heap:
            sum += item
        return -sum
