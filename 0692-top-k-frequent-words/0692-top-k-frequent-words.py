import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        for word in words:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
        res = sorted(d, key=lambda x: (-d[x], x))
        return res[:k]
#         for key in d:
#             heapq.heappush(heap, [d[key], key])
#             if len(heap) > k:
#                 heapq.heappop(heap)
#         # lexi order
#         print(heap)
#         heap = heap[::-1]
#         res = []
#         new = {}
#         for each in heap:
#             if each[0] in new:
#                 new[each[0]].append(each[1])
#             else:
#                 new[each[0]] = [each[1]]

#         for key in new:
#             res += (sorted(new[key]))
#         return res