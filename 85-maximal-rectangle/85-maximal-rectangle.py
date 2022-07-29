class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxArea = float('-inf')
        height = [0 for i in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    height[j] +=1
                else:
                    height[j] = 0
            # print(height)
            maxArea = max(maxArea, self.largestRectangleArea(height))
        return maxArea
            
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                ans = max(ans, height * width)
            stack.append(i)
        heights.pop()
        return ans