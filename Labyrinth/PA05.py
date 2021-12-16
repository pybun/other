def abstand(s, t, dateiname = 'labyrinth.dat'):

    if s == t: return 0

    with open(dateiname) as f:
        maze = []
        for line in f:
            maze.append([i for i in line])

    p = []
    for i in range(0, len(maze)):
        for j in range(0, len(maze[i])):
            if maze[i][j] == 'P':
                p.append((i, j))
    p.remove(s)
    q = [s]
    c = 0

    for _ in range(0, len(p)):
        x = []
        while len(q) > 0:
            y = q[0]


            for delta in (-1, 1):
                if (y[0] + delta, y[1]) in p:
                    x.append((y[0] + delta, y[1]))
                    p.remove((y[0] + delta, y[1]))
                if (y[0], y[1] + delta) in p:
                    x.append((y[0], y[1] + delta))
                    p.remove((y[0], y[1] + delta))
            q.pop(0)

        c += 1
        for i in range(0, len(x)):
            if x[i] == t: return c
        if len(x) == 0: return -1
        q = x
