import random
from Stages.baseStageClass import *


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
        self.map = self.generate_map_list()
        self.screen_width = self.screen.screen_height-400
        self.screen_height = self.screen.screen_width +10
        self.quitButton = StageButton("Quit", "", self.screen_width + 180, 10)
        self.bgImage = pygame.transform.scale(pygame.image.load('Map/media/trees.jpg').convert(), (self.screen_height,
                                                                                                   self.screen_width))
        self.treasureImage = pygame.transform.scale(pygame.image.load('Map/media/Treasure.png').convert_alpha(), (35, 35))
        self.mysteryImage = pygame.transform.scale(pygame.image.load('Map/media/Mystery.png').convert_alpha(), (35, 35))
        self.bossBattleImage = pygame.transform.scale(pygame.image.load('Map/media/BossSkull.png').convert_alpha(), (35, 35))
        self.battleImage = pygame.transform.scale(pygame.image.load('Map/media/NormalBattle.png').convert_alpha(), (35, 35))
        self.puzzleImage = pygame.transform.scale(pygame.image.load('Map/media/Puzzle.png').convert_alpha(), (35, 35))

    def generate_map_list(self):
        random.seed(str(self.level) + str(self.seed))
        number_of_levels = 10
        list_of_nodes = self.generate_nodes_and_keys(number_of_levels)
        connected_list = self.generate_node_connections(list_of_nodes)
        return connected_list

    def check_for_end_of_map(self, selected_node_key):
        if selected_node_key == "B":
            self.node = -1
            self.level += 1
            self.map = self.generate_map_list()

    def generate_nodes_and_keys(self, number_of_levels):
        nodes_per_level = 0
        node_index = 1
        list_of_levels = []
        for level_index in range(number_of_levels):
            list_of_levels.append([])
            if level_index == number_of_levels - 1:
                nodes_per_level = 1
            elif level_index == 0:
                nodes_per_level = random.randint(1, 3)
            elif level_index == 0:
                nodes_per_level = random.randint(1, 4)
            else:
                nodes_per_level = random.randint(1, nodes_per_level + 1)
                while nodes_per_level > 4:
                    nodes_per_level = random.randint(1, nodes_per_level)
            for node in range(nodes_per_level):
                if level_index == 0:
                    node_key = "b"
                elif level_index == number_of_levels - 1:
                    node_key = "B"
                elif level_index == number_of_levels - 2:
                    node_key = "T"
                else:
                    rand = random.randint(1, 7)
                    if rand == 1:
                        node_key = "T"
                    elif rand == 2 or rand == 3:
                        node_key = "P"
                    elif rand == 4:
                        node_key = "?"
                    else:
                        node_key = "b"
                list_of_levels[level_index].append([node_index, node_key, []])
                node_index += 1
        return list_of_levels

    def generate_node_connections(self, list_of_levels):
        for level in range(len(list_of_levels) - 1):
            next_level = level + 1
            len_level = len(list_of_levels[level])
            len_next_level = len(list_of_levels[next_level])
            if len_next_level > len_level:
                average = len_next_level / len_level
                if average.is_integer():
                    from_nodes = 0
                    count = 0
                    while from_nodes < len_level:
                        for i in range(int(average)):
                            list_of_levels[level][from_nodes][2].append(list_of_levels[next_level][i + count][0])
                        from_nodes += 1
                        count += int(average)
                else:
                    for i in range(len(list_of_levels[next_level])):
                        rand_node = random.randint(0, len_level - 1)
                        list_of_levels[level][rand_node][2].append(list_of_levels[next_level][i][0])
                    for i in range(len(list_of_levels[level])):
                        if not list_of_levels[level][i][2]:
                            rand_node = random.randint(0, len_next_level - 1)
                            list_of_levels[level][i][2].append(list_of_levels[next_level][rand_node][0])

            elif len_next_level < len_level:
                average = len_level / len_next_level
                if average.is_integer():
                    count = 1
                    from_nodes = 0
                    for i in range(len_next_level):
                        for j in range(int(average) * (count - 1), int(average) * (count), 1):
                            list_of_levels[level][j][2].append(list_of_levels[next_level][i][0])
                        count += 1
                else:
                    for i in range(len(list_of_levels[next_level])):
                        rand_node = random.randint(0, len_level - 1)
                        list_of_levels[level][rand_node][2].append(list_of_levels[next_level][i][0])
                    for i in range(len(list_of_levels[level])):
                        if not list_of_levels[level][i][2]:
                            rand_node = random.randint(0, len_next_level - 1)
                            list_of_levels[level][i][2].append(list_of_levels[next_level][rand_node][0])
            elif len_next_level == len_level:
                average = len_level / len_next_level
                if average.is_integer():
                    from_nodes = 0
                    while from_nodes < len_next_level:
                        list_of_levels[level][from_nodes][2].append(list_of_levels[next_level][from_nodes][0])
                        from_nodes += 1
        return list_of_levels

    def draw_map(self):
        next_nodes = []
        next_nodes_dict = {}
        red = (255, 0, 0)
        blue = (0, 0, 255)
        black = (0, 0, 0)
        bronze = (205, 127, 50)
        grey = (86, 80, 81)
        white = (255, 255, 255)
        node_dict = {}
        node_index = 0
        circle_radius = 24

        myfont = pygame.font.SysFont('media/Chapaza.ttf', 17)
        while True:
            num_levels = len(self.map)
            node_height = int(round(self.screen_height / num_levels))

            for level_index in range(num_levels):
                level_length = len(self.map[level_index])
                for i in range(level_length):
                    line_width = 1
                    line_color = grey
                    if self.map[level_index][i][0] == self.node+1:
                        line_width = 3
                        line_color = black
                        #print(self.map[level_index][i][0], self.node)
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
                        circle_width = circle_radius
                        circle_colour = black
                        for node in range(len(self.map[level_index])):
                            current_level_nodes.append(self.map[level_index][node][0])
                        next_nodes = self.map[level_index][i][2]
                    elif node_index < self.node or node_index in current_level_nodes:
                        circle_colour = black
                        circle_width = circle_radius
                        pygame.draw.circle(self.screen.display, circle_colour, (circle_x, circle_y), circle_radius, )
                        circle_width = 1
                    elif (node_index + 1) in next_nodes:
                        next_nodes_dict[node_index] = node_key
                        circle_width = circle_radius
                        circle_colour = blue
                    else:
                        circle_width = 1
                        circle_colour = grey

                    circle = pygame.draw.circle(self.screen.display, circle_colour, (circle_x, circle_y),
                                                circle_radius, )
                    node_dict[node_index] = circle
                    node_index += 1
                    text = myfont.render("%s" % node_key, True, black)
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

    def get_next_node(self):
        node_dict, next_nodes, next_nodes_dict = self.draw_map()
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

    def get_user_selection(self):
        selected_node_key = self.get_next_node()
        self.check_for_end_of_map(selected_node_key)
        return selected_node_key

    def backgroundLayer(self):
        pygame.font.init()
        red = (53,36,26)
        grey = (51, 61, 51)
        black = (0, 0, 0)
        myfont = pygame.font.SysFont('media/Chapaza.ttf', 37)
        self.screen.display.blit(self.screen.bgImage, (275, 0))
        self.screen.displayButton(self.quitButton)
        display_level = myfont.render("Level: %i" % self.level, True, black)
        myfont = pygame.font.SysFont('media/Chapaza.ttf', 27)
        display_instructions1 = myfont.render("Hint: Choose your", True, black)
        display_instructions2 = myfont.render("     next step by", True, black)
        display_instructions3 = myfont.render("    clicking on a", True, black)
        display_instructions4 = myfont.render("     blue circle!", True, black)
        hintRect = Rect(100, 588, 170, 100)
        levelRect = Rect(129, 119, 100, 40)
        pygame.draw.rect(self.screen.display, red, hintRect)
        pygame.draw.rect(self.screen.display, grey, levelRect)
        self.screen.display.blit(display_level, (130, 120))
        self.screen.display.blit(display_instructions1, (102, 590))
        self.screen.display.blit(display_instructions2, (102, 610))
        self.screen.display.blit(display_instructions3, (102, 630))
        self.screen.display.blit(display_instructions4, (102, 650))
        pygame.display.update()

    def mainLoop(self):
        self.backgroundLayer()
        current_room = "b"
        while current_room != "B":
            current_room = self.get_user_selection()
            return current_room, 0
        return current_room, 1
