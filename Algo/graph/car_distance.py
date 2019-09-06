"""

For each '0', find the distance to the closest 'C'

"""

input = [
    ['0', '0', '0', 'C', '#', '#'],
    ['C', '0', '0', '#', '0', '#'],
    ['#', '#', '#', '#', '0', '0'],
    ['C', '0', '0', '0', '0', '#'],
    ['0', '0', '0', '0', '#', '0']
]



def calc_dist(g):
    m, n = len(g), len(g[0])
    dist = [[float('inf')] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if g[i][j] == 'C':
                visited = [[False] * n for _ in range(m)]
                for neighbor in neighbors(i, j, g, visited):
                    dfs(neighbor[0], neighbor[1], g, dist, visited, 1)

    return dist


def dfs(x, y, grid, dist, visited, d):
    if grid[x][y] != '0':
        return

    if dist[x][y] == float('inf') or d < dist[x][y]:
        dist[x][y] = d

    visited[x][y] = True
    for neighbor in neighbors(x, y, grid, visited):
        visited[neighbor[0]][neighbor[1]] = True
        dfs(neighbor[0], neighbor[1], grid, dist, visited, d + 1)
        visited[neighbor[0]][neighbor[1]] = False


def neighbors(x, y, grid, visited):
    m, n = len(grid), len(grid[0])
    nei = []
    if x + 1 < m and grid[x + 1][y] and not visited[x + 1][y]:
        nei.append((x + 1, y))
    if x - 1 >= 0 and grid[x - 1][y] and not visited[x - 1][y]:
        nei.append((x - 1, y))
    if y + 1 < n and grid[x][y + 1] and not visited[x][y + 1]:
        nei.append((x, y + 1))
    if y - 1 >= 0 and grid[x][y - 1] and not visited[x][y - 1]:
        nei.append((x, y-1))
    return nei


print(calc_dist(input))
