from memeplex import partition_memeplexes, select_submemeplex, get_local_best, get_worst, improve_submemeplex
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


# Reads input
fixed, max_solutions = read_input()

F = 0           # total frogs
M = 0           # memeplexes
Q = 0           # submemeplex size
N = 0           # evolution steps
S = 0           # number of times the memeplexes are shuffled

assert S * N * M <= max_solutions

# Initialize F new frogs
all_frogs = [Frog(fixed) for _ in range(F)]

for _ in range(S): 
   # SFLA
   memeplexes, global_best = partition_memeplexes(all_frogs)
   for m in memeplexes:                   # For each memeplex
      for _ in range(N):                     # For each evolution step
         sub_meme = select_submemeplex(m, Q)    
         local_best = get_local_best(sub_meme)
         local_worst = get_worst(sub_meme)

         # Makes frog better
         if not improve_submemeplex(sub_meme, global_best, local_best, local_worst):
            local_worst = Frog(fixed)

   all_frogs = [item for sublist in memeplexes for item in sublist]


