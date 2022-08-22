class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj = [[] for i in range(len(isConnected)+1)]
        for r in range(len(isConnected)):
            for c in range(len(isConnected)):
                if r != c and isConnected[r][c] == 1:
                    adj[r+1].append(c+1)
        for each in adj:
            print(each)
        vis = [0 for i in range(len(isConnected) + 1)]
        cnt = 0
        for node in range(1, len(isConnected)+1):
            if vis[node] == 0:
                cnt += 1
                self.dfs(node, adj, vis)
        return cnt
    def dfs(self, node, adj, vis):
        vis[node] = 1
        for each in adj[node]:
            if vis[each] == 0:
                self.dfs(each, adj, vis)
    
            