import random
from Stages.baseStageClass import *
from Map.generate_map_data import *

# map() creates the map and returns a map object
# Map keeps track of the current level, and the players position within that level
# Each time you call myMap.getUserSelection() the map will appear for the user to select their next step
# It will automatically move the user forward to the step they chose during the previous function call
# It returns the key of the users selected node:
# P = puzzle, b = battle, ? = mystery, T = treasure, B = final battle (also indicates end of level)


class Map(object):
    def __init__(self, screen, seed):
        self.seed = seed
        self.screen = screen
        self.level = 1
        self.node = -1
        self.map = self.generate_map_data()
        self.screen_width = self.screen.screen_height - 400
        self.screen_height = self.screen.screen_width + 10
        self.quitButton = StageButton("Quit", "", self.screen_width + 180, 10)
        self.bgImage = pygame.transform.scale(pygame.image.load('Map/media/trees.jpg').convert(), (self.screen_height,
                                                                                                   self.screen_width))
        self.heal = pygame.transform.scale(pygame.image.load('Map/media/healthRoom.png').convert_alpha(), (35, 35))
        self.treasureImage = pygame.transform.scale(pygame.image.load('Map/media/treasure.png').convert_alpha(), (35, 35))
        self.mysteryImage = pygame.transform.scale(pygame.image.load('Map/media/Mystery.png').convert_alpha(), (35, 35))
        self.bossBattleImage = pygame.transform.scale(pygame.image.load('Map/media/BossSkull.png').convert_alpha(), (35, 35))
        self.battleImage = pygame.transform.scale(pygame.image.load('Map/media/NormalBattle.png').convert_alpha(), (35, 35))
        self.puzzleImage = pygame.transform.scale(pygame.image.load('Map/media/Puzzle.png').convert_alpha(), (35, 35))

        self.currentNode = ""
        self.mysteryUpdate=""
    # generates map data --> how many nodes, what room they represent, how they're connected
    # using functions in generate_map_data file
    def generate_map_data(self):
        random.seed(str(self.level) + str(self.seed))
        list_of_nodes = generate_nodes_and_keys(10)
        connected_list = generate_node_connections(list_of_nodes)
        return connected_list

    # at the end of each level, the node number is reset and a new map is generated
    def check_for_end_of_map(self, selected_node_key):
        if selected_node_key == "B":
            self.node = -1
            self.level += 1
            self.map = self.generate_map_data()

    # this function draws the current map, with the most recently selected node and data
    def draw_map(self):
        next_nodes = []
        next_nodes_dict = {}
        blue = (0, 0, 255)
        black = (0, 0, 0)
        grey = (86, 80, 81)
        white = (255, 255, 255)
        node_dict = {}
        node_index = 0
        circle_radius = 24
        num_levels = 10
        node_height = int(round(self.screen_height / num_levels))

        # for each level, and for each node, draw a line to its following nodes
        # line colour and width depend on the users current position
        for level_index in range(num_levels):
            level_length = len(self.map[level_index])
            for i in range(level_length):
                line_width = 1
                line_color = grey
                if self.map[level_index][i][0] == self.node+1:
                    line_width = 3
                    line_color = black
                from_node_x = self.screen_width / len(self.map[level_index])
                number_of_to_nodes = len(self.map[level_index][i][2])
                for j in range(number_of_to_nodes):
                    to_node_x = self.screen_width / len(self.map[level_index + 1])
                    for to_node_index in range(len(self.map[level_index + 1])):
                        if self.map[level_index + 1][to_node_index][0] == self.map[level_index][i][2][j]:
                            q = to_node_index
                            pygame.draw.lines(self.screen.display, line_color, False,
                                              [(int(from_node_x * (i + 1) - (from_node_x / 2))+200,
                                                int(self.screen_height - node_height * (
                                                        level_index + 1)) - 1),
                                               (int(to_node_x * (q + 1) - (to_node_x / 2))+200,
                                                int(self.screen_height - node_height * (
                                                        level_index + 2) +
                                                    node_height - circle_radius) - 5)], line_width)

        # for each node in map, draw a circle, and draw an image inside it
        # colour and image depend on the users current position in the map
        for level_index in range(num_levels):
            node_x = int(round(self.screen_width / len(self.map[level_index])))
            current_level_nodes = []
            for i in range(len(self.map[level_index])):
                node_key = self.map[level_index][i][1]
                circle_x = int(node_x * (i + 1) - (node_x / 2))+200
                circle_y = int(self.screen_height - node_height * (level_index + 1) + 20)

                if self.node == -1:
                    next_nodes = []
                    for node in self.map[0]:
                        next_nodes.append(node[0])
                pygame.draw.circle(self.screen.display, grey, (circle_x, circle_y), 20)
                if node_index == self.node:
                    node_key = "YOU"
                    circle_colour = black
                    for node in range(len(self.map[level_index])):
                        current_level_nodes.append(self.map[level_index][node][0])
                    next_nodes = self.map[level_index][i][2]
                elif node_index < self.node or node_index in current_level_nodes:
                    circle_colour = black
                    pygame.draw.circle(self.screen.display, circle_colour, (circle_x, circle_y), circle_radius, )
                elif (node_index + 1) in next_nodes:
                    next_nodes_dict[node_index] = node_key
                    circle_colour = blue
                else:
                    circle_colour = grey

                circle = pygame.draw.circle(self.screen.display, circle_colour, (circle_x, circle_y),
                                            circle_radius, )
                node_dict[node_index] = circle
                node_index += 1

                # add the relevant image to represent the node
                if node_key == "YOU":
                    font = pygame.font.SysFont('media/Chapaza.ttf', 23)
                    text = font.render("%s" % node_key, True, white)
                    self.screen.display.blit(text, (int(node_x * (i + 1) - (node_x / 2))-15+200,
                                                    int(self.screen_height - node_height * (
                                                            level_index + 1) + 20) -8))
                elif node_key == "T":
                    self.screen.display.blit(self.treasureImage, (int(node_x * (i + 1) - (node_x / 2)) - 18+200,
                                                                  int(self.screen_height - node_height * (
                                                                          level_index + 1) + 20) - 18))
                elif node_key == "H":
                    self.screen.display.blit(self.heal, (int(node_x * (i + 1) - (node_x / 2)) - 18+200,
                                                                  int(self.screen_height - node_height * (
                                                                          level_index + 1) + 20) - 18))
                elif node_key == "?":
                    self.screen.display.blit(self.mysteryImage, (int(node_x * (i + 1) - (node_x / 2)) - 18+200,
                                                                 int(self.screen_height - node_height * (
                                                                         level_index + 1) + 20) - 18))
                elif node_key == "b":
                    self.screen.display.blit(self.battleImage, (int(node_x * (i + 1) - (node_x / 2)) - 18+200,
                                                                int(self.screen_height - node_height * (
                                                                        level_index + 1) + 20) - 18))
                elif node_key == "B":
                    self.screen.display.blit(self.bossBattleImage, (int(node_x * (i + 1) - (node_x / 2)) - 18+200,
                                                                    int(self.screen_height - node_height * (
                                                                            level_index + 1) + 20) - 18))
                else:
                    self.screen.display.blit(self.puzzleImage, (int(node_x * (i + 1) - (node_x / 2)) - 18+200,
                                                                    int(self.screen_height - node_height * (
                                                                            level_index + 1) + 20) - 18))
        return node_dict, next_nodes, next_nodes_dict

    # wait for the user to select the node they want to move to next, or to exit
    def get_next_node(self, node_dict, next_nodes, next_nodes_dict):
        while True:
            pygame.display.update()
            length_next_nodes = len(next_nodes)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if (self.quitButton.xLocation + self.quitButton.width) > pos[0] > self.quitButton.xLocation and (
                            self.quitButton.yLocation + self.quitButton.height) > pos[1] > self.quitButton.yLocation:
                        node_key = "m"
                        return node_key
                    for item in range(length_next_nodes):
                        rectangle = node_dict[next_nodes[item] - 1]
                        click = rectangle.collidepoint(pos)
                        if click == 1:
                            self.node = next_nodes[item] - 1
                            node_key = next_nodes_dict[self.node]
                            pygame.display.update()
                            return node_key

    # display the map background image, current level, quit button etc
    def printBackground(self):
        pygame.font.init()
        brown = (53, 36, 26)
        grey = (51, 61, 51)
        black = (0, 0, 0)
        myfont = pygame.font.SysFont('media/Chapaza.ttf', 37)
        self.screen.display.blit(self.screen.bgImage, (275, 0))
        self.screen.displayButton(self.quitButton)
        display_level = myfont.render("Level %i" % self.level, True, black)
        my_font = pygame.font.SysFont('media/Chapaza.ttf', 27)
        display_instructions1 = my_font.render("Hint: Choose your", True, black)
        display_instructions2 = my_font.render("     next step by", True, black)
        display_instructions3 = my_font.render("    clicking on a", True, black)
        display_instructions4 = my_font.render("     blue circle!", True, black)
        hint_rect = Rect(100, 588, 170, 100)
        level_rect = Rect(129, 119, 100, 40)
        pygame.draw.rect(self.screen.display, brown, hint_rect)
        pygame.draw.rect(self.screen.display, grey, level_rect)
        self.screen.display.blit(display_level, (130, 120))
        self.screen.display.blit(display_instructions1, (102, 590))
        self.screen.display.blit(display_instructions2, (102, 610))
        self.screen.display.blit(display_instructions3, (102, 630))
        self.screen.display.blit(display_instructions4, (102, 650))
        pygame.display.update()

    # main function called by external main file
    # displays all data and returns the users selection
    def mainloop(self):
        self.printBackground()
        node_dict, next_nodes, next_nodes_dict = self.draw_map()
        selected_node_key = self.get_next_node(node_dict, next_nodes, next_nodes_dict)
        self.check_for_end_of_map(selected_node_key)
        return selected_node_key



