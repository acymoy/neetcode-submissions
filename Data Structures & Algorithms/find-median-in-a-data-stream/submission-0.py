class MedianFinder:

    def __init__(self):
        self.min_heap = [] # holds the bigger half of the array
        self.max_heap = [] # holds the smaller half of the array

    def addNum(self, num: int) -> None:
        if not (self.min_heap or self.max_heap):
            self.max_heap.append(num)
        else:   
            if self.max_heap and self.max_heap[0] >= num:
                heapq.heappush_max(self.max_heap, num)
            else:
                heapq.heappush(self.min_heap, num)
                
            if abs(len(self.max_heap) - len(self.min_heap)) > 1:
                if len(self.max_heap) - len(self.min_heap) > 1:
                    value = heapq.heappop_max(self.max_heap)
                    heapq.heappush(self.min_heap, value)
                else:
                    value = heapq.heappop(self.min_heap)
                    heapq.heappush_max(self.max_heap, value)

    def findMedian(self) -> float:
        if (len(self.max_heap) + len(self.min_heap)) % 2 == 0:
            return (self.max_heap[0] + self.min_heap[0]) / 2
        if len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0]
        else:
            return self.min_heap[0]
        