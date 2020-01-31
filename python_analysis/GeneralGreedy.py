""" General Greedy Algorithm
This algorithm performs in O(knRm)
"""


def general_greedy(graph, budget, r=10000):
    seed_set = []

    # For the number of budget
    for i in range(0, budget):
        best_node = -1
        best_spread = -1

        for node in graph.nodes():
            s = 0
            if node not in seed_set:
                s = independent_cascade(graph, seed_set, node, r)
                if s > best_spread:
                    best_spread = s
                    best_node = node
        seed_set.append(best_node)
        print(best_node)

    return seed_set


def independent_cascade(G, S, node, p=0.1, r=10000):
    from copy import deepcopy
    from random import random
    T = deepcopy(S)
    T.append(node)

    active_nodes = T[:]
    for i in range(r):
        while active_nodes.__len__() > 0:
            new_active_nodes = []
            for u in active_nodes:
                for v in G.neighbors(u):
                    if v not in T:
                        if random() <= p:
                            T.append(v)
                            new_active_nodes.append(v)
            active_nodes = deepcopy(new_active_nodes)

    return len(T) / r
