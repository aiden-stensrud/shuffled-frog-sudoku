from Frog import Frog
from util import swap
from copy import deepcopy
import random, heapq


# Partitions the list of frogs into M memeplexes round-robin style
def partition_memeplexes(frogs: list, M: int):
    plexes = []
    frogs.sort(key = lambda Frog: Frog.coll)
    for _ in range(M):
        plexes.append(list())

    counter = 0
    for frog in frogs:
        plexes[counter].append(frog)
        counter += 1
        counter %= M

    return plexes, plexes[0][0]


# Selects a submemeplex of size qbased on a triangular distribution
# using the Efraimidis-Spirakis algorithm for weighted sampling
def select_submemeplex(original: list, q: int):
    plex = deepcopy(original)
    subplex = []
    n = len(plex)
    for j in range(n):
        plex[j].set_key(2 * (n + 1 - j) / (n * (n + 1)))

    heapq._heapify_max(plex)
    best_frog = plex[0]
    worst_frog = plex[0]

    for _ in range(q):
        frog = heapq._heappop_max(plex)
        subplex.append(frog)
        if frog.coll < best_frog.coll:
            best_frog = frog
            
        if frog.coll > worst_frog.coll:
            worst_frog = frog
    
    return (subplex, best_frog, worst_frog)


# We try to improve the frog by taking the 3 rows or columns from the best frog
# that have the largest difference in collisions with the worst frog
def improve_frog(worst: Frog, best: Frog):
    # decide which parts of the frog to improve
    max_diff = 0
    to_swap = (0, 1)
    for i in range(3):
        if worst.row_colls - best.row_colls > max_diff:
            max_diff = worst.row_colls - best.row_colls
            to_swap = (i, 1)

    for i in range(3):
        if worst.col_colls - best.col_colls > max_diff:
            max_diff = worst.col_colls - best.col_colls
            to_swap = (i, 3)

    swaps = [to_swap[0] + x * to_swap[1] for x in range(3)]

    new_frog = swap(best, worst, swaps)
    new_frog.evaluate()
    return new_frog


# returns true if the worst frog was improved, otherwise returns false
def improve_submemeplex(subplex: list, global_best: Frog, local_best: Frog, worst: Frog):
    new_frog = improve_frog(worst, local_best)
    if new_frog.coll < worst.coll:
        worst.board = new_frog.board
        worst.evaluate()
        return True
    
    new_frog = improve_frog(worst, global_best)
    if new_frog.coll < worst.coll:
        worst.board = new_frog.board
        worst.evaluate()
        return True
    
    return False


def shuffle_memeplexes(plexes: list):
    pass

