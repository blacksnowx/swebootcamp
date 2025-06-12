class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # set up a queue
        q = deque()
        # track time as well as number of fresh oranges on the grid
        time, fresh = 0, 0
        # create variables to track coordinates as we move along the grid
        rows, cols = len(grid), len(grid[0])

        # Iterate over every cell in the grid
        for r in range(rows):
            for c in range(cols):
                # count up all the fresh oranges initially
                if grid[r][c] == 1:
                    fresh += 1
                # count up all the rotten oranges and add them to our queue at the same time
                if grid[r][c] == 2:
                    q.append([r, c])

        # create the list of directions we need to check for DFS (up, down, left, and right)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # run the DFS algo until queue is empty OR no more fresh oranges remain
        while q and fresh > 0:
            # run the BFS for ALL rotten oranges at time 0.
            for i in range(len(q)):
                # pop items (which are in coordinate form (r, c) out of the queue from the left
                # remember, queue holds items [r, c] from line 23 above
                r, c = q.popleft()
                # check all 4 directions from that coordinate
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    # skip if we're off the grid or we're not on a fresh orange
                    if (
                        row < 0
                        or row == len(grid)
                        or col < 0
                        or col == len(grid[0])
                        or grid[row][col] != 1
                    ):
                        continue
                    # otherwise, if we're on the grid and we're on a fresh orange
                    # change the fresh orange to a rotten one
                    grid[row][col] = 2
                    # add the newly rotten orange to our queue
                    q.append([row, col])
                    # reduce remaining fresh oranges by 1
                    fresh -= 1
            # now that we've cleared the first round of rotten orange BFS
            # increment time forward to the next minute (or round, if you will)
            time += 1
        # We're now out of fresh oranges or we've exhausted the rotting process
        # if we're out of oranges, return time (number of minutes or rounds)
        # otherwise, return -1, per the instructions of the problem
        return time if fresh == 0 else -1
