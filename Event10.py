file = open("input10.txt")
lines = file.read().splitlines()

open_brackets = ['(', '{', '[', '<']
close_brackets = [')', '}', ']', '>']

incomplete = []
for l in lines:
    bracket_stack = []
    corrupted = False
    for c in l:
        if (c == '('):
            bracket_stack.append(')')
        elif (c == '['):
            bracket_stack.append(']')
        elif (c == '{'):
            bracket_stack.append('}')
        elif (c == '<'):
            bracket_stack.append('>')
        else:
            bracket = bracket_stack[len(bracket_stack) - 1]
            bracket_stack = bracket_stack[0:len(bracket_stack)-1]
            if (c != bracket):
                corrupted = True
                break
    if (not corrupted):
        incomplete.append(l)

scores = []
for l in incomplete:
    bracket_stack = []
    points = 0
    for c in l:
        if (c == '('):
            bracket_stack.append(')')
        elif (c == '['):
            bracket_stack.append(']')
        elif (c == '{'):
            bracket_stack.append('}')
        elif (c == '<'):
            bracket_stack.append('>')
        else:
            bracket_stack.pop()

    bracket_stack.reverse()
    for b in bracket_stack:
        if (b == ')'):
            points = points * 5 + 1
        if (b == ']'):
            points = points * 5 + 2
        if (b == '}'):
            points = points * 5 + 3
        if (b == '>'):
            points = points * 5 + 4
        
    scores.append(points)

scores.sort()
print(scores[len(scores) // 2])