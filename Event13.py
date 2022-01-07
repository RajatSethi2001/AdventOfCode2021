file = open("input13.txt", "r")
data = file.read()
map_folds = data.split("\n\n")

map_info = map_folds[0].splitlines()
fold_info = map_folds[1].splitlines()

map_data = set(map_info)
fold_queue = []
for f in fold_info:
    fold = f.replace("fold along ", "").split("=")
    fold[1] = int(fold[1])
    fold_queue.append(fold)

for f in fold_queue:
    if (f[0] == "x"):
        to_remove = []
        to_add = []
        for val in map_data:
            point = val.split(",")
            point[0] = int(point[0])
            point[1] = int(point[1])
            
            if (point[0] > f[1]):
                to_remove.append(val)
                dist = point[0] - f[1]
                to_add.append(f"{f[1] - dist},{point[1]}")
        
        for val in to_remove:
            map_data.remove(val)
        
        for val in to_add:
            map_data.add(val)
    
    else:
        to_remove = []
        to_add = []
        for val in map_data:
            point = val.split(",")
            point[0] = int(point[0])
            point[1] = int(point[1])
            
            if (point[1] > f[1]):
                to_remove.append(val)
                dist = point[1] - f[1]
                to_add.append(f"{point[0]},{f[1] - dist}")
        
        for val in to_remove:
            map_data.remove(val)
        
        for val in to_add:
            map_data.add(val)
    
    print(f"Number of Coords: {len(map_data)}")

max_x = 0
max_y = 0
for val in map_data:
    point = val.split(",")
    point[0] = int(point[0])
    point[1] = int(point[1])

    if (point[0] > max_x):
        max_x = point[0]
    
    if (point[1] > max_y):
        max_y = point[1]

for y in range(max_y + 1):
    print_this = ""
    for x in range(max_x + 1):
        if f"{x},{y}" in map_data:
            print_this += '# '
        else:
            print_this += '. '
    print(print_this)
