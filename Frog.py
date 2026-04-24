import random

class Frog:
   def __init__(self, fixed: list):
      self.board = self.random_grid(fixed)

   def random_grid(self, fixed: list):
      self.board = [[0] * 9 for _ in range(9)]

      for i in range (0, 9, 3):
         for j in range(0, 9, 3):
            if fixed[i][j] != 0:
                  self.board[i][j] = self.fixed[i][j]
                  continue
            arr = list(range(1, 10))
            random.shuffle(arr)
            for k in range(9):
                  row = i + (k // 3)
                  col = j + (k % 3)
                  self.board[row][col] = arr[k]


   def evaluate(self):
      # count collisions
      collisions = 0

      for i in range(9):
         uniqueRow = set()
         uniqueCol = set()
         for j in range(9):
            uniqueRow.add(self.board[i][j])
            uniqueCol.add(self.board[j][i])
         collisions += (9 - len(uniqueRow)) + (9 - len(uniqueCol))

      return collisions

