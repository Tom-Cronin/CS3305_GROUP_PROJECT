import pygame as pygame


def draw_level_map(list_of_nodes, screen_width, screen_height, screen, current_node):
    next_nodes = []
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    darkBlue = (0, 0, 128)
    white = (255, 255, 255)
    black = (0, 0, 0)
    grey = (192, 192, 192)
    pink = (255, 200, 200)
    node_dict = {}
    node_index = 0
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
                circle_x = int(node_x * (i + 1) - (node_x / 2))
                circle_y = int(screen_height - node_height * (level_index + 1) + 20)

                if node_index == current_node:
                    circle_width = circle_radius
                    circle_colour = red
                    next_nodes = list_of_nodes[level_index][i][2]
                elif node_index < current_node:
                    circle_colour = grey
                    circle_width = 1
                    circle_width = circle_radius
                elif (node_index+1) in next_nodes:
                    circle_width = circle_radius
                    circle_colour = blue
                else:
                    circle_width = 1
                    circle_colour = black
                circle = pygame.draw.circle(screen, circle_colour, (circle_x, circle_y), circle_radius, circle_width)
                node_dict[node_index] = circle
                node_index += 1
                text = myfont.render("%s" % node_key, True, black)
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
                            pygame.draw.lines(screen, black, True, [(int(from_node_x * (i + 1) - (from_node_x / 2)),
                                                                   int(screen_height - node_height * (
                                                                           level_index + 1))),
                                                                  (int(to_node_x * (q + 1) - (to_node_x / 2)),
                                                                   int(screen_height - node_height * (level_index + 2) +
                                                                       node_height - circle_radius))], 1)

        pygame.display.update()
        length_next_nodes = len(next_nodes)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for item in range(length_next_nodes):
                    rectangle = node_dict[next_nodes[item]-1]
                    click = rectangle.collidepoint(pos)
                    if click == 1:
                        current_node = next_nodes[item]-1
                        print("Selected node: ", current_node)
                        screen.fill(white)
                        pygame.display.update()
                        return current_node



