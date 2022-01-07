import ast
import copy

exploded = False
split = False

class Node:
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value

        if (isinstance(value, list)):
            self.insert(value)
    
    def get_value(self):
        return self.value

    def change_value(self, value):
        self.value = value

    def insert(self, value):
        left_child = Node(value[0])
        right_child = Node(value[1])
        
        self.left = left_child
        self.right = right_child
    
    def zero(self):
        self.left = None
        self.right = None
        self.value = 0

def add_nodes(node1, node2):
    new_value = [node1.get_value(), node2.get_value()]
    return Node(new_value)

def add_pos(tar_pos, value, node, cur_pos):
    if (tar_pos < 0):
        return
    
    new_pos = cur_pos
    if (isinstance(node.get_value(), int)):
        new_pos += 1
        if (new_pos == tar_pos):
            node.change_value(node.get_value() + value)
        return new_pos
    
    new_pos += add_pos(tar_pos, value, node.get_value()[0], new_pos)
    new_pos += add_pos(tar_pos, value, node.get_value()[1], new_pos)

def explode(node, rank, position, head):
    global exploded
    if (exploded):
        return position

    new_pos = position
    if (isinstance(node.get_value(), int)):
        new_pos += 1
        return new_pos
    
    new_pos += explode(node.get_value()[0], rank+1, new_pos, head)

    if (rank == 4 and isinstance(node.get_value(), list) and isinstance(node.get_value()[0], int) and isinstance(node.get_value()[0], int)):
        exploded = True
        add_pos(position - 1, node.get_value()[0], head, -1)
        add_pos(position + 2, node.get_value()[1], head, -1)
        node.zero()
        return new_pos + 2
    
    new_pos += explode(node.get_value()[1], rank+1, new_pos, head)

def split_node(node):
    global split
    if (split):
        return

    if (isinstance(node.get_value(), int)):
        if (node.get_value() >= 10):
            split = True
            left = node.get_value() // 2
            right = node.get_value() - left
            new_value = [left, right]
            node.change_value(new_value)
            node.insert(new_value)
        return

    split_node(node.get_value()[0])
    split_node(node.get_value()[1])

file = open('input18.txt')
data = file.read().splitlines()

for s in range(len(data)):
    data[s] = ast.literal_eval(data[s])

test_node = Node(data[0])
