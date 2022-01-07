import copy

class BingoBoard:
    def __init__(self, markers):
        markers = markers.replace("  ", " ")
        self.board = markers.split("\n")
        try:
            self.board.remove('')
        except:
            pass

        for r in range(len(self.board)):
            self.board[r] = self.board[r].split(" ")
            try:
                self.board[r].remove('')
            except:
                pass

            for c in range(len(self.board[r])):
                self.board[r][c] = int(self.board[r][c])
            
        self.og_board = copy.deepcopy(self.board)
        
        #print(self.board)
    
    def remove_marker(self, marker):
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if (self.board[r][c] == marker):
                    self.board[r][c] = -1
    
    def check_rows(self):
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if (self.board[r][c] != -1):
                    break
                if (c == (len(self.board[r]) - 1)):
                    return True
        return False
    
    def check_cols(self):
        for c in range(len(self.board[0])):
            for r in range(len(self.board)):
                if (self.board[r][c] != -1):
                    break
                if (r == (len(self.board) - 1)):
                    return True
        return False

    def check_diags(self):
        for r in range(len(self.board)):
            if (self.board[r][r] != -1):
                break
            if (r == (len(self.board) - 1)):
                return True
        
        for r in range(len(self.board)):
            if (self.board[r][len(self.board) - r - 1] != -1):
                break
            if (r == (len(self.board) - 1)):
                return True
        return False

    def check_win(self):
        return (self.check_rows() or self.check_cols())

    def collect_answer(self, marker):
        sum = 0
        for r in self.board:
            for num in r:
                if (num != -1):
                    sum += num
        
        print(self.og_board)
        print(self.board)
        return (sum * marker)


file = open("input4.txt", "r")
bingo_nums = file.readline().split(",")
for i in range(len(bingo_nums)):
    bingo_nums[i] = int(bingo_nums[i])
file.readline()

bingo_data = file.read().split("\n\n")
boards = [BingoBoard(b) for b in bingo_data]

for m in bingo_nums:
    print(m)
    b = 0
    while b < len(boards):
        boards[b].remove_marker(m)
        winner = boards[b].check_win()

        if (winner):
            print(boards[b].collect_answer(m))
            boards.remove(boards[b])
        else:
            b += 1

#print(bingo_nums)