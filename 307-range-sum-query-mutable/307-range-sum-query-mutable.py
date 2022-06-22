class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = nums
        self.sum = sum(nums)

    def update(self, index: int, val: int) -> None:
        if index >= 0 and index < len(self.arr):
            n = self.arr[index]
            self.arr[index] = val
            self.sum = self.sum + val - n


    def sumRange(self, left: int, right: int) -> int:
        right = sum(self.arr[right+1:])
        left = sum(self.arr[0:left])
        return self.sum - right - left
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)