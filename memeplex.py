from Frog import Frog
from util import swap
import random, heapq


# Partitions the list of frogs into M memeplexes round-robin style
def partition_memeplexes(frogs: list, M: int):
    plexes = []
    for _ in range(M):
        plexes.append(list())

    counter = 0
    for frog in frogs:
        plexes[counter].append(frog)
        counter += M
        counter %= M

    return plexes


# Selects a submemeplex of size qbased on a triangular distribution
# using the Efraimidis-Spirakis algorithm for weighted sampling
def select_submemeplex(plex: list, q: int):
    subplex = []
    n = len(plex)
    for j in range(n):
        plex[j].set_key(2 * (n + 1 - j) / (n * (n + 1)))

    pq = heapq.heapify_max(plex)
    best_frog = pq[0]
    worst_frog = pq[0]

    for _ in range(q):
        frog = pq.heappop_max()
        subplex.append(frog)
        if frog.collisions < best_frog.collisions:
            best_frog = frog
            
        if frog.collisions > worst_frog.collisions:
            worst_frog = frog
    
    return (subplex, best_frog, worst_frog)


def improve_frog(worst: Frog, best: Frog):
    # decide which part of the frog to improve
    swaps = [1, 2, 3]

    new_frog = swap(best, worst, swaps)
    new_frog.evaluate()
    return new_frog


# returns true if the worst frog was improved, otherwise returns false
def improve_submemeplex(subplex: list, global_best: Frog, local_best: Frog, worst: Frog):
    new_frog = improve_frog(worst, local_best)
    if new_frog.col < worst.col:
        worst = new_frog
        subplex.sort()
        return True
    
    new_frog = improve_frog(worst, global_best)
    if new_frog.col < worst.col:
        worst = new_frog
        subplex.sort()
        return True
    
    return False


def shuffle_memeplexes(plexes: list):
    pass