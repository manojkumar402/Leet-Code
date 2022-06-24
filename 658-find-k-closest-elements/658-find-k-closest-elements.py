class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        result = []
        for i in arr:
            heapq.heappush(heap, (abs(i - x), i))
        # print(heap)
        while k > 0:
            # print(heapq.heappop(heap)[1])
            result.append(heapq.heappop(heap)[1])
            k-= 1
        
        return sorted(result)