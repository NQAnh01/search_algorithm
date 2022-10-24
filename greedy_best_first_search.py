from heuristic import euclid, manhattan

def find_neighbors(matrix, current):
    neighbors = [(current[0] + 1, current[1]),
                 (current[0], current[1] - 1),
                 (current[0] - 1, current[1]),
                 (current[0], current[1] + 1)]
    i = 0
    while i < len(neighbors): #xét nếu nó là 'x' hoặc không thuộc ma trận thì bỏ ra
        if neighbors[i][0] < 0 or neighbors[i][0] >= len(matrix) \
                or neighbors[i][1] < 0 or neighbors[i][1] >= len(matrix[0]) \
                or matrix[neighbors[i][0]][neighbors[i][1]] == 'x':
            neighbors.pop(i)
        else: i += 1
    return neighbors

def G_BFS(matrix, heuristic, start, end):
    #hàng đợi
    queue = []
    queue.append(start)
    #các đỉnh mở
    open = {}
    open[start] = None
    #các đỉnh đã xét
    close = []
    while True:
        if len(queue) == 0:
            return None, None
        current = queue[0]
        for i in range(len(queue)): #lấy phần tử có heuristic nhỏ nhất ra, xét hàng đợi theo hàng đợi ưu tiên
            if heuristic == "euclid":
                if euclid(queue[i], end) < euclid(current, end):
                    current = queue[i]
            else:
                if manhattan(queue[i], end) < manhattan(current, end):
                    current = queue[i]

        if current == end:
            break
        queue.remove(current)
        next_step = find_neighbors(matrix, current) #node kế tiếp

        for next in next_step: #đưa node kế tiếp vào
            if next not in open:
                queue.append(next)
                open[next] = current
                if next == start or next == end:
                    continue
                else:
                    close.append(next)

    return open, close

