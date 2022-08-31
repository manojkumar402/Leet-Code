class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = {}
        res = []
        n = len(nums)
        for each in nums:
            if each in d:
                d[each] += 1
            else:
                d[each] = 1
        for key in d:
            if d[key] > n // 3:
                res.append(key)
        return res