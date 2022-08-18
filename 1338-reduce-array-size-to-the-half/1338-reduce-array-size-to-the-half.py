class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        size = len(arr)
        heap = []
        d = {}
        for each in arr:
            if each not in d:
                d[each] = 1
            else:
                d[each] += 1
        for key in d:
            heapq.heappush(heap, [-1 * d[key], key])
        print(heap)
        # [-1 * d[key]]
        req = size // 2
        c = 0
        while size > req:
            a = heapq.heappop(heap)
            c += 1
            size = size - abs(a[0])
        return c
            
    