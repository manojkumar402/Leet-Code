class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        self.solve(sr, sc, image[sr][sc], newColor, image)
        return image
        
    def solve(self, row, col, color, newcolor, image):
        if row < 0 or row >= len(image):
            return 
        if col < 0 or col >= len(image[0]):
            return
        image[row][col] = newcolor
        # up
        if row-1 >= 0 and image[row-1][col] == color:
            self.solve(row-1, col, color, newcolor, image)
        # down
        if row + 1 < len(image) and image[row+1][col] == color:
            self.solve(row+1, col, color, newcolor, image)
        # left
        if col + 1 < len(image[0]) and image[row][col+1] == color:
            self.solve(row, col+1, color, newcolor, image)
        # right
        if col - 1 >= 0 and image[row][col-1] == color:
            self.solve(row, col-1, color, newcolor, image)
        
        
        