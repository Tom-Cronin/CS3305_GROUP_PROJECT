from test1 import generate_map_list
from tkinter import *

list_of_nodes = generate_map_list()

for node in list_of_nodes:
    print(node)

#Each node is a list [node ID number, node key(as below), [list of previous nodes], [list of following nodes]]
#node key
#   0 = first entry node
#   1 = battle
#   2 = puzzle
#   3 = mystery
#   4 = treasure chest
#   5 = final battle

def draw_map():
    length = len(list_of_nodes)

    master = Tk()

    canvas_width = 800
    canvas_height = 650
    w = Canvas(master, width=canvas_width, height=canvas_height)
    w.pack()

    size = 60
    startx = -50
    starty = canvas_height-size-10
    direction = 1
    node_dict = {}

    if (length < 15):
        turn_nodes = [4, 7, 10, 13]
        turn_nodes_minus = [3, 6, 9, 12]
    elif (length < 23):
        turn_nodes = [8, 14, 20]
        turn_nodes_minus = [7, 13, 19]
    elif (length < 26):
        turn_nodes = [9, 17]
        turn_nodes_minus = [8, 16]
    else:
        turn_nodes = [10, 18, 25]
        turn_nodes_minus = [9, 17, 24]

    for index in range(length):
        if (index in turn_nodes):
            direction = direction*(-1)

        if (index in turn_nodes):
            startx += (size+10) * direction
            starty -= (size * .6)
            w.create_oval(startx, starty, startx + (size), starty + size)
        elif (index in turn_nodes_minus):
            startx += (size+10) * direction
            starty -= (size * .7)
            w.create_oval(startx, starty, startx + (size), starty + size)
        else:
            startx += (size+15)*direction
            starty -= (size*.25)
            w.create_oval(startx, starty, startx + (size),  starty+size)

        node_dict[index]=[startx, starty, direction]

        #label nodes
        node_key = list_of_nodes[index][1]
        if (node_key == 0):
            w.create_text(startx+size/2, starty+size/2, text="Start" )
        elif (node_key == 1):
            w.create_text(startx + size / 2, starty + size / 2, text="Battle")
        elif (node_key == 2):
            w.create_text(startx + size / 2, starty + size / 2, text="Puzzle")
        elif (node_key == 3):
            w.create_text(startx + size / 2, starty + size / 2, text="?")
        elif (node_key == 4):
            w.create_text(startx + size / 2, starty + size / 2, text="Treasure")
        elif (node_key == 5):
            w.create_text(startx + size / 2, starty + size / 2, text="BATTLE")

    for index in range(length):
        indexx = node_dict[index][0]
        indexy = node_dict[index][1]
        next_nodes = list_of_nodes[index][3]
        index_direction = node_dict[index][2]
        #print(index, next_nodes)
        number_nodes = len(next_nodes)
        if (number_nodes > 0):
            for next_node in range(number_nodes):
                node = next_nodes[next_node]
                direction = node_dict[node][2]
                nodex = node_dict[node][0]
                nodey = node_dict[node][1]
                direction_size = 0
                if (index_direction == direction or index in turn_nodes_minus):
                    if (direction == -1):
                        direction_size = size
                    if (node - index == 1):
                        w.create_line(indexx + size-direction_size, indexy+(size/2), nodex + direction_size, nodey+(size/2), fill="#476042")
                    else:
                        if (direction == 1):
                            w.create_line(indexx + (size/2), indexy, ((nodex - indexx)) / 2 + indexx, nodey-size, nodex, nodey+(size/2), smooth="true")
                        else:
                            w.create_line(indexx + (size/2), indexy, ((nodex +size - indexx+ size)) / 2 + indexx, nodey-size , nodex+size, nodey + (size / 2), smooth="true")
                else:
                    w.create_line(indexx + (size/2), indexy, nodex + (size/2), nodey + size, fill="#476042")
    mainloop()

draw_map()