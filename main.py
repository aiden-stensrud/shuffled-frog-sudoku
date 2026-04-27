from memeplex import partition_memeplexes, select_submemeplex, improve_submemeplex
from Frog import Frog

improve_by_local_count = 0
improve_by_global_count = 0
improve_by_random_count = 0

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

   total = 0
   for frog in all_frogs:
      total += frog.coll
   print(f"The average number of collisions per frog at the start is: {total//F}\n")

   global_best = None
   global improve_by_local_count
   global improve_by_global_count
   global improve_by_random_count

   for i in range(S): 
      memeplexes, global_best = partition_memeplexes(all_frogs, M)
      if i == 0: 
         print(f"Global best frog before evolution:")
         global_best.print_board()
      if global_best.coll == 0:
         return global_best

      for m in memeplexes:                   # For each memeplex
         for _ in range(N):                     # For each evolution step
            sub_meme, local_best, local_worst = select_submemeplex(m, Q)

            # Makes frog better
            did_local_improve, did_global_improve = improve_submemeplex(sub_meme, global_best, local_best, local_worst)
            if did_local_improve: improve_by_local_count += 1
            elif did_global_improve: improve_by_global_count += 1
            else:
               local_worst.random_grid(fixed)
               local_worst.evaluate()
               improve_by_random_count += 1
            
            if local_worst.coll == 0:
               return local_worst

            m.sort(key = lambda Frog: Frog.coll)

      all_frogs = [item for sublist in memeplexes for item in sublist]

   return global_best


# Reads input
fixed, max_solutions = read_input()

F = 1000           # total frogs
M = 10           # memeplexes
Q = F//M//2           # submemeplex size
N = 100          # evolution steps
S = 200          # number of times the memeplexes are shuffled

#assert S * N * M + F <= max_solutions

# Run the main algorithm
best_solution = SFLA(F, M, Q, N, S, fixed)

# Prints the output
print(f"Global best frog after evolution:")
best_solution.print_board()
print(f"improve by local count: {improve_by_local_count}")
print(f"improve by global count: {improve_by_global_count}")
print(f"improve by random count: {improve_by_random_count}")