# Assignment-4-Path-Planning-with-Obstacle-Avoidance-Simulation-

Path Planning with Obstacle Avoidance

Objective

The purpose of this project is to demonstrates the A* search algorithm that can be used to find the shortest path in a 2D grid with obstacles. The following is the grid representation. 

Grid Representation

Start (S): (0, 0)

Goal (G): (8, 8)

Obstacle (1): Impassable cells

Empty (0): Traversable cells

Path (*): Final calculated path

Implementation Highlights

Algorithm: A* with Manhattan distance heuristic.

Inputs: A 10x10 grid, start, and goal positions.

Output: A list of path coordinates and a visualized grid with the path.

Movement: Restricted to up, down, left, and right with no diagonals.

Execution

You can run the Python script to display the path found as a list of coordinates as shown below. We have visualized the output as grid with the path marked with *.

Output

For the provided grid, the path found is

[(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8)]

The following 2d shows drid with path marked with * copied from the output we get after running the script attached. 

S * * * * * * * * 0

0 1 0 1 0 0 0 1 * 0

0 1 0 1 0 0 0 1 * 0

0 1 0 0 0 0 0 1 * 0

0 0 0 1 1 1 0 0 * 0

0 1 0 0 0 0 1 0 * 0

0 1 1 1 1 0 1 1 * 0

0 1 0 0 0 0 0 0 * 0

0 1 0 0 0 1 0 0 G 0

0 0 0 0 0 1 0 0 0 0

