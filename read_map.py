
def read_map(file_name):
    f = open(file_name, 'r')
    n = int(f.readlines(1)[0])
    bonus_points = []
    gate = []
    for i in range(n):
        x, y, z = map(int, next(f)[:-1].split(' '))
        bonus_points.append((x, y, z))

    text = f.readlines()
    matrix = [list(i) for i in text]
    for i in range(len(matrix)):
        if matrix[i][len(matrix[i])-1] == '\n':
            matrix[i].remove(matrix[i][len(matrix[i])-1])
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'S':
                start = (i, j)
            if matrix[i][j] == ' ':
                if (i == 0) or (j == 0) or (i == len(matrix)) or (j == len(matrix[0]) - 1):
                    end = (i, j)
            if matrix[i][j] == 'T':
                gate.append((i,j))

    f.close()
    return bonus_points, matrix, start, end, gate

