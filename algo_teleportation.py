from greedy_best_first_search import G_BFS

def get_path(start, end, open):
    if open == None:
        return None
    path = []
    current = end
    while current!=start:
        current = open[current]
        path.append(current)
    return path

def find_way_to_teleport(matrix,start,end, heuristic,gate):
    s_to_g0, temp1 = G_BFS(matrix, heuristic,start,gate[0])
    g1_to_g, temp2 = G_BFS(matrix, heuristic,gate[1],end)
    s_to_g1, temp3 = G_BFS(matrix, heuristic,start,gate[1])
    g0_to_g, temp4 = G_BFS(matrix, heuristic,gate[0],end)
    len1 = len2 = len3 = len4 = 0
    if s_to_g0 != None:
        len1 = len(get_path(start, gate[0], s_to_g0))
    if g1_to_g != None:
        len2 = len(get_path(gate[1], end, g1_to_g))
    if s_to_g1 != None:
        len3 = len(get_path(start, gate[1], s_to_g1))
    if g0_to_g != None:
        len4 = len(get_path(gate[0], end, g0_to_g))

    if s_to_g0 == None or g1_to_g==None:
        if s_to_g1 == None or g0_to_g == None:
            print("ủa alo")
            return None, None
        else:
            path1, close1 = get_path(start, gate[1], s_to_g1), temp2
            path2, clode2 = get_path(gate[0], end, g0_to_g), temp4

    elif s_to_g1 == None or g0_to_g == None:
        path1, close1 = get_path(start, gate[0], s_to_g0), temp1
        path2, clode2 = get_path(gate[1], end, g1_to_g), temp2

    elif len1+len2 < len3+len4:
        path1, close1 = get_path(start, gate[0], s_to_g0), temp1
        path2, clode2 = get_path(gate[1], end, g1_to_g), temp2
    else:
        path1, close1 = get_path(start, gate[1], s_to_g1), temp2
        path2, clode2 = get_path(gate[0], end, g0_to_g), temp4

    path2 = path2 + path1
    close1 = close1 + clode2

    return path2, close1

def find_way(matrix, start, end, heuristic, gate):
    start_end, temp_1 = G_BFS(matrix,heuristic,start,end)
    start_end = get_path(start,end,start_end)
    start_tele_end, temp_2 = find_way_to_teleport(matrix,start,end, heuristic,gate)

    temp = []
    if temp_1 != None:
        temp = temp + temp_1
    if temp_2 != None:
        temp = temp + temp_2

    if start_end == None:
        if start_tele_end == None:
            return None, None
        else: return start_tele_end, temp # temp_2
    elif start_tele_end == None:
        return start_end, temp #temp_1
    elif len(start_end) < len(start_tele_end):
        return start_end, temp #temp_1
    else: return start_tele_end, temp #temp_2



