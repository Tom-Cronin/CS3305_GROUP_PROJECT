import random


# randomly generate the nodes in each level of the map, and what stage they represent
def generate_nodes_and_keys(number_of_levels):
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
                rand = random.randint(1, 10)
                if rand in [1, 2, 3, 4]:
                    node_key = "b"
                elif rand in [5, 6, 7]:
                    node_key = "?"
                elif rand in [8, 9]:
                    node_key = "P"
                else:
                    node_key = "T"
            list_of_levels[level_index].append([node_index, node_key, []])
            node_index += 1
    return list_of_levels


# randomly generate the connections between the nodes on each level of the map
def generate_node_connections(list_of_levels):
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
                for i in range(len_next_level):
                    for j in range(int(average) * (count - 1), int(average) * count, 1):
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
