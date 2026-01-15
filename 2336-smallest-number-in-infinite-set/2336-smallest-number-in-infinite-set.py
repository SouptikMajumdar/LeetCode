class SmallestInfiniteSet:

    def __init__(self):
        self.minHeap = []
        self.addedBack = set()
        self.smallest = 1



    def popSmallest(self) -> int:
        if self.minHeap:
            smallest = heapq.heappop(self.minHeap)
            self.addedBack.remove(smallest)
            return smallest
        ret = self.smallest
        self.smallest += 1
        return ret

        """ret = self.smallest
        self.removed.append(ret)
        self.removed.sort()
        self.smallest = self.find_smallest()
        return ret """

    def addBack(self, num: int) -> None:
        if num < self.smallest and num not in self.addedBack:
            heapq.heappush(self.minHeap, num)
            self.addedBack.add(num)


"""     def find_smallest(self) -> int:
        if len(self.removed) == 0:
            return -1
        if len(self.removed) == 1:
            return self.removed[0] + 1
        for i in range(0,len(self.removed)-1):
            if self.removed[i]+1 != self.removed[i+1]:
                return self.removed[i] + 1
        return self.removed[-1] + 1 """


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)