from copy import copy
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.powerSet(candidates, len(candidates)-1, [], [], 0, target)
    
    def powerSet(self, nums, i, res, ans, sumTN, target):
        if sumTN == target:
            ans.append(copy(res))
            return
        if sumTN > target:
            return
        if (i < 0):
            return

        res.append(nums[i])
        sumTN += nums[i]
        self.powerSet(nums, i - 1, res, ans, sumTN, target)
        res.pop()
        sumTN -= nums[i]
        while (i > 0 and nums[i] == nums[i - 1]):
            i -= 1
        self.powerSet(nums, i - 1, res, ans, sumTN, target)
        return ans
        
        
    