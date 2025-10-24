class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        maxClusters = len(isConnected)
        visited = [False] * maxClusters
        provinces = 0

        def dfs(currNode):
            visited[currNode] = True
            for j, connected in enumerate(isConnected[currNode]):
                if not visited[j] and connected == 1:
                    dfs(j)
        
        for i in range(maxClusters):
            if not visited[i]:
                dfs(i)
                provinces += 1
        
        return provinces 

        


                
