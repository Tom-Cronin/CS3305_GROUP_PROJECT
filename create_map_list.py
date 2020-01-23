import random

# node key
# 0 = first entry node
# 1 = battle
# 2 = puzzle
# 3 = mystery
# 4 = treasure chest
# 5 = final battle
# Each node is a list [node ID number, node key(as above), [list of previous nodes], [list of following nodes]]

def generate_map_list(level):
    nodes_per_level = 0
    random.seed(level)
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
                    if (list_of_levels[level][i][2] == []):
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
                    if (list_of_levels[level][i][2] == []):
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
