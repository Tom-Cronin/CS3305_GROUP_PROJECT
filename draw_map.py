from create_map_list import generate_map_list
from tkinter import *


# Each node is a list [node ID number, node key(as below), [list of previous nodes], [list of following nodes]]
# node key
#   0 = first entry node
#   1 = battle
#   2 = puzzle
#   3 = mystery
#   4 = treasure chest
#   5 = final battle

def draw_map(level):
    list_of_nodes = generate_map_list(level)
    num_levels = len(list_of_nodes)
    master = Tk()
    canvas_width = 800
    canvas_height = 650
    w = Canvas(master, width=canvas_width, height=canvas_height)
    w.pack()
    node_height = canvas_height / num_levels

    for level_index in range(num_levels):
        node_x = canvas_width / len(list_of_nodes[level_index])
        for i in range(len(list_of_nodes[level_index])):
            node_key = list_of_nodes[level_index][i][1]

            w.create_oval(node_x * (i + 1) - (node_x / 2), canvas_height - node_height * (level_index + 1),
                          node_x * (i + 1) + node_height -
                          25 - (node_x / 2), canvas_height - node_height * (level_index + 1) + node_height - 25)
            circle_radius = ((node_x * (i + 1) + node_height - 25 - (node_x / 2)) - (
                    node_x * (i + 1) - (node_x / 2))) / 2
            w.create_text((node_x * (i + 1) - (node_x / 2)) + circle_radius,
                          (canvas_height - node_height * (level_index + 1)) + circle_radius,
                          text="%s" % (list_of_nodes[level_index][i][1]))
            print(circle_radius)

    for level_index in range(num_levels):
        level_length = len(list_of_nodes[level_index])
        for i in range(level_length):
            from_node_x = canvas_width / len(list_of_nodes[level_index])
            number_of_to_nodes = len(list_of_nodes[level_index][i][2])
            for j in range(number_of_to_nodes):
                to_node_x = canvas_width / len(list_of_nodes[level_index + 1])
                for to_node_index in range(len(list_of_nodes[level_index + 1])):
                    if list_of_nodes[level_index + 1][to_node_index][0] == list_of_nodes[level_index][i][2][j]:
                        q = to_node_index
                        w.create_line(from_node_x * (i + 1) - (from_node_x / 2) + 12.5, canvas_height - node_height *
                                      (level_index + 1), to_node_x * (q + 1) - (to_node_x / 2) + 12.5, canvas_height -
                                      node_height * (level_index + 2) + node_height - 25)

    mainloop()


 for level in range(10):
    draw_map(level)

#draw_map(1)
