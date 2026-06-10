class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()


        def dfs(r, c):

            if not( 0 <= r < ROWS and 0 <= c < COLS) or grid[r][c] == 0:
                return

            visited.add((r, c))
            nonlocal perimeter
            perimeter += 4

            nbrs = [(r+1, c), (r-1, c), (r, c+1), (r, c-1) ]
            nbr_count = 0
            for x, y in nbrs:
                if 0 <= x < ROWS and 0 <= y < COLS and grid[x][y] == 1 and (x, y) in visited:
                    perimeter -= 2
            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    dfs(r, c)
        
        return perimeter