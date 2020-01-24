import pygame as pygame
from create_map_list import generate_map_list
import sys, time

pygame.init()
screen_height = 640
screen_width = 800
screen = pygame.display.set_mode((screen_width, screen_height))


def draw_level_map(list_of_nodes):
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    darkBlue = (0, 0, 128)
    white = (255, 255, 255)
    black = (0, 0, 0)
    pink = (255, 200, 200)
    circle_radius = 20
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 10)
    while True:
        num_levels = len(list_of_nodes)
        node_height = int(round(screen_height / num_levels))

        for level_index in range(num_levels):
            node_x = int(round(screen_width / len(list_of_nodes[level_index])))

            for i in range(len(list_of_nodes[level_index])):
                node_key = list_of_nodes[level_index][i][1]
                pygame.draw.circle(screen, red, (
                    int(node_x * (i + 1) - (node_x / 2)),
                    int(screen_height - node_height * (level_index + 1) + 20)),
                                   circle_radius, 1)
                text = myfont.render("%s" % node_key, True, red)
                screen.blit(text, (int(node_x * (i + 1) - (node_x / 2)) - 4,
                                   int(screen_height - node_height * (level_index + 1) + 20) - 6))
        for level_index in range(num_levels):
            level_length = len(list_of_nodes[level_index])
            for i in range(level_length):
                from_node_x = screen_width / len(list_of_nodes[level_index])
                number_of_to_nodes = len(list_of_nodes[level_index][i][2])
                for j in range(number_of_to_nodes):
                    to_node_x = screen_width / len(list_of_nodes[level_index + 1])
                    for to_node_index in range(len(list_of_nodes[level_index + 1])):
                        if list_of_nodes[level_index + 1][to_node_index][0] == list_of_nodes[level_index][i][2][j]:
                            q = to_node_index
                            pygame.draw.lines(screen, red, True, [(int(from_node_x * (i + 1) - (from_node_x / 2)),
                                                                   int(screen_height - node_height * (
                                                                           level_index + 1))),
                                                                  (int(to_node_x * (q + 1) - (to_node_x / 2)),
                                                                   int(screen_height - node_height * (level_index + 2) +
                                                                       node_height - circle_radius))], 1)

        pygame.display.update()
        return


def draw_map(level):
    white = (255, 255, 255)
    screen.fill(white)
    pygame.display.update()
    list_of_nodes = generate_map_list(level)
    draw_level_map(list_of_nodes)


for level in range(10):
    draw_map(level)
    time.sleep(2)
