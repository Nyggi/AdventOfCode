# %%
with open('input.txt', 'r') as f:
    data = f.read()

data =  data.split('\n')
# %%
data
# %%
draws = data[0].split(',')
# %%
draws
# %%
def clean_board(board_data) -> list:
    board = []
    for row in board_data:
        row = [number for number in row if number != '']
        board.append(row)
    
    return board
# %%
class BingoBoard:

    def __init__(self, board_data) -> None:
        cleaned_board = clean_board(board_data)
        self.number_board = cleaned_board
        self.reset_board()
    
    def check_row(self, row_index) -> bool:
        row = self.board[row_index]
        if row.count(True) == len(row):
            return True
        return False

    def check_column(self, column_index) -> bool:
        column = [row[column_index] for row in self.board]
        if column.count(True) == len(column):
            return True
        return False

    def bingo(self) -> bool:
        for row_index in range(len(self.board)):
            if self.check_row(row_index):
                return True
        for col_index in range(len(self.board[0])):
            if self.check_column(col_index):
                return True

        return False
    
    def mark_number(self, number) -> None:
        for row_index in range(len(self.number_board)):
            row = self.number_board[row_index]
            if number in row:
                self.board[row_index][row.index(number)] = True
    
    def reset_board(self) -> None:
        self.board = [[False for _ in row] for row in self.number_board]

# %%
bingo_boards = []

board_data = []
for row in data[2:]:
    if row == '':   
        bingo_boards.append(BingoBoard(board_data))
        board_data = []
    else:
        board_data.append(row.split(' '))

# %%
bingo_boards[0].number_board
# %%
bingo_boards[0].board
# %%
winner_found = False
winner_board = None

for board in bingo_boards:
    board.reset_board()

for i, draw in enumerate(draws):
    print(i)
    for bingo_board in bingo_boards:
        bingo_board.mark_number(draw)
        if bingo_board.bingo():
            print(bingo_board.number_board)
            print(bingo_board.board)
            print(draw)
            winner_found = True
            winner_board = bingo_board
            break
    if winner_found:
        break
# %%
def calc_unmarked_sum(board):
    unmarked_sum = 0

    for i, row in enumerate(board.board):
        for j, number in enumerate(row):
            if not number:
                unmarked_sum += int(board.number_board[i][j])
    
    return unmarked_sum

# %%
int(draw) * calc_unmarked_sum(winner_board)
# %%
winner_count = 0
last_winner = None

for board in bingo_boards:
    board.reset_board()

for i, draw in enumerate(draws):
    print(i, draw)
    for bingo_board in bingo_boards:
        if bingo_board.bingo():
            continue
        bingo_board.mark_number(draw)
        if bingo_board.bingo():
            winner_count += 1
            if winner_count == len(bingo_boards):
                last_winner = bingo_board
                break
    if last_winner:
        break
# %%
last_winner.board

# %%
last_winner.number_board

# %%
int(draw) * calc_unmarked_sum(last_winner)
# %%
