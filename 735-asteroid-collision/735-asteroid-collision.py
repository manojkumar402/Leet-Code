class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        i = 0
        while i < len(asteroids):
            curr = asteroids[i]
            
            # if curr goes right or stack top goes left - stack stays stable when added
            if curr > 0 or len(stack) == 0 or stack[-1] < 0:
                stack.append(curr)
                
            # if curr is negative, stack top is positive and values are equal - both will explode
            elif abs(curr) == stack[-1]:
                stack.pop()
                i += 1
                continue
            
            # if curr is negative, stack top is positive and curr > stack top - stack top will explode
            elif abs(curr) > stack[-1]:
                stack.pop()
                i -= 1
            i+=1
                
        return stack
