#https://leetcode.com/problems/number-of-islands/


from typing import List, Tuple, Set
from functools import reduce
class Solution:
    def neighbors(self, coords: Tuple[int,int], grid) -> Set:
        neighbors_set = set()
        direct_neighbors = [(0,0),(-1,0),(1,0),(0,-1),(0,1)]
        for (row,col) in direct_neighbors:
                new_row, new_col = (coords[0] + row, coords[1] + col)

                if new_row >=0 and new_row < len(grid) and new_col >= 0 and new_col < len(grid[0]):
                    if grid[new_row][new_col] == "1":
                        neighbors_set.add((new_row, new_col))

        return neighbors_set
       
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = list()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    neighbors = self.neighbors(coords=(row,col), grid=grid)
                    if not islands:
                        islands.append(neighbors)
                        continue
                    
                    islands_it_belongs = list(filter(lambda i: i.intersection(neighbors) != set(), islands))
                    islands_not_belonging = list(filter(lambda i: not i.intersection(neighbors), islands))


                    combined_island = reduce(lambda acc, curr: acc | curr,islands_it_belongs, neighbors)
                    islands = [combined_island] + islands_not_belonging

            

        return len(islands)

    def optimicedNumIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        num_islands = 0
        rows = len(grid)
        cols = len(grid[0])


        def dfs(row,col):

            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == "0":
                return
            
            grid[row][col] = "0"
            dfs(row-1,col)
            dfs(row+1,col)
            dfs(row,col-1)
            dfs(row,col+1)

        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    num_islands +=1
                    dfs(row,col)

        return num_islands



island_1 = [["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]]

island_2 = [["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]]

sol = Solution()

islands = sol.optimicedNumIslands(island_2)

print(islands)
