import math

def euclid(start, end):
    return float(math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2))

def manhattan(start, end):
    return float(abs(end[0] - start[0]) + abs(end[1] - start[1]))

def diagonal_distance(start, end):
    return max(math.fabs(end[0] - start[0]), math.fabs(end[1] - start[1]))