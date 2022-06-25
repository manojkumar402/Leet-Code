class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        ans = []
        for each in nums:
            if each in d:
                d[each] -= 1
            else:
                d[each] = -1
        heap = []
        for key in d:
            heapq.heappush(heap, (d[key], key))
        c = 0
        while c < k:
            freq, itm = heapq.heappop(heap)
            ans.append(itm)
            c+=1
        return ans
        # keys = list(d.keys())
        # values = list(d.values())
        # while k>0:
        #     max_freq = max(values)
        #     l = values.index(max_freq)
        #     ans.append(keys[l])
        #     values.pop(l)
        #     keys.pop(l)
        #     k = k - 1
        # return ans