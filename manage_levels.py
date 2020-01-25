from create_map_list import generate_map_list
from draw_map import draw_level_map
import time
import pygame as pygame

pygame.init()
screen_height = 640
screen_width = 800
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
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


#run_game()

#
class map(object):
    def __init__(self, seed, level):
        self.seed = seed
        self.originalSeed = seed
        self.level = level

        self.currentNode = 0

    def draw_map(self, list_of_nodes, node):
        current_node = draw_level_map(list_of_nodes, screen_width, screen_height, screen, node)
        return current_node
    def createScreen(self):
        pygame.init()
        screen_height = 640
        screen_width = 800
        screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
        white = (255, 255, 255)
        screen.fill(white)
        pygame.display.update()
        list_of_nodes = generate_map_list(self.level)
        length_of_level = len(list_of_nodes) - 1
        for i in range(length_of_level):
            self.currentNode = self.draw_map(list_of_nodes, self.currentNode)

    def returnSeedNew(self):
        return self.seed

    def returnSeed(self):
        return self.originalSeed
myMap = map(10, 10)
myMap.createScreen()