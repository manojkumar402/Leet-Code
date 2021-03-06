class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
    
        heap = []
        for key in counts:
            heapq.heappush(heap, (counts[key], (-1 *key)))
        
        output = []
        while heap:
            count, val = heapq.heappop(heap)
            val *= -1
            
            for i in range(count):
                output.append(val)
        return output	
        