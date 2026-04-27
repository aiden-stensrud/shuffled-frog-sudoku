from memeplex import partition_memeplexes, select_submemeplex, improve_submemeplex
from Frog import Frog



def read_input():
   board_string = input()
   solutions = int(input())

   board = []
   index = 0
   for row in range(9):
      board_row = []
      for col in range(9):
         char = board_string[index]

         if char == '.':
            board_row.append(0)
         else: 
            board_row.append(int(char))
         index += 1

      board.append(board_row)
   return board, solutions

def SFLA(F, M, Q, N, S, fixed):

   # Initialize F new frogs
   all_frogs = [Frog(fixed) for _ in range(F)]
   global_best = None

   for _ in range(S): 
      memeplexes, global_best = partition_memeplexes(all_frogs, M)

      if global_best.coll == 0:
         return global_best

      for m in memeplexes:                   # For each memeplex
         for _ in range(N):                     # For each evolution step
            sub_meme, local_best, local_worst = select_submemeplex(m, Q)

            # Makes frog better
            if not improve_submemeplex(sub_meme, global_best, local_best, local_worst):
               local_worst.random_grid(fixed)
               local_worst.evaluate()
            
            if local_worst.coll == 0:
               return local_worst

            m.sort(key = lambda Frog: Frog.coll)

      all_frogs = [item for sublist in memeplexes for item in sublist]

   return global_best


# Reads input
fixed, max_solutions = read_input()

F = 1000           # total frogs
M = 50           # memeplexes
Q = 10           # submemeplex size
N = 9           # evolution steps
S = 20           # number of times the memeplexes are shuffled

assert S * N * M + F <= max_solutions

# Run the main algorithm
best_solution = SFLA(F, M, Q, N, S, fixed)

# Prints the output
best_solution.print_board()
