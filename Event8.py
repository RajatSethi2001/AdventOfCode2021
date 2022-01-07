f = open("input8.txt", "r")
data = f.read().splitlines()
input_output = [d.split(" | ") for d in data]

total = 0
for i in input_output:
    inputs = i[0].split(" ")
    outputs = i[1].split(" ")
    all = inputs + outputs

    top_right = False
    top = False
    top_left = False
    middle = False
    bottom_left = False
    bottom = False
    bottom_right = False

    zero = False
    one = False
    two = False
    three = False
    four = False
    five = False
    six = False
    seven = False
    eight = set(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    nine = False

    for a in all:
        if (len(a) == 2):
            one = set(a)
        elif (len(a) == 3):
            seven = set(a)
        elif (len(a) == 4):
            four = set(a)
        
    while not (top_right and top and top_left and middle and bottom_left and bottom and bottom_right):
        print([top_right, top, top_left, middle, bottom_left, bottom, bottom_right])
        for a in all:
            if (len(a) == 5):
                if (four and seven):
                    bottom_test = set(a).difference(four).difference(seven)
                    if (len(bottom_test) == 1):
                        bottom = bottom_test.pop()
                
                if (four and top and bottom):
                    bottom_left_test = set(a).difference(four).difference(set([top, bottom]))
                    if (len(bottom_left_test) == 1):
                        bottom_left = bottom_left_test.pop()
                
                if (seven and bottom and bottom_left):
                    middle_test = set(a).difference(seven).difference(set([bottom, bottom_left]))
                    if (len(middle_test) == 1):
                        middle = middle_test.pop()

            if (len(a) == 6):
                if (seven and bottom and middle):
                    top_left_test = set(a).difference(seven).difference(set([bottom, middle]))
                    if (len(top_left_test) == 1):
                        top_left = top_left_test.pop()
                
                if (top_left and top and middle and bottom_left and bottom):
                    bottom_right_test = set(a).difference(set([top_left, top, middle, bottom_left, bottom]))
                    if (len(bottom_right_test) == 1):
                        bottom_right = bottom_right_test.pop()
                
                if (top_left and top and middle and bottom_left and bottom and bottom_right):
                    top_right_test = set(a).difference(set([top_left, top, middle, bottom_left, bottom, bottom_right]))
                    if (len(top_right_test) == 1):
                        top_right = top_right_test.pop()
        
        if (seven and one):
            top = seven.difference(one).pop()

        if (top_right and top and top_left and bottom_left and bottom and bottom_right):
            zero = set([top_right, top, top_left, bottom_left, bottom, bottom_right])
        if (top_right and bottom_right):
            one = set([top_right, bottom_right])
        if (top_right and top and middle and bottom_left and bottom):
            two = set([top_right, top, middle, bottom_left, bottom])
        if (top_right and top and middle and bottom_right and bottom):
            three = set([top_right, top, middle, bottom_right, bottom])
        if (top_right and top_left and middle and bottom_right):
            four = set([top_right, top_left, middle, bottom_right])
        if (top and top_left and middle and bottom and bottom_right):
            five = set([top, top_left, middle, bottom, bottom_right])
        if (top and top_left and middle and bottom_left and bottom and bottom_right):
            six = set([top, top_left, middle, bottom_left, bottom, bottom_right])
        if (top_right and top and bottom_right):
            seven = set([top_right, top, bottom_right])
        if (top_right and top and top_left and middle and bottom and bottom_right):
            nine = set([top_right, top, top_left, middle, bottom, bottom_right])

    digits = [zero, one, two, three, four, five, six, seven, eight, nine]
    digitstr = ""
    for digit in outputs:
        digitstr = f"{digitstr}{digits.index(set(digit))}"
    
    total += int(digitstr)

print(total)