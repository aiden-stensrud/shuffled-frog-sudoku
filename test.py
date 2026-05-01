from Frog import Frog
from main import sfla, read_input

puzzles_to_test = 10

F = 1000         # total frogs
M = 10           # memeplexes
Q = F//M//2      # submemeplex size
N = 80          # evolution steps
S = 80          # number of times the memeplexes are shuffled


# Run the main algorithm
results = []
with open("puzzles.txt", "r") as f:
   for i in range(puzzles_to_test):
      print(f"Processing puzzle {i}")
      board_string = f.readline().strip()
      fixed = read_input(board_string)
      best_solution = sfla(F, M, Q, N, S, fixed)
      results.append(best_solution.coll)
      print(f"result for puzzle {i}: {best_solution.coll}")
avg = sum(results) // len(results)

print(f"\naverage from {puzzles_to_test} puzzles is: {avg}")
