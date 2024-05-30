#!/usr/bin/python3
'''
island perimeter
'''


def island_perimeter(grid):
    ''' calculates the island perimeter of grid. '''
    length = 0
    width = 0
    for n in range(0, len(grid)+1):
        current_grid = grid[n]
        num_ones = 0
        for o in range(0, len(current_grid) + 1):
            if current_grid[o] == 0:
                num_ones += 1
        if num_ones != 0:
            length += 1
        if num_ones > width:
            width = num_ones
    return 2 * (length + width)
