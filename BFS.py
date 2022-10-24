from greedy_best_first_search import find_neighbors

def BFS(matrix, start, end):
    queue = []
    queue.append(start)
    open = {}
    open[start] = None
    close = []
    while True:
        current = queue[0]
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
