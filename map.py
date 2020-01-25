import time
import pygame
import random


# map() creates the map and returns a list representation of the map, but this isn't needed
# Map keeps track of the current level, and the players position within that level
# Each time you call myMap.getUserSelection() the map will appear for the user to select their next step
# It will automatically move the user forward to the step they chose during the previous function call
# It returns the key of the users selected node:
# P = puzzle, b = battle, ? = mystery, T = treasure, B = final battle (also indicates end of level)

class map(object):
    def __init__(self, screen, screen_width, screen_height, seed):
        self.seed = seed
        self.level = 0
        self.node = -1
        self.selectedNode = None
        self.selected_node_key = None
        self.map = self.generate_map_list()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = screen

    def check_for_end_of_map(self):
        if self.selected_node_key == "B":
            self.node = -1
            self.level += 1
            self.map = self.generate_map_list()

    def generate_map_list(self):
        nodes_per_level = 0
        seed = str(self.level) + str(self.seed)
        random.seed(seed)
        number_of_levels = random.randint(10, 10)
        level_index = 0
        node_index = 1
        list_of_levels = []

        while level_index <= number_of_levels:
            list_of_levels.append([])
            if level_index == number_of_levels:
                nodes_per_level = 1
            elif level_index == 0:
                nodes_per_level = random.randint(1, 3)
            else:
                nodes_per_level = random.randint(1, nodes_per_level + 1)
                while nodes_per_level > 4:
                    nodes_per_level = random.randint(1, nodes_per_level)
            for node in range(nodes_per_level):
                if level_index == 0:
                    node_key = "S"
                elif level_index == number_of_levels:
                    node_key = "B"
                elif level_index == number_of_levels - 1:
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
            level_index += 1

        for level in range(len(list_of_levels) - 1):
            next_level = level + 1
            len_level = len(list_of_levels[level])
            len_next_level = len(list_of_levels[next_level])
            # print(len_level, len_next_level)
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
                        if list_of_levels[level][i][2] == []:
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
                        if list_of_levels[level][i][2] == []:
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
        white = (255, 255, 255)
        black = (0, 0, 0)
        grey = (192, 192, 192)
        node_dict = {}
        node_index = 0
        circle_radius = 20
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 10)
        while True:
            num_levels = len(self.map)
            node_height = int(round(self.screen_height / num_levels))

            for level_index in range(num_levels):
                node_x = int(round(self.screen_width / len(self.map[level_index])))

                for i in range(len(self.map[level_index])):
                    node_key = self.map[level_index][i][1]
                    circle_x = int(node_x * (i + 1) - (node_x / 2))
                    circle_y = int(self.screen_height - node_height * (level_index + 1) + 20)

                    if self.node == -1:
                        next_nodes = []
                        for node in self.map[0]:
                            next_nodes.append(node[0])
                    if node_index == self.node:
                        circle_width = circle_radius
                        circle_colour = red
                        next_nodes = self.map[level_index][i][2]
                    elif node_index < self.node:
                        circle_colour = grey
                        circle_width = 1
                        circle_width = circle_radius
                    elif (node_index + 1) in next_nodes:
                        next_nodes_dict[node_index] = node_key
                        circle_width = circle_radius
                        circle_colour = blue
                    else:
                        circle_width = 1
                        circle_colour = black
                    circle = pygame.draw.circle(self.screen, circle_colour, (circle_x, circle_y), circle_radius,
                                                circle_width)
                    node_dict[node_index] = circle
                    node_index += 1
                    text = myfont.render("%s" % node_key, True, black)
                    self.screen.blit(text, (int(node_x * (i + 1) - (node_x / 2)) - 4,
                                            int(self.screen_height - node_height * (level_index + 1) + 20) - 6))
            for level_index in range(num_levels):
                level_length = len(self.map[level_index])
                for i in range(level_length):
                    from_node_x = self.screen_width / len(self.map[level_index])
                    number_of_to_nodes = len(self.map[level_index][i][2])
                    for j in range(number_of_to_nodes):
                        to_node_x = self.screen_width / len(self.map[level_index + 1])
                        for to_node_index in range(len(self.map[level_index + 1])):
                            if self.map[level_index + 1][to_node_index][0] == self.map[level_index][i][2][j]:
                                q = to_node_index
                                pygame.draw.lines(self.screen, black, True,
                                                  [(int(from_node_x * (i + 1) - (from_node_x / 2)),
                                                    int(self.screen_height - node_height * (
                                                            level_index + 1))),
                                                   (int(to_node_x * (q + 1) - (to_node_x / 2)),
                                                    int(self.screen_height - node_height * (
                                                            level_index + 2) +
                                                        node_height - circle_radius))], 1)

            pygame.display.update()
            length_next_nodes = len(next_nodes)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    for item in range(length_next_nodes):
                        rectangle = node_dict[next_nodes[item] - 1]
                        click = rectangle.collidepoint(pos)
                        if click == 1:
                            self.node = next_nodes[item] - 1
                            node_key = next_nodes_dict[self.node]
                            # print("Selected node: ", self.node, node_key)
                            self.screen.fill(white)
                            pygame.display.update()
                            return node_key

    def get_user_selection(self):
        self.selected_node_key = self.draw_map()
        self.check_for_end_of_map()
        return self.selected_node_key
