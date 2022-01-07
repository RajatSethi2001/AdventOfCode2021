file = open("input2.txt", "r")
data = file.readlines()
data = [d.replace('\n','').split(" ") for d in data]

hor = 0
ver = 0
aim = 0
for i in range(len(data)):
    if (data[i][0] == "forward"):
        hor += int(data[i][1])
        ver += aim * int(data[i][1])
    elif (data[i][0] == "up"):
        aim -= int(data[i][1])
    elif (data[i][0] == "down"):
        aim += int(data[i][1])

print(hor)
print(ver)
print(hor * ver)