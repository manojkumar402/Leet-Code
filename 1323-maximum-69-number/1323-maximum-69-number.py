class Solution:
    def maximum69Number (self, num: int) -> int:
             
        def revNum(num):
            revNum = 0
            while num > 0:
                rem = num % 10
                revNum = revNum * 10 + rem
                num = num // 10
            return revNum
        n = revNum(num)
        f=False
        res = 0
        while n > 0:
            if n % 10 == 6 and not f:
                f = True
                res = res * 10 + 9
            else:
                res = res * 10 + n % 10
            n = n // 10
        return res