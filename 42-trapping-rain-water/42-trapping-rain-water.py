class Solution:
    def trap(self, height: List[int]) -> int:
        water = []
        mLeft = []
        mRight =[0 for i in range(len(height))]
        mLeft.append(height[0])
        mRight[len(height) - 1] = height[len(height) - 1]
        for i in range(1, len(height)):
            mLeft.append(max(mLeft[i-1], height[i]))
        # print(mLeft)
        for j in range(len(height)-2,-1,-1):
            mRight[j] = max(mRight[j+1], height[j])
        # print(mRight)
        for i in range(len(height)):
            val = min(mLeft[i], mRight[i]) - height[i]
            water.append(val)
        return sum(water)
           
