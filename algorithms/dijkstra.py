# dijkstra_grid.py - SUPER SIMPLE VERSION (Windows Compatible)
print("=== WEEK 1: STARTING SIMPLE ===")

# Step 1: Make a tiny 3x3 grid
grid = [
    [0, 2, 9],
    [5, 1, 3],
    [2, 7, 0]
]

print("--- Our 3x3 Grid ---")
for row in grid:
    print(row)

# Step 2: Let's just FIND the shortest path manually first
print("\n>>> Let's find path from TOP-LEFT (0,0) to BOTTOM-RIGHT (2,2)")

# Possible paths:
path1 = [(0,0), (0,1), (0,2), (1,2), (2,2)]  # Right, Right, Down, Down
path2 = [(0,0), (1,0), (2,0), (2,1), (2,2)]  # Down, Down, Right, Right
path3 = [(0,0), (0,1), (1,1), (1,2), (2,2)]  # Right, Down, Right, Down

def calculate_path_cost(path, grid):
    """Calculate total cost of a path"""
    total = 0
    for i in range(len(path)-1):
        r1, c1 = path[i]
        r2, c2 = path[i+1]
        total += grid[r2][c2]  # Cost to ENTER the next cell
    return total

print("\n>>> Calculating path costs:")
print(f"Path 1 {path1}: Cost = {calculate_path_cost(path1, grid)}")
print(f"Path 2 {path2}: Cost = {calculate_path_cost(path2, grid)}")
print(f"Path 3 {path3}: Cost = {calculate_path_cost(path3, grid)}")

# Step 3: Now let's code a SIMPLE Dijkstra
print("\n>>> Now let's code Dijkstra to find it automatically...")

def simple_dijkstra(grid, start, end):
    """Super simple Dijkstra for 3x3 grid"""
    rows, cols = len(grid), len(grid[0])
    
    # Distance from start to each cell
    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[start[0]][start[1]] = 0
    
    # Directions: right, down, left, up
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    
    # We'll do 10 iterations max (simple approach)
    for i in range(10):
        # Print current distances
        print(f"\nIteration {i}: Current distances")
        for r in range(rows):
            print([f"{dist[r][c]:.1f}" if dist[r][c] != float('inf') else "inf" 
                   for c in range(cols)])
        
        # Update distances
        for r in range(rows):
            for c in range(cols):
                if dist[r][c] != float('inf'):
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            new_dist = dist[r][c] + grid[nr][nc]
                            if new_dist < dist[nr][nc]:
                                dist[nr][nc] = new_dist
    
    return dist[end[0]][end[1]]

# Run it!
start = (0, 0)
end = (2, 2)
shortest = simple_dijkstra(grid, start, end)

print(f"\n>>> Dijkstra found shortest distance: {shortest}")
print("(Should match the smallest cost from our manual calculation!)")
