file = open("input17.txt","r")
data = file.read()
data = data.replace("target area: ", "")

target = data.split(", ")
x = target[0].split("=")[1].split("..")
min_x = int(x[0])
max_x = int(x[1])

y = target[1].split("=")[1].split("..")
min_y = int(y[0])
max_y = int(y[1])

highest_y = 0
all_inits = 0
for x_vel in range(1, max_x + 1):
    for y_vel in range(min_y, abs(min_y)):
        print(x_vel)
        start_x_vel = x_vel
        start_y_vel = y_vel
        
        x_pos = 0
        y_pos = 0

        high_y = 0
        target = False
        while (not((y_pos < min_y) and (start_y_vel < 0)) and (x_pos < max_x)):
            x_pos += start_x_vel
            y_pos += start_y_vel

            if (start_x_vel > 0):
                start_x_vel -= 1
            elif (start_x_vel < 0):
                start_x_vel += 1
            
            start_y_vel -= 1

            if (y_pos > high_y):
                high_y = y_pos
            
            if (x_pos >= min_x and x_pos <= max_x and y_pos >= min_y and y_pos <= max_y):
                target = True
                all_inits += 1
                break
        
        if (target and high_y > highest_y):
            highest_y = high_y

print(highest_y)
print(all_inits)