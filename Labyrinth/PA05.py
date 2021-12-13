from collections import deque

def abstand(s, t, dateiname='labyrinth.dat'):
    with open(dateiname) as f:
        maze = []
        for line in f:
            maze.append([i for i in line.strip('\n')])

    i, j = len(maze), len(maze[0])

    start = (s[0], s[1])
    end = (t[0], t[1])

    queue = deque()
    queue.appendleft((start[0], start[1], 0))
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    visited = [[False] * j for _ in range(i)]

    while len(queue) != 0:
        coord = queue.pop()
        visited[coord[0]][coord[1]] = True
        for dir in directions:
            nr, nc = coord[0] + dir[0], coord[1] + dir[1]
            if(nr < 0 or nr >= i or nc < 0 or nc >= j or maze[nr][nc] == 'U' or visited[nr][nc]):
                continue
            queue.appendleft((nr, nc, coord[2] + 1))
            if nr == end[0] and nc == end[1]:
                return coord[2] + 1
    return -1