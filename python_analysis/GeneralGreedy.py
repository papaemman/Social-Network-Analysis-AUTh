from math import floor,ceil
"""
    This algorithm performs in O(knRm)
"""


def general_greedy(graph, budget, r=20000):
    seed_set = []

    # For the number of budget
    for i in range(0, budget):
        for node in graph.nodes():
            if node not in seed_set:
                s = [0]*len(graph.nodes())
                for j in range(0, r):
                    s[node] += ran_cas(graph, seed_set, node)
                s[node] = s[node] / r

        seed_set.append(s.index(max(s)))
        print(max(s))

    return seed_set


def ran_cas(G, S, node, p=0.1):
    from copy import deepcopy
    from random import random
    T = deepcopy(S)
    T.append(node)

    active_nodes = T

    while active_nodes.__len__() > 0:
        new_active_nodes = []
        for u in active_nodes:
            for v in G.neighbors(u):
                if v not in T:
                    if random() <= p:
                        T.append(v)
                        new_active_nodes.append(v)
        active_nodes = new_active_nodes

    return T.__len__()
