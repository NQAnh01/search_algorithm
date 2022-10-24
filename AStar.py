import heapq
from heuristic import *

# Kiểm tra một điểm có nằm bên trong ma trận và là điểm có thể đi được (không phải tường)
def IsInside(map, point):
    return (point[0] < len(map) 
        and point[0] >= 0 
        and point[1] < len(map[0]) 
        and point[1] >= 0 
        and map[point[0]][point[1]] != 'x')

def AStar( map, start, end, heuristic):
    # Danh sách đỉnh đang mở
    open = []
    # Danh sách đỉnh có xét
    close = []
    # Danh sách đỉnh và chi phí hiện tại để đến đó
    cost = {}
    # Đường đi
    result = {}
    # Vị trí có thể đi mỗi ô
    steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Xét điểm bắt đầu
    heapq.heappush(open, (0, start))
    result[start] = None
    cost[start] = 0
    while len(open) != 0:
        current = heapq.heappop(open)[1]

        if (current == end):
            break
        
        # Xét 4 hướng đi được để thêm điểm vào open
        for step in steps:
            next = (current[0] + step[0], current[1] + step[1])

            if not IsInside(map, next):
                continue
            
            #Tính chi phí mới
            if heuristic == "euclid":
                new_cost = float(manhattan(next, start) + euclid(next, end))
            else:
                new_cost = float(manhattan(next, start) + manhattan(next, end))

            # Thêm điểm mới vào đường đi nếu chưa đi qua hoặc đường đi hiện tại tốt hơn đường đi trước đó
            if (next not in cost) or (cost[next] > new_cost):
                heapq.heappush(open, (cost, next))
                result[next] = current
                cost[next] = new_cost
                
                # Vẽ những vị trí đang xét
                if next != start and next != end:
                    close.append(next)

    return result, close


