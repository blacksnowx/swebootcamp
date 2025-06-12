class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        if not grid:
            return 0

        num_islands = 0
        # Set up variables for tracking row, column coordinates
        rows = len(grid)
        cols = len(grid[0])

        # Traverse the grid, looking for "land" (1's)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    # Once we encounter land, increment num_islands
                    num_islands += 1
                    # Now run Depth First Search algorithm to find borders of the land
                    self._dfs_sink(grid, r, c)

        return num_islands

    # This helper is going to do all the DFS until we've found the boundaries of the current island
    # Because we're in a Class and we aren't inside another method, get all the attributes again
    # self, grid, r, and c
    def _dfs_sink(self, grid, r, c):
        # Create variables to find edges of the overall grid
        rows = len(grid)
        cols = len(grid[0])
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
            return
        grid[r][c] = "#"

        # Within this loop, if we're looking at "land", run this recursively on all adjacencies
        self._dfs_sink(grid, r + 1, c)
        self._dfs_sink(grid, r - 1, c)
        self._dfs_sink(grid, r, c + 1)
        self._dfs_sink(grid, r, c - 1)
