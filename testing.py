from Frog import Frog
import util, memeplex

M = 50
F = 1000
E_steps = 1

frogs = []
default_board = util.read_board('.9.2.1.....4..8.7..7..69..814...58...6.....2...86...472..34..6..3.1..7.....8.2.1.')
for i in range(F):
    frogs.append(Frog(default_board, i))

frogs.sort(key = lambda Frog: Frog.coll)

plexes = memeplex.partition_memeplexes(frogs, M)


for frog in plexes[0]:
    print(frog.coll)

print()
for i in range(5):
    sub, _, _ = memeplex.select_submemeplex(plexes[0], 5)
    sub.sort(key = lambda Frog: Frog.coll)
    for frog in sub:
        print(frog.coll)
    print()


