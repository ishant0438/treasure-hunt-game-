import random

def create_grid(size):
    """Create a grid with a hidden treasure."""
    grid = [['_' for _ in range(size)] for _ in range(size)]
    treasure_x = random.randint(0, size - 1)
    treasure_y = random.randint(0, size - 1)
    grid[treasure_x][treasure_y] = 'T'  # T for treasure
    return grid, (treasure_x, treasure_y)

def print_grid(grid):
    """Print the grid to the console."""
    for row in grid:
        print(" ".join(row))
    print()

def get_user_input(size):
    """Get valid user input for grid coordinates."""
    while True:
        try:
            x = int(input(f"Enter row (0-{size - 1}): "))
            y = int(input(f"Enter column (0-{size - 1}): "))
            if 0 <= x < size and 0 <= y < size:
                return x, y
            else:
                print("Invalid coordinates. Try again.")
        except ValueError:
            print("Please enter valid integers.")

def main():
    print("Welcome to the Treasure Hunt Game!")
    size = 5  # Size of the grid (5x5)
    grid, treasure_location = create_grid(size)
    attempts = 0
    found = False

    while not found:
        print_grid(grid)
        x, y = get_user_input(size)
        attempts += 1

        if (x, y) == treasure_location:
            print(f"Congratulations! You found the treasure in {attempts} attempts!")
            found = True
        else:
            print("No treasure here. Keep searching!")
            grid[x][y] = 'X'  # Mark the guessed location with 'X'

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
