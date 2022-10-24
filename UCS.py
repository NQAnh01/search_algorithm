from heuristic import euclid, manhattan
from greedy_best_first_search import find_neighbors

def UCS(matrix, heuristic, start, end):
    queue = []
    queue.append(start)
    open = {}
    open[start] = None
    close = []
    while True:
        current = queue[0]
        for i in range(len(queue)): #lấy phần tử có heuristic nhỏ nhất ra
            if heuristic == "euclid":
                if euclid(queue[i], start) < euclid(current, start):
                    current = queue[i]
            else:
                if manhattan(queue[i], start) < manhattan(current, start):
                    current = queue[i]

        if current == end:
            break
        queue.remove(current)
        next_step = find_neighbors(matrix, current)

        for next in next_step:
            if next not in open:
                queue.append(next)
                open[next] = current
                if next == start or next == end:
                    continue
                else:
                    close.append(next)

    return open, close
