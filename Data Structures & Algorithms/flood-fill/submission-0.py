class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        color_to_change = image[sr][sc]
        if color_to_change == color: return image
        
        def dfs(r, c):
            if not (0 <= r < ROWS and 0 <= c < COLS) or image[r][c] != color_to_change:
                return
            image[r][c] = color
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        dfs(sr, sc)

        return image