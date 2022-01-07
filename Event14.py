from collections import Counter
import copy

file = open("input14.txt","r")
input_str = file.readline().replace("\n","")
first = input_str[0]
last = input_str[len(input_str)-1]
file.readline()

insertions = file.read().splitlines()
insert_dict = {}
str_dict = {}
outputs = {}

for i in insertions:
    rule = i.split(" -> ")
    insert_dict[rule[0]] = rule[1]
    str_dict[rule[0]] = 0
    outputs[rule[1]] = 0

changes_template = copy.deepcopy(str_dict)

for c in range(len(input_str) - 1):
    key = f"{input_str[c]}{input_str[c+1]}"
    str_dict[key] += 1

for step in range(40):
    changes = copy.deepcopy(changes_template)
    for key in str_dict.keys():
        old_value = str_dict[key]
        new_char = insert_dict[key]
        new_key1 = f"{key[0]}{new_char}"
        new_key2 = f"{new_char}{key[1]}"

        changes[key] -= old_value
        changes[new_key1] += old_value
        changes[new_key2] += old_value
    
    for key in changes.keys():
        str_dict[key] += changes[key]
    print(step)


for key in str_dict.keys():
    value = str_dict[key]
    outputs[key[0]] += value
    outputs[key[1]] += value

outputs[first] += 1
outputs[last] += 1

answer = list(outputs.values())
answer.sort()
print(answer)