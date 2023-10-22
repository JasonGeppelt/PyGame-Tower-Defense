from enemy import BasicEnemy, AdvancedEnemy

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
    # Define maps for other levels here
}

level_enemy_instructions = {
    1: find_path(level_maps.get(1, []), (0, 1), (9, 9)),
    2: find_path(level_maps.get(2, []), (0, 1), (9, 8))
    # Define paths for other levels here
}

level_enemy_lists = {
    1: [BasicEnemy, BasicEnemy, BasicEnemy, AdvancedEnemy, BasicEnemy],
    2: [AdvancedEnemy, AdvancedEnemy, BasicEnemy, BasicEnemy, AdvancedEnemy, 
        BasicEnemy, AdvancedEnemy, BasicEnemy]
    # Define lists for other levels here
}

