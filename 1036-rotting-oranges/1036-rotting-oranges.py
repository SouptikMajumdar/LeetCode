class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        queue = deque()
        fresh = 0

        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
                
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for d in directions:
                    nr, nc = r + d[0], c + d[1]
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
            minutes += 1
        

        return minutes if fresh == 0 else -1
