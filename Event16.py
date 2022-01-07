file = open("input16.txt","r")
hex_string = file.read()

bit_string = ""
for c in hex_string:
    if (c == '0'):
        bit_string = f"{bit_string}0000"
    elif (c == '1'):
        bit_string = f"{bit_string}0001"
    elif (c == '2'):
        bit_string = f"{bit_string}0010"
    elif (c == '3'):
        bit_string = f"{bit_string}0011"
    elif (c == '4'):
        bit_string = f"{bit_string}0100"
    elif (c == '5'):
        bit_string = f"{bit_string}0101"
    elif (c == '6'):
        bit_string = f"{bit_string}0110"
    elif (c == '7'):
        bit_string = f"{bit_string}0111"
    elif (c == '8'):
        bit_string = f"{bit_string}1000"
    elif (c == '9'):
        bit_string = f"{bit_string}1001"
    elif (c == 'A'):
        bit_string = f"{bit_string}1010"
    elif (c == 'B'):
        bit_string = f"{bit_string}1011"
    elif (c == 'C'):
        bit_string = f"{bit_string}1100"
    elif (c == 'D'):
        bit_string = f"{bit_string}1101"
    elif (c == 'E'):
        bit_string = f"{bit_string}1110"
    elif (c == 'F'):
        bit_string = f"{bit_string}1111"

bit_index = 0
versions = 0
iter = 0

def calculate(version, operands):
    if (version == 0):
        sum = 0
        for ope in operands:
            sum += ope
        return sum
    elif (version == 1):
        product = 1
        for ope in operands:
            product *= ope
        return product
    elif (version == 2):
        return min(operands)
    elif (version == 3):
        return max(operands)
    elif (version == 5):
        return (operands[0] > operands[1])
    elif (version == 6):
        return (operands[0] < operands[1])
    elif (version == 7):
        return (operands[0] == operands[1])

def read_length(version):
    global iter
    global bit_string
    print("Operator - Length")
    total_bits = '0'
    for i in range(iter, iter + 15):
        total_bits = f"{total_bits}{bit_string[iter]}"
        iter += 1

    packet_length = int(total_bits, 2)
    start_point = iter
    operands = []
    while ( (iter - start_point) < packet_length):
        value = read_packet()
        operands.append(value)
    
    return calculate(version, operands)

def read_num(version):
    global iter
    global bit_string
    print('Operator - Number')
    print(version)
    total_packets = '0'
    for i in range(iter, iter + 11):
        total_packets = f"{total_packets}{bit_string[iter]}"
        iter += 1

    packet_num = int(total_packets, 2)
    current_packet = 0
    operands = []
    while (current_packet < packet_num):
        value = read_packet()
        operands.append(value)
        current_packet += 1

    return calculate(version, operands)

def read_literal():
    global iter
    global bit_string
    print('Literal')
    start_bit = "1"
    number = "0"
    while (start_bit == "1"):
        start_bit = bit_string[iter]
        iter += 1
        for i in range(iter, iter + 4):
            number = f"{number}{bit_string[iter]}"
            iter += 1
    
    return int(number, 2)

def read_packet():
    global versions
    global bit_string
    global iter
    version = "0"
    for i in range(iter, iter + 3):
        version = f"{version}{bit_string[iter]}"
        iter += 1
    version_int = int(version, 2)
    versions += version_int

    packet_type = "0"
    for i in range(iter, iter + 3):
        packet_type = f"{packet_type}{bit_string[iter]}"
        iter += 1

    version_int = int(packet_type, 2)
    
    val = 0
    if (packet_type == "0100"):
        val = read_literal()
    
    else:
        length = bit_string[iter]
        iter += 1

        if (length == '0'):
            val = read_length(version_int)
        
        else:
            val = read_num(version_int)

    return val

val = read_packet()       
print(val) 
