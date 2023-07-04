from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

maze = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 0, 1]]

grid = Grid(matrix = maze)

start = grid.node(0,0)
end = grid.node(6,3)

finder = AStarFinder()

path, cells = finder.find_path(start,end,grid)

print(path)
print(cells)