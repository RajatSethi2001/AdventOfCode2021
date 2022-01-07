file = open("input12.txt","r")
data = file.read().splitlines()

paths = {}

for d in data:
    path = d.split("-")
    if (path[0] not in paths.keys()):
        paths[path[0]] = [path[1]]
    else:
        paths[path[0]] = paths[path[0]] + [path[1]]
    
    if (path[1] not in paths.keys()):
        paths[path[1]] = [path[0]]
    else:
        paths[path[1]] = paths[path[1]] + [path[0]]

def double_taken(path):
    for i in range(len(path)):
        for j in range(len(path)):
            if (i != j and path[i] == path[j] and path[i].islower()):
                return True
    return False


all_routes = [] 
def traverse(current, path):
    if (current == "start" and "start" in path):
        return

    if (current.islower() and double_taken(path) and current in path):
        return
    
    new_path = path + [current]

    if (current == "end"):
        all_routes.append(new_path)
        return
    
    for node in paths[current]:
        traverse(node, new_path)

traverse("start", [])
print(len(all_routes))