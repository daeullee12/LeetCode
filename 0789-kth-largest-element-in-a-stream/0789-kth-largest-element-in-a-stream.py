class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """

        # O(nlogn)
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap) # O((nlogn)
        while len(self.minHeap) > k: # O((n-k)logn)
            heapq.heappop(self.minHeap) 
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        # O((n-k)logn)
        heapq.heappush(self.minHeap, val) # O(logn)
        while len(self.minHeap) > self.k: # O((n-k)logn)
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)