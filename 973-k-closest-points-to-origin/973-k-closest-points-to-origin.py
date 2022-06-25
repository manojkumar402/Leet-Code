class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for each in points:
            p1 = each[0] * each[0]
            p2 = each[1] * each[1]
            heapq.heappush(heap, (-1 * math.sqrt(p1 + p2), each)) 
            # dist.append(math.sqrt(p1 + p2))
        # dist.sort()
        while len(heap) > k:
            heapq.heappop(heap)
        while len(heap) > 0:
            key, itm = heapq.heappop(heap)
            res.append(itm)
        return res