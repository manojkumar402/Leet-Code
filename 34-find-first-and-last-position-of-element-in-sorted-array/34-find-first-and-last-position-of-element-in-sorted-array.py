class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1] * 2
        start = self.searchTarget(nums,target,True)
        end = self.searchTarget(nums,target,False)
        ans[0] = start
        ans[1] = end
        return ans
    
    def searchTarget(self, nums: List[int], target: int, findStartIndex: bool) -> int:
        ans = -1
        start = 0
        end = len(nums)-1
        while start<=end:
            mid = start + (end-start) //2
            if target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                ans = mid
                if findStartIndex:
                    end = mid -1
                else:
                    start = mid + 1
        return ans