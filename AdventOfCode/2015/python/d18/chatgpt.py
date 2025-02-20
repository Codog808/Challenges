def parse_input(lines):
    """
    Parse the input lines (each line is a string of '.' and '#'),
    and store them in a 2D list of booleans:
      True  -> light is on  ('#')
      False -> light is off ('.')
    """
    grid = []
    for line in lines:
        row = [True if ch == '#' else False for ch in line.strip()]
        grid.append(row)
    return grid

def count_on_neighbors(grid, r, c):
    """
    Given the current grid, count how many of the eight neighbors
    around grid[r][c] are on (True).
    """
    rows = len(grid)
    cols = len(grid[0])
    on_count = 0
    
    # Offsets for the eight possible neighbors
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            # Skip the cell itself
            if dr == 0 and dc == 0:
                continue
            
            rr = r + dr
            cc = c + dc
            # Check bounds
            if 0 <= rr < rows and 0 <= cc < cols:
                if grid[rr][cc]:
                    on_count += 1
    return on_count

def step_grid(grid):
    """
    Perform one animation step on the grid according to the rules:
      - A light which is on stays on when 2 or 3 neighbors are on, 
        and turns off otherwise.
      - A light which is off turns on if exactly 3 neighbors are on, 
        and stays off otherwise.
    """
    rows = len(grid)
    cols = len(grid[0])
    
    # We'll build the next grid state from scratch
    new_grid = [[False]*cols for _ in range(rows)]
    
    for r in range(rows):
        for c in range(cols):
            on_count = count_on_neighbors(grid, r, c)
            if grid[r][c]:
                # Light is currently on
                if on_count in [2, 3]:
                    new_grid[r][c] = True
                else:
                    new_grid[r][c] = False
            else:
                # Light is currently off
                if on_count == 3:
                    new_grid[r][c] = True
                else:
                    new_grid[r][c] = False
    return new_grid

def count_lights_on(grid):
    """
    Return how many lights are on (True) in the given grid.
    """
    return sum(sum(1 for cell in row if cell) for row in grid)

if __name__ == "__main__":
    # Example usage:
    # Suppose we read from a file or standard input a 100x100 grid of lines.
    # Here is how you'd do it if you had the puzzle input in a file:
    #
    # with open("puzzle_input.txt") as f:
    #     lines = f.readlines()
    #
    # grid = parse_input(lines)
    #
    # for _ in range(100):
    #     grid = step_grid(grid)
    #
    # print("Number of lights on after 100 steps:", count_lights_on(grid))

    # For demonstration, here's a small example (6x6) from the puzzle statement:
    example_lines = [
        ".#.#.#",
        "...##.",
        "#....#",
        "..#...",
        "#.#..#",
        "####.."
    ]
    
    #grid = parse_input(example_lines)
    grid = parse_input(open("input").read().strip().splitlines())
    steps = 100  # the example walked through 4 steps
    
    for _ in range(steps):
        grid = step_grid(grid)
    
    print("After {} steps, {} lights are on.".format(steps, count_lights_on(grid)))

