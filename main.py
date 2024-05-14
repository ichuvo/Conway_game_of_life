# Define the grid dimensions
width = 200
height = 200


def count_live_neighbors(grid, x, y):
  """
  Counts the number of live neighbors around a specific cell in the grid.

  Args:
      grid: A 200x200 grid (list of lists) with 0s (dead) and 1s (live).
      x: X-coordinate of the cell.
      y: Y-coordinate of the cell.

  Returns:
      The number of live neighbors surrounding the cell at (x, y).
  """

  live_neighbors = 0

  # Iterate through the eight neighbors (up, down, left, right, diagonals)
  for dy in range(-1, 1):  # Corrected range: -1 to 1 (inclusive)
    for dx in range(-1, 1):  # Corrected range: -1 to 1 (inclusive)
      # Skip the current cell (dx, dy = 0, 0)
      if dx == 0 and dy == 0:
        continue

      # Calculate neighbor coordinates (considering wrapping around the grid)
      neighbor_x = (x + dx) % 200  # Modulo 200 to handle wrapping
      neighbor_y = (y + dy) % 200

      # Check if neighbor is within the grid and alive
      if 0 <= neighbor_x < 200 and 0 <= neighbor_y < 200 and grid[neighbor_y][neighbor_x] == 1:
        live_neighbors += 1

  return live_neighbors


def create_grid(width, height, live_cells):
  """
  Creates a 200x200 grid and marks live cells based on coordinates.

  Args:
      width: Grid width (200 in this case).
      height: Grid height (200 in this case).
      live_cells: List of lists containing coordinates (x, y) of live cells.

  Returns:
      A 200x200 grid (list of lists) with 0s (dead) and 1s (live) marked based on input coordinates.
  """

  grid = [[0 for _ in range(width)] for _ in range(height)]  # Initialize grid with all 0s

  # Mark live cells based on coordinates
  for x, y in live_cells:
    if 0 <= x < width and 0 <= y < height:  # Check for valid coordinates within the grid
      grid[y][x] = 1  # Mark the cell at (y, x) as live (1)

  return grid

def get_live_cells():
  """Prompts the user for all live cell coordinates and returns them as a list of lists.

  Returns:
      A list of lists containing coordinates (x, y) of live cells provided by the user.
  """

  while True:
    # Get user input for all live cells at once
    live_cells_str = input("Enter all live cell coordinates as a list (e.g., [[5, 5], [6, 5], ...]): ")

    try:

      live_cells = eval(live_cells_str)

      # Validate the format of the entered list
      if not isinstance(live_cells, list):
        raise ValueError("Invalid format! Please enter a list of coordinates.")
      for inner_list in live_cells:
        if not isinstance(inner_list, list) or len(inner_list) != 2:
          raise ValueError("Invalid format! Each inner list should have two elements (x, y).")
        x, y = inner_list
        if x < 0 or x >= 200 or y < 0 or y >= 200:
          raise ValueError("Invalid coordinates! Please enter values between 0 and 199 (inclusive).")

      # Valid input, break out of the loop
      break

    except (ValueError, SyntaxError):
      # Handle various input errors
      print("Invalid input! Please enter a valid list of coordinates (e.g., [[5, 5], [6, 5], ...]).")

  return live_cells

def update_cells(grid):
  """
  Updates the state of cells in the grid based on Conway's Game of Life rules.

  Args:
      grid: A 200x200 grid (list of lists) with 0s (dead) and 1s (live).

  Returns:
      A new 200x200 grid (list of lists) representing the next generation.
  """

  # Create a new grid to store the next generation
  new_grid = [[0 for _ in range(200)] for _ in range(200)]

  # Iterate through each cell in the current grid
  for y in range(200):
    for x in range(200):
      # Count live neighbors around the current cell
      live_neighbors = count_live_neighbors(grid, x, y)

      # Apply Conway's Game of Life rules
      if grid[y][x] == 1:  # Live cell
        if live_neighbors < 2 or live_neighbors > 3:
          new_grid[y][x] = 0  # Dies (underpopulation or overcrowding)
        else:
          new_grid[y][x] = 1  # Lives on to the next generation
      else:  # Dead cell
        if live_neighbors == 3:
          new_grid[y][x] = 1  # Becomes alive (reproduction)
        else:
          new_grid[y][x] = 0  # Stays dead

  return new_grid

# Example usage
live_cells = get_live_cells()

# The live_cells list containing coordinates in the desired format.
print(f"Live cells entered by the user: {live_cells}")





