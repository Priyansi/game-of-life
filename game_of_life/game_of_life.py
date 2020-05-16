import random
import itertools
ALL_NEIGHBOURS = [
    neighbour for neighbour in itertools.product([-1, 0, 1], repeat=2) if not neighbour == (0, 0)]
DEAD = '0'
BLACK = 'B'


def add_blacks_around(grid):
    width = len(grid[0])
    new_grid = [BLACK+row+BLACK for row in grid]
    new_grid.append((width+2)*BLACK)
    new_grid.insert(0, (width+2)*BLACK)
    return new_grid


def add_dead_cells_around(grid):
    return [row.replace('B', '0') for row in grid]


def find_random_value():
    return 1 if random.randint(1, 100) > 75 else 0


def create_grid(rows):
    return add_blacks_around([''.join(str(find_random_value()) for column in range(rows)) for row in range(rows)])


def is_cell_near_edge(grid, rows):
    if grid[1].find('1') != -1 or grid[-2].find('1') != -1:
        return True
    for row in grid[1:-1]:
        if row[0] == '1' or row[-1] == '1':
            return True
    return False


def update_grid(grid, rows):
    def count_living_neighbours(row, column):
        return len([1 for row_neighbour, column_neighbour in ALL_NEIGHBOURS if grid[row + row_neighbour][column + column_neighbour] == '1'])

    if is_cell_near_edge(grid, rows):
        grid = add_blacks_around(add_dead_cells_around(grid))
        rows += 2
    new_grid = grid.copy()
    for row in range(1, rows+1):
        for column in range(1, rows+1):
            living_neighbours = count_living_neighbours(row, column)
            if living_neighbours in (2, 3):
                if living_neighbours == 3 and grid[row][column] == '0':
                    new_grid[row] = new_grid[row][:column] + \
                        '1'+new_grid[row][column+1:]
            else:
                new_grid[row] = new_grid[row][:column] + \
                    '0'+new_grid[row][column+1:]
    return new_grid, rows


def game(rows, CYCLES=1):
    all_generations = []
    grid = create_grid(rows)
    all_generations.append(grid)
    for cycle in range(CYCLES):
        grid, rows = update_grid(grid, rows)
        all_generations.append(grid)
    return all_generations


if __name__ == "__main__":
    for generation in game(4, 6):
        for row in generation:
            for column in row:
                print(column, end=' ')
            print()
        print()
