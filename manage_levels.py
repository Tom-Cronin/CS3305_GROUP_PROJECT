from create_map_list import generate_map_list
from draw_map import draw_level_map
import time
import pygame as pygame

pygame.init()
screen_height = 640
screen_width = 800
screen = pygame.display.set_mode((screen_width, screen_height))
white = (255, 255, 255)


def draw_map(list_of_nodes, node):
    current_node = draw_level_map(list_of_nodes, screen_width, screen_height, screen, node)
    return current_node


def run_game():
    current_level = 1000
    current_node = 0
    screen.fill(white)
    pygame.display.update()
    list_of_nodes = generate_map_list(current_level)
    length_of_level = len(list_of_nodes) - 1
    for i in range(length_of_level):
        current_node = draw_map(list_of_nodes, current_node)


run_game()
