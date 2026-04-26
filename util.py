import random, heapq

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


# returns the number of collisions
def eval(board: list):
    collisions = 0

    for i in range(9):
        uniqueRow = set()
        uniqueCol = set()
        for j in range(9):
            uniqueRow.add(board[i][j])
            uniqueCol.add(board[j][i])
        collisions += (9 - len(uniqueRow)) + (9 - len(uniqueCol))


    return collisions


'''
Swap will swap the 3x3 blocks given as a list argument labeled as:

1|2|3
-----
4|5|6
-----
7|8|9
'''
def swap(copy: list, target: list, swaps: list):
    # create a new board since we may not use the changed one
    result = copy_board(target)
    for swap in swaps:
        # top left corner of the given 3x3
        row = 3 * ((swap - 1) // 3)
        col = 3 * ((swap - 1) % 3)
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                result[i][j] = copy[i][j]

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


def copy_board(original: list):
    copy = [[0] * 9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            copy[i][j] = original[i][j]

    return copy


def main():
    boards = list()
    try:
        with open("valid boards.txt") as f:
            for line in f:
                boards.append(read_board(line))
    except:
        print("cant find file")
            

    default_board = '.9.2.1.....4..8.7..7..69..814...58...6.....2...86...472..34..6..3.1..7.....8.2.1.'
    boards.append(generate_board(read_board(default_board)))
    if len(boards) >= 2:
        changed = swap(boards[0], boards[1], (1, 2, 3))
        boards.append(changed)
    for board in boards:
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


main()

