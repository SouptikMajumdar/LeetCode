class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ans = 0
        rowCountsDict = {}
        for row in grid:
            rowCountsDict[tuple(row)] = 1 if tuple(row) not in rowCountsDict else rowCountsDict[tuple(row)] + 1
        
        for c in range(n):
            col = []
            for r in range(n):
                col.append(grid[r][c])
            
            if tuple(col) in rowCountsDict:
                ans += rowCountsDict[tuple(col)]
        
        return ans
