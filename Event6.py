input_data = open("input6.txt", "r")
fish = input_data.read().split(",")
fish = [int(f) for f in fish]
fish_dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}

for f in fish:
    fish_dict[f] += 1

for i in range(256):
    new_fish = 0
    day = 8

    next_day = fish_dict[day]
    while (day > 0):
        stored_fish = fish_dict[day - 1]
        fish_dict[day - 1] = next_day
        next_day = stored_fish
        day -= 1

    fish_dict[8] = next_day
    fish_dict[6] += next_day
    print(f"Day {i+1}: {sum(fish_dict.values())}")

print(sum(fish_dict.values()))