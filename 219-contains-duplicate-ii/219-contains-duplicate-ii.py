class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = [i]
            else:
                d[nums[i]] += [i]
                # if abs(d[nums[i]] - i) <= k:
                #     return True
        for key in d:
            tmp = d[key]
            if len(tmp) >= 2:
                for i in range(len(tmp)-1):
                    if abs(tmp[i] - tmp[i+1]) <= k:
                        return True
        
        # return False