from collections import deque
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        adj = [[] for i in range(len(quiet))]
        n = len(quiet)
        ans = []
        for each in richer:
            adj[each[1]].append(each[0])
        for i in range(n):
            vis = [0 for i in range(n)]
            ans.append(self.bfs(adj, vis, i, [quiet[i],-1], quiet))
        res = []
        for i in range(n):
            if ans[i][1] != -1:
                res.append(ans[i][1])
            else:
                res.append(i)
        return res
        #  0 -> node 5
        #  1 -> 5
        #  2->  5
        #  3 -> 
    def bfs(self, adj, vis, root, ans, quiet):
        q = deque()
        q.append(root)
        while len(q) > 0:
            node = q[0]
            vis[node] = 1
            if quiet[node] < ans[0]:
                ans[0] = quiet[node]
                ans[1] = node
            q.popleft()
            for each in adj[node]:
                if vis[each] != 1:
                    q.append(each)
        
        return ans