class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands_count = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return

            grid[r][c] = "0"

            dfs(r + 1, c)  # вниз
            dfs(r - 1, c)  # вверх
            dfs(r, c + 1)  # вправо
            dfs(r, c - 1)  # влево

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands_count += 1
                    dfs(r, c)

        return islands_count
