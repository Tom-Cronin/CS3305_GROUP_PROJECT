from random import *

#node key
#0 = first entry node
#1 = battle
#2 = puzzle
#3 = mystery
#4 = treasure chest
#5 = final battle

#Each node is a list [node ID number, node key(as above), [list of previous nodes], [list of following nodes]]

def generate_map_list():
    level = 1
    number_of_nodes = randint(10, 20+level)
    node_index = 1
    # print(number_of_nodes)
    list_of_nodes = [[0,0,[],[]]]
    previous_node = 0
    node = 0

    while (node_index <= number_of_nodes):
        if (node_index == number_of_nodes):
            random_number = 15
        else:
            random_number = randint(0, 11)
        previous_nodes = []

        random_previous_nodes = randint(0, 7)
        if (random_previous_nodes <=5):
            number_of_previous_nodes = 1
        elif (random_previous_nodes == 6):
            number_of_previous_nodes =2
        else:
            number_of_previous_nodes = 3

        for num in range(number_of_previous_nodes):
            if (node_index<5):
                selected_node = randint(0, node_index-1)
            else:
                selected_node = randint(node_index-3, node_index)
            if (selected_node in previous_nodes):
                number_of_previous_nodes +=1
            elif (selected_node == node_index):
                previous_nodes.append(node_index-1)
            else:
                previous_nodes.append(selected_node)

        if (random_number <= 3 and random_number >= 0):
            list_of_nodes.append([node_index, 1, previous_nodes, []])
            previous_node = 1
            node_index +=1
        elif (random_number <=7 and random_number >= 4):
            list_of_nodes.append([node_index, 2, previous_nodes, []])
            previous_node = 2
            node_index += 1
        elif (random_number <= 9 and random_number >= 5 and previous_node != 3):
            list_of_nodes.append([node_index, 3, previous_nodes, []])
            previous_node = 3
            node_index += 1
        elif (random_number <=11 and random_number >=10 and previous_node != 4):
            list_of_nodes.append([node_index, 4, previous_nodes, []])
            previous_node = 4
            node_index += 1
        elif (random_number == 15):
            #print("DONE")
            list_of_nodes.append([node_index, 5, previous_nodes, []])
            node_index += 1


    for index in range(len(list_of_nodes)):
        for sub_index in range(len(list_of_nodes[index][2])):
            prev_node = list_of_nodes[index][2][sub_index]
            list_of_nodes[prev_node][3].append(index)

    for index in range(len(list_of_nodes)-1):
        if (len(list_of_nodes[index][3]) == 0):
            list_of_nodes[index][3].append(index+1)
            list_of_nodes[index+1][2].append(index)
    return(list_of_nodes)

list_of_nodes = generate_map_list()
#print(list_of_nodes)