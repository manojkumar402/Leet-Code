class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
    # TLE how to use dp ??? 
    def solve(self, i, j, piles, a, b, turn):
        if i > j:
            if a > b:
                return True
            return False
        # alice takes first one
        q,w,e,r = False, False, False, False
        if turn:
            # alice
            turn = 0
            q = self.solve(i+1, j, piles, a + piles[i], b, turn)
            w = self.solve(i, j -1, piles, a + piles[j], b, turn)
        else:
            turn = 1
            e = self.solve(i+1, j, piles, a, b + piles[i], turn)
            r = self.solve(i, j -1, piles, a, b + piles[j], turn)
        return q or w or e or r