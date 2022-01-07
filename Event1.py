file = open("input1.txt", "r")
data = file.readlines()
data = [int(d) for d in data]

increases = 0
for i in range(3, len(data)):
    if ( (data[i-2] + data[i-1] + data[i]) > (data[i-3] + data[i-2] + data[i-1])):
        increases += 1

print(increases)