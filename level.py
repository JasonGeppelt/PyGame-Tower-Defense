from enemy import BasicEnemy, AdvancedEnemy

# Pathfinder for enemies. Maybe should go somewhere else, but this file is the only place it is called
def find_path(maze, start, end):
    def is_valid(x, y):
        return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0

    def dfs(x, y, path):
        if (x, y) == end:
            paths.append(path)
            return
        for dx, dy, direction in [(1, 0, 'd'), (0, 1, 'r'), (-1, 0, 'u'), (0, -1, 'l')]:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y):
                maze[x][y] = 1  # Mark as visited
                dfs(new_x, new_y, path + [direction])
                maze[x][y] = 0  # Backtrack

    paths = []
    dfs(start[0], start[1], [])
    return paths[0] if paths else []

level_maps = {
    1: [
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ],
    2: [
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
    ],
    3: [
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
    ],
    # Define maps for more levels here.
}

level_enemy_lists = {
    1: [BasicEnemy, BasicEnemy, BasicEnemy, AdvancedEnemy, BasicEnemy],
    2: [BasicEnemy, AdvancedEnemy, AdvancedEnemy, BasicEnemy, BasicEnemy, AdvancedEnemy, 
        BasicEnemy, AdvancedEnemy, BasicEnemy],
    3: [BasicEnemy, AdvancedEnemy, AdvancedEnemy, BasicEnemy, BasicEnemy, AdvancedEnemy, 
        BasicEnemy, AdvancedEnemy, BasicEnemy]
    # Define lists for other levels here
}

start_end_coords = {
    1: [(0, 1), (9, 9)],
    2: [(0, 1), (9, 8)],
    3: [(0, 1), (9, 8)]
    # Define the start and end coords for other levels here
}

def get_level_count():
    return len(level_maps)

def get_level_map(level) :
    return level_maps[level]

def get_enemy_instructions(level):
    return find_path(level_maps[level], start_end_coords[level][0], start_end_coords[level][1])

def get_enemy_list(level):
    return level_enemy_lists[level]