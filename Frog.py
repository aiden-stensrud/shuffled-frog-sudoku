import random

class Frog:
    def __init__(self, fixed: list, id = None):
        self.random_grid(fixed)
        self.key = None
        self.coll = None
        self.row_colls = [0, 0, 0]
        self.col_colls = [0, 0, 0]
        self.id = id

        self.evaluate()


    def random_grid(self, fixed: list):
        self.board = [[0] * 9 for _ in range(9)]

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
                        self.board[row][col] = fixed[row][col]
                        count += 1
                    else:
                        self.board[row][col] = arr[k - count]


    def evaluate(self):
        # count collisions
        collisions = 0

        for i in range(9):
            unique_row = set()
            unique_col = set()
            for j in range(9):
                unique_row.add(self.board[i][j])
                unique_col.add(self.board[j][i])
            collisions += (9 - len(unique_row)) + (9 - len(unique_col))

            # update the collisions per 3 rows/columns
            self.row_colls[i // 3] += 9 - len(unique_row)
            self.col_colls[i // 3] += 9 - len(unique_col)

        self.coll = collisions
   


    def print_board(self):
        for i in range(9):
            for j in range(9):
                print(self.board[i][j], end = " ")
                if (j + 1) % 3 == 0 and j != 8:
                    print("|", end = " ")
                
            print()
            if (i + 1) % 3 == 0 and i != 8:
                print("---------------------")

        print()
        print(eval(self.board))
        print()


    # key used for constructing a submemeplex
    def set_key(self, weight):
       self.key = random.random() ** weight


    def __lt__(self, other: "Frog"):
        return self.key < other.key

