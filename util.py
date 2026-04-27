import random, heapq
from Frog import Frog

# generates a standard sudoku board that has self-consistent 3x3 boxes
def generate_board(fixed: list):
    board = [[0] * 9 for _ in range(9)]

    for i in range (0, 9, 3):
        for j in range(0, 9, 3):
            nine = set(range(1, 10))
            for k in range(9):
                row = i + (k // 3)
                col = j + (k % 3)
                if fixed[row][col] != 0 and fixed[row][col] in nine:
                    nine.remove(fixed[row][col])
            
            arr = list(nine)
            random.shuffle(arr)
            count = 0
            for k in range(9):
                row = i + (k // 3)
                col = j + (k % 3)
                if fixed[row][col] != 0:
                    board[row][col] = fixed[row][col]
                    count += 1
                else:
                    board[row][col] = arr[k - count]
                
    return board


'''
Swap will swap the 3x3 blocks given as a list argument labeled as:

1|2|3
-----
4|5|6
-----
7|8|9
'''
def swap(copy, target, swaps: list):
    # create a new board since we may not use the changed one
    result = Frog()
    result.board = copy_board(target.board)
    for swap in swaps:
        # top left corner of the given 3x3
        row = 3 * ((swap - 1) // 3)
        col = 3 * ((swap - 1) % 3)
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                result.board[i][j] = copy.board[i][j]

    return result


# reads a sudoku board from a given 81 digit number
def read_board(board_str: str):
    board = [[0] * 9 for _ in range(9)]

    for i in range(9):
        for j in range(9):
            c = board_str[i * 9 + j]
            if c != ".":
                board[i][j] = int(c)

    return board


def subplex(plex: list, q: int):
    subplex = []
    n = len(plex)
    for j in range(n):
        plex[j].set_key(2 * (n + 1 - j) / (n * (n + 1)))

    pq = heapq.heapify_max(plex)

    for _ in range(q):
        subplex.append(pq.heappop_max())
    
    return subplex


def copy_board(original):
    copy = [[0] * 9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            copy[i][j] = original[i][j]

    return copy


def print_board(board: list):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end = " ")
            if (j + 1) % 3 == 0 and j != 8:
                print("|", end = " ")
            
        print()
        if (i + 1) % 3 == 0 and i != 8:
            print("---------------------")

    print()
    print(eval(board))
    print()


def main():
    boards = list()
    boards.append(read_board('327951864195684372846723915659472138471538296283169547738216459962345781514897623'))
            

    default_board = '.9.2.1.....4..8.7..7..69..814...58...6.....2...86...472..34..6..3.1..7.....8.2.1.'
    boards.append(generate_board(read_board(default_board)))
    if len(boards) >= 2:
        changed = swap(boards[0], boards[1], (1, 2, 3))
        boards.append(changed)
    for board in boards:
        print_board(board)


#main()