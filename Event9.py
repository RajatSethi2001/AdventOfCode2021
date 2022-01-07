file = open("input9.txt", "r")
data = file.read().splitlines()
data = [list(d) for d in data]

for r in range(len(data)):
    for c in range(len(data)):
        data[r][c] = int(data[r][c])

def get_basin(point, checked):
    r = point[0]
    c = point[1]
    
    if (r < 0 or r >= len(data)):
        return checked
    if (c < 0 or c >= len(data[r])):
        return checked
    if (data[r][c] == 9):
        return checked
    
    if (point not in checked):
        checked.append([r, c])
    else:
        return checked
        
    checked = get_basin([r+1, c], checked)
    checked = get_basin([r-1, c], checked)
    checked = get_basin([r, c+1], checked)
    checked = get_basin([r, c-1], checked)

    return checked
    


low_points = []
for r in range(len(data)):
    for c in range(len(data)):
        if (r != 0 and data[r][c] >= data[r-1][c]):
            continue
        if (r != (len(data) - 1) and data[r][c] >= data[r+1][c]):
            continue
        if (c != 0 and data[r][c] >= data[r][c-1]):
            continue
        if (c != (len(data[r]) - 1) and data[r][c] >= data[r][c+1]):
            continue
        low_points.append([r, c])

basin_sizes = []
for p in low_points:
    basin = get_basin(p, [])
    basin_sizes.append(len(basin))

basin_sizes.sort()
print(basin_sizes)