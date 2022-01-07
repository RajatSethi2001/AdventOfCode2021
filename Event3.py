import random

input_data = open('input3', 'r')
data = input_data.readlines()
data = [int(d.replace('\n', ''), 2) for d in data]
oxygen = []+data
CO2 = []+data

Oxygen_Rating = 0
CO2_Rating = 0

gamma = ""
epsilon = ""
mask = 1
index = 0

while(mask < data[0] / 2):
    mask = mask << 1

mask_start = mask

while (mask > 0):
    zeroes = 0
    ones = 0
    for index in range(len(oxygen)):
        if (mask & oxygen[index]):
            ones += 1
        else:
            zeroes += 1
    
    if (ones >= zeroes):
        index = 0
        while (index < len(oxygen)):
            if (len(oxygen) == 1):
                break

            if ((oxygen[index] & mask) == 0):
                oxygen.remove(oxygen[index])
            else:
                index += 1
            
    else:        
        index = 0
        while (index < len(oxygen)):
            if (len(oxygen) == 1):
                break

            if ((oxygen[index] & mask)):
                oxygen.remove(oxygen[index])
            else:
                index += 1

    mask = mask >> 1

mask = mask_start

while (mask > 0):
    zeroes = 0
    ones = 0
    for index in range(len(CO2)):
        if (mask & CO2[index]):
            ones += 1
        else:
            zeroes += 1
    
    print(len(CO2))
    if (zeroes <= ones):
        index = 0
        while (index < len(CO2)):
            if (len(CO2) == 1):
                break

            if ((CO2[index] & mask)):
                CO2.remove(CO2[index])
            else:
                index += 1
        
    else:
        index = 0
        while (index < len(CO2)):
            if (len(CO2) == 1):
                break
    
            if ((CO2[index] & mask) == 0):
                CO2.remove(CO2[index])
            else:
                index += 1

    mask = mask >> 1

print(CO2)
print(oxygen)
    
    

    


