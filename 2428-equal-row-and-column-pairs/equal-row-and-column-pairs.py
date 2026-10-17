class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        n = len(grid)
        counter = 0
        hashmaprow = {}
        for row in grid:
            hashmaprow[tuple(row)] = hashmaprow.get(tuple(row), 0) + 1
        for i in range(n):
            column = [] * n
            for j in range(n):
                column.append(grid[j][i])
            counter = counter + hashmaprow.get(tuple(column), 0)
        return counter