class Solution:

    def isExit(self, current: List[int], maze: List[List[str]], entrance: List[int]) -> bool:
        if (self.m == current[0] or 0 == current[0]) or (self.n == current[1] or 0 == current[1]):
            if maze[current[0]][current[1]] == ".":
                return current != entrance
        return False   
    def traverse(self, current: List[int], step: str, maze: List[List[str]]) -> List[int]:
        #print(current, step)
        if step == "up" and current[0] != 0 and maze[current[0] - 1][current[1]] != "+":
            return [current[0] - 1, current[1]]
        if step == "down" and current[0] != self.m and maze[current[0] + 1][current[1]] != "+":
            return [current[0] + 1, current[1]]
        if step == "left" and current[1] != 0 and maze[current[0]][current[1] - 1] != "+":
            return [current[0], current[1] - 1]
        if step == "right" and current[1] != self.n and maze[current[0]][current[1] + 1] != "+":
            return [current[0], current[1] + 1]
        return None 

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        self.m = len(maze) - 1
        self.n = len(maze[0]) - 1
        queue = deque([(entrance, 0)])
        visited = set()
        visited.add(tuple(entrance))
        directions = ["up", "down", "left", "right"]

        while queue:
            current, steps = queue.popleft()
            for step in directions:
                next_cell = self.traverse(current, step, maze)
                if next_cell and tuple(next_cell) not in visited:
                    if self.isExit(next_cell, maze, entrance):
                        return steps + 1
                    visited.add(tuple(next_cell))
                    queue.append((next_cell, steps + 1))
        return -1






        