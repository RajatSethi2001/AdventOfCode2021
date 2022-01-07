class Line:
    def __init__(self, line):
        coord1 = line[0].split(",")
        coord2 = line[1].split(",")
        self.x1 = int(coord1[0])
        self.y1 = int(coord1[1])
        self.x2 = int(coord2[0])
        self.y2 = int(coord2[1])
    
    def is_horizontal(self):
        return (self.y1 == self.y2)
    
    def is_vertical(self):
        return (self.x1 == self.x2)

    def is_diagonal(self):
        return (abs(self.x1 - self.x2) == abs(self.y1 - self.y2))

    def get_coords(self):
        coords = []
        if (self.is_horizontal()):
            small_x = min(self.x1, self.x2)
            big_x = max(self.x1, self.x2)
            x_counter = small_x
            while (x_counter <= big_x):
                coord = f"{x_counter},{self.y1}"
                coords.append(coord)
                x_counter += 1
        
        elif (self.is_vertical()):
            small_y = min(self.y1, self.y2)
            big_y = max(self.y1, self.y2)
            y_counter = small_y
            while (y_counter <= big_y):
                coord = f"{self.x1},{y_counter}"
                coords.append(coord)
                y_counter += 1
        
        elif (self.is_diagonal()):
            small_x = min(self.x1, self.x2)
            big_x = max(self.x1, self.x2)
            if (small_x == self.x1):
                small_y = self.y1
                big_y = self.y2
            else:
                small_y = self.y2
                big_y = self.y1

            if (small_y <= big_y):
                y_change = 1
            else:
                y_change = -1

            x_counter = small_x
            y_counter = small_y
            while (x_counter <= big_x):
                coord = f"{x_counter},{y_counter}"
                coords.append(coord)
                x_counter += 1
                y_counter += y_change
        
        return coords

input_data = open("input5.txt", "r")
lines = input_data.readlines()
coord_dict = {}

for l in range(len(lines)):
    lines[l] = lines[l].replace("\n", "")
    lines[l] = lines[l].split(" -> ")
    lines[l] = Line(lines[l])
    coords = lines[l].get_coords()
    for c in coords:
        if (c not in coord_dict.keys()):
            coord_dict[c] = 1
        else:
            coord_dict[c] += 1

two_plus = 0
for v in coord_dict.values():
    if (v >= 2):
        two_plus += 1

print(two_plus)