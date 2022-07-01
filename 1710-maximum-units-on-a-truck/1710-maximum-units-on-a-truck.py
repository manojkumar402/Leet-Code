class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda boxTypes:boxTypes[1], reverse=True)
        ans = 0
        # print(boxTypes)
        for i in range(len(boxTypes)):
            if truckSize == 0:
                break
            if truckSize > 0 and truckSize >= boxTypes[i][0]:
                truckSize = truckSize - boxTypes[i][0]
                ans = ans + boxTypes[i][0] * boxTypes[i][1]
                # print(truckSize, ans)
            elif truckSize > 0 and truckSize < boxTypes[i][0]:
                ans = ans + truckSize * boxTypes[i][1]
                truckSize = 0
                # print(truckSize, ans)
        return ans
            