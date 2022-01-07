input_data = open("input7.txt", "r")
crabs = input_data.read().split(",")

crabs = [int(c) for c in crabs]

max_dist = max(crabs)

fuel = 9999999999999
for d in range(max_dist):
    fuel_total = 0
    for c in crabs:
        dist = abs(c - d)
        fuel_total += dist * (dist + 1) / 2
    
    if (fuel_total < fuel):
        fuel = fuel_total

print(fuel)