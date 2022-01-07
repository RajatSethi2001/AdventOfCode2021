file = open("input11.txt", "r")
data = file.read().splitlines()

for r in range(len(data)):
    data[r] = list(data[r])
    for c in range(len(data[r])):
        data[r][c] = int(data[r][c])

flashes = 0
flashpoints = []
def flash(point):
    global flashes
    global flashpoints
    global data
    r = point[0]
    c = point[1]
    if (r < 0 or r >= len(data)):
        return
    if (c < 0 or c >= len(data[r])):
        return
    
    data[r][c] += 1
    if (data[r][c] <= 9):
        return
    
    if ([r, c] not in flashpoints):
        flashes += 1
        flashpoints.append([r, c])
        for r_change in range(-1, 2):
            for c_change in range(-1, 2):
                if (r_change != 0 or c_change != 0):
                    flash([r + r_change, c + c_change])

steps = 0
while True:
    steps += 1
    for r in range(len(data)):
        for c in range(len(data[r])):
            data[r][c] += 1

    for r in range(len(data)):
        for c in range(len(data[r])):
            if (data[r][c] > 9):
                flash([r, c])
    
    for r in range(len(data)):
        for c in range(len(data[r])):
            if (data[r][c] > 9):
                data[r][c] = 0
    
    if (len(flashpoints) == len(data) * len(data[0])):
        break

    flashpoints = []

print(steps)