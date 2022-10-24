from greedy_best_first_search import find_neighbors

def DFS(matrix, start, end):
    stack = []
    stack.append(start)
    open = {}
    open[start] = None
    close = []
    while True:
        current = stack[-1]
        if current == end:
            break
        stack.remove(current)
        next_step = find_neighbors(matrix, current)

        for next in next_step:
            if next not in open:
                stack.append(next)
                open[next] = current
                if next == start or next == end:
                    continue
                else:
                    close.append(next)

    return open, close
