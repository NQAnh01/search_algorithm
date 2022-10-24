import pygame
from pygame.locals import *
import sys

from draw_matrix import init_map
from read_map import read_map
from greedy_best_first_search import G_BFS
from BFS import BFS
from AStar import AStar
from algo_teleportation import find_way
import time


def write_map(input_file, path):
    output_file = "out" + input_file[2:]
    output = open(output_file, "w")
    if path == None:
        output.write('No')
    else:
        output.write(len(path).__str__())
    output.close()

def main():

    input_file = 'input/level_1/maze_map6.txt'
    bonus, matrix, start, end, gate = read_map(input_file)
    width = len(matrix[0]) * 30
    height = len(matrix) * 30
    screen = init_map(width, height)

    draw_matrix(matrix, bonus, screen)
    pygame.display.update()

    open, close = G_BFS(matrix,"euclid", start, end)
    # open, close = UCS(matrix,"manhattan", start, end)
    # open, close = BFS(matrix,start,end)
    # open, close = DFS(matrix, start, end)
    # open, close = AStar(matrix, start, end, "euclid")

    # gọi hàm teleport
    # open, close = find_way(matrix,start,end,"euclid",gate)

    # if open == None:
    #     print("khong co duong di")
    #     write_map(input_file, open)
    #     return
    #
    #
    draw_path(open, close, start, end, screen)
    pygame.display.update()
    # write_map(input_file, open)

    # vẽ teleport cho map có gate
    # draw_path_tele(open,close,start,end,gate,screen)
    # pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

# vẽ ô và đường biên
def fill_cell (x1, y1, x2, y2, color, screen):
    pygame.draw.rect(screen, color, (x1, y1, x2, y2))
    pygame.draw.rect(screen, (0, 0, 0), (x1, y1, x2, y2), 1) #(0, 0, 0): đen

def draw_matrix(matrix, bonus, screen):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'x':
                fill_cell(j*30, i*30, 30, 30, (54, 54, 54), screen) #gray
            elif matrix[i][j] == 'S':
                fill_cell(j*30, i*30, 30, 30, (0, 255, 255), screen) #yellow
            elif matrix[i][j] == 'T':
                fill_cell(j * 30, i * 30, 30, 30, (148,0,211), screen)  # darkviolet
            elif matrix[i][j] == ' ':
                if (i == 0) or (j == 0) or (i == len(matrix)) or (j == len(matrix[0]) - 1):
                    fill_cell(j * 30, i * 30, 30, 30, (255, 0, 0), screen)
                else: fill_cell(j*30, i*30, 30, 30, (255,255,255), screen) #white

    if len(bonus) != 0:
        for i in bonus:
            fill_cell(i[1] * 30, i[0] * 30, 30, 30, (255, 255, 0), screen)

def draw_path(open, close, start, end, screen):
    for cell in close:
        fill_cell(cell[1]*30, cell[0]*30, 30, 30, (192,192,192), screen)
        pygame.display.update()
        pygame.time.wait(15)

    current = end
    while True:
        current = open[current]
        if current == start:
            break
        fill_cell(current[1]*30, current[0]*30, 30, 30, (0, 255, 0), screen)
        pygame.display.update()
        pygame.time.wait(30)

def draw_path_tele(open, close, start, end, gate, screen):
    for i in close:
        if i==start or i==end or i ==gate[0] or i ==gate[1]:
            continue
        fill_cell(i[1]*30, i[0]*30, 30, 30, ((192,192,192)), screen)
        pygame.display.update()
        pygame.time.wait(15)
    for i in open:
        if i==start or i==end or i ==gate[0] or i ==gate[1]:
            continue
        fill_cell(i[1]*30, i[0]*30, 30, 30, (0, 255, 0), screen)
        pygame.display.update()
        pygame.time.wait(15)

if __name__ == "__main__":
    # main(sys.argv[1:])
    main()
