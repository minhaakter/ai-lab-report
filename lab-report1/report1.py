import random

def generate_grid(n):
    grid = [['.' for _ in range(n)] for _ in range(n)]
    source = (random.randint(0, n - 1), random.randint(0, n - 1))
    goal = (random.randint(0, n - 1), random.randint(0, n - 1))
    
    while goal == source:
        goal = (random.randint(0, n - 1), random.randint(0, n - 1))
    
    grid[source[0]][source[1]] = 'S'
    grid[goal[0]][goal[1]] = 'G'
    return grid, source, goal

def print_grid(grid):
    for row in grid:
        print(" ".join(row))

def dfs(grid, source, goal, n):
    stack = [source]
    visited = set()
    parent = {}
    topological_order = []
    
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        topological_order.append(node)
        if node == goal:
            break
        
        x, y = node
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                stack.append((nx, ny))
                parent[(nx, ny)] = node
    
    path = []
    current = goal
    while current in parent:
        path.append(current)
        current = parent[current]
    path.append(source)
    path.reverse()
    
    return path if goal in visited else [], topological_order

def main():
    n = int(input("Enter grid size (4-7): "))
    if n < 4 or n > 7:
        print("Invalid size! Please enter a number between 4 and 7.")
        return
    
    grid, source, goal = generate_grid(n)
    print("\nGenerated Grid:")
    print_grid(grid)
    
    path, topological_order = dfs(grid, source, goal, n)
    
    if path:
        print("\nDFS Path:", path)
    else:
        print("\nNo path found from source to goal.")
    
    print("Topological Order:", topological_order)

if __name__ == "__main__":
    main()
