import copy

file = open("input15.txt","r")
map_data = file.read().splitlines()

for row in range(len(map_data)):
    map_data[row] = list(map_data[row])
    for col in range(len(map_data[row])):
        map_data[row][col] = int(map_data[row][col])

tile = copy.deepcopy(map_data)
for i in range(4):
    for row in range(len(tile)):
        for col in range(len(tile[row])):
            tile[row][col] += 1
            if (tile[row][col] > 9):
                tile[row][col] = 1
    
    for row in range(len(map_data)):
        map_data[row] = map_data[row] + tile[row]

tile = copy.deepcopy(map_data)
for i in range(4):
    for row in range(len(tile)):
        for col in range(len(tile[row])):
            tile[row][col] += 1
            if (tile[row][col] > 9):
                tile[row][col] = 1
        map_data.append(copy.deepcopy(tile[row]))

node_possible = {}
node_complete = {"0,0": 0}

end_y = len(map_data) - 1
end_x = len(map_data[end_y]) - 1

root_node = [0,0]
while f"{end_x},{end_y}" not in node_complete.keys():
    root_x = root_node[0]
    root_y = root_node[1]
    root_key = f"{root_x},{root_y}"

    neighbors = []
    if (root_x > 0):
        neighbors.append([root_x - 1, root_y])

    if (root_x < (len(map_data[root_y]) - 1)):
        neighbors.append([root_x + 1, root_y])

    if (root_y > 0):
        neighbors.append([root_x, root_y-1])

    if (root_y < (len(map_data) - 1)):
        neighbors.append([root_x, root_y+1])
    
    for node in neighbors:
        node_x = node[0]
        node_y = node[1]
        node_key = f"{node_x},{node_y}"
        new_cost = node_complete[root_key] + map_data[node_y][node_x]

        if (node_key in node_complete.keys()):
            continue

        elif (node_key not in node_possible.keys()):
            node_possible[node_key] = new_cost
        
        elif(new_cost < node_possible[node_key]):
            node_possible[node_key] = new_cost
    
    short_node = ""
    short_value = 999999
    for key in node_possible.keys():
        if (node_possible[key] < short_value):
            short_node = key
            short_value = node_possible[key]
    
    node_complete[short_node] = short_value
    node_possible.pop(short_node)

    new_root = short_node.split(",")
    root_node = [int(new_root[0]), int(new_root[1])]

print(node_complete[f"{end_x},{end_y}"])
