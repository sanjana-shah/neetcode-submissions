class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # dfs/bfs to find the extent
        # traverse the grid
        def validBounds(x: int, y: int) -> bool:
            return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])


        def dfs(x: int, y: int):
            directions = [[0, 1], [1,0], [0, -1], [-1,0]]

            for direction in directions:
                i = x + direction[0]
                j = y + direction[1]
                if validBounds(i, j) and grid[i][j] == "1":
                    grid[i][j] = "-1"
                    dfs(i, j)



        islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    islands += 1
                    grid[i][j] = "-1"
                    dfs(i, j)

        return islands