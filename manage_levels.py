from create_map_list import generate_map_list
from draw_map import draw_level_map
import time
import pygame as pygame


#variables which should be pre set before using the map
pygame.init()
screen_height = 640
screen_width = 800
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
white = (255, 255, 255)
screen.fill(white)
pygame.display.update()


class map(object):
    def __init__(self, seed, level, node):
        self.seed = seed
        self.level = level
        self.node = node
        self.selectedNode = None
        self.selected_node_key = None

    def createScreen(self):
        list_of_nodes = generate_map_list(self.level, self.seed)
        self.selectedNode, self.selected_node_key = draw_level_map(list_of_nodes, screen_width, screen_height, screen,
                                                                   self.node)

    def getSelectedNode(self):
        return self.selectedNode, self.selected_node_key


game_seed = "xy2z"
current_level = 1
current_node = 3

myMap = map(game_seed, current_level, current_node)  # (game_seed, current_level, current_node_in_level)

myMap.createScreen()

new_node, new_node_key = myMap.getSelectedNode()

print("""\n\nGame seed: %s\nUser is currently at node %s on level %s.\nFrom here the user has selected to move to node %s which is: %s (see key).""" %(game_seed, current_node, current_level, new_node, new_node_key))