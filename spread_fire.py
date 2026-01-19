def spread_fire(grid):
    """Update the forest grid based on fire spreading rules."""
    update_grid = grid.copy()
    grid_size = len(grid)

    for i in range(grid_size-1):
        for j in range(grid_size-1):
          if grid[i,j] == 1 and i < 29 and j < 29 and i > 0 and j > 0:
              neighbors = [grid[i - 1,j], grid[i + 1,j], grid[i,j - 1], grid[i,j + 1]]
              if 2 in neighbors:
                  update_grid[i,j] = 2

          if i == 29 and grid[i,j] == 1 and j < 29:
                neighbors = [grid[i - 1,j], grid[i,j - 1], grid[i,j + 1]]
                if 2 in neighbors:
                    update_grid[i,j] = 2

          if j == 29 and grid[i,j] == 1 and i < 29:
              neighbors = [grid[i - 1,j], grid[i + 1,j], grid[i,j - 1]]
              if 2 in neighbors:
                  update_grid[i,j] = 2

          if i == 29 and j == 29 and grid[i,j] == 1:
              neighbors = [grid[i - 1,j], grid[i,j - 1]]
              if 2 in neighbors:
                  update_grid[i,j] = 2
          
          if i == 0 and grid[i,j] == 1 and j < 29 and j > 0:
              neighbors = [grid[i + 1,j], grid[i,j - 1], grid[i,j + 1]]
              if 2 in neighbors:
                  update_grid[i,j] = 2

          if j == 0 and grid[i,j] == 1 and i < 29 and i > 0:
              neighbors = [grid[i - 1,j], grid[i + 1,j], grid[i,j + 1]]
              if 2 in neighbors:
                  update_grid[i,j] = 2
          
          if i == 0 and j == 0 and grid[i,j] == 1:
              neighbors = [grid[i + 1,j], grid[i,j + 1]]
              if 2 in neighbors:
                  update_grid[i,j] = 2

    return update_grid
