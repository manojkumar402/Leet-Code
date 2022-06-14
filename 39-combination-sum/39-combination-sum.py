from copy import copy
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.cs(0, candidates, target, 0, [], [])
        
    def cs(self, i, arr : list, B, sumTilnow, subSet : list, ans: list[list]) -> list[list]:

        if sumTilnow == B:
            ans.append(copy(subSet))
            return ans
        if sumTilnow > B:
            return
        if i >= len(arr):
            return


        # Skip the ith element
        self.cs(i + 1, arr, B, sumTilnow, subSet, ans)

        # Take the ith element
        # I made some disturbance so backtrack

        sumTilnow += arr[i]
        subSet.append(arr[i])

        self.cs(i, arr, B, sumTilnow, subSet, ans)

        sumTilnow -= arr[i] # BackTracking
        subSet.pop() # BackTracking

        return ans