import heapq
import numpy as np

# Define constants for grid representation
EMPTY = 0
OBSTACLE = 1
START = 'S'
GOAL = 'G'
PATH = '*'

def create_grid():
    """Creates the 10x10 grid as described in the assignment."""
    grid = [
        [START, EMPTY, EMPTY, OBSTACLE, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, OBSTACLE, EMPTY, OBSTACLE, EMPTY, EMPTY, EMPTY, OBSTACLE, EMPTY, EMPTY],
        [EMPTY, OBSTACLE, EMPTY, OBSTACLE, EMPTY, EMPTY, EMPTY, OBSTACLE, EMPTY, EMPTY],
        [EMPTY, OBSTACLE, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, OBSTACLE, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, OBSTACLE, OBSTACLE, OBSTACLE, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, OBSTACLE, EMPTY, EMPTY, EMPTY, EMPTY, OBSTACLE, EMPTY, EMPTY, EMPTY],
        [EMPTY, OBSTACLE, OBSTACLE, OBSTACLE, OBSTACLE, EMPTY, OBSTACLE, OBSTACLE, OBSTACLE, EMPTY],
        [EMPTY, OBSTACLE, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, OBSTACLE, EMPTY],
        [EMPTY, OBSTACLE, EMPTY, EMPTY, EMPTY, OBSTACLE, EMPTY, EMPTY, GOAL, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, OBSTACLE, EMPTY, EMPTY, EMPTY, EMPTY],
    ]
    return np.array(grid)

def heuristic(a, b):
    """Calculate Manhattan distance between points a and b."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    """Implements the A* pathfinding algorithm."""
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from, current)

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < grid.shape[0] and 0 <= neighbor[1] < grid.shape[1]:
                if grid[neighbor] == OBSTACLE:
                    continue

                tentative_g_score = g_score[current] + 1

                if tentative_g_score < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None

def reconstruct_path(came_from, current):
    """Reconstructs the path from the came_from dictionary."""
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path

def print_grid(grid, path):
    """Prints the grid with the path visualized."""
    grid_copy = grid.copy()
    for step in path:
        if grid_copy[step] not in (START, GOAL):
            grid_copy[step] = PATH

    for row in grid_copy:
        print(' '.join(map(str, row)))

def main():
    grid = create_grid()
    start = (0, 0)
    goal = (8, 8)

    path = astar(grid, start, goal)

    if path:
        print("Path found:")
        print(path)
        print("\nGrid with path:")
        print_grid(grid, path)
    else:
        print("No path found.")

if __name__ == "__main__":
    main()
