""" General Greedy Algorithm
This algorithm performs in O(knRm)
"""
import src.functions.IC
# def general_greedy(graph, budget, r=3):
#     seed_set = []
#
#     # For the number of budget
#     for i in range(0, budget):
#         best_node = -1
#         best_spread = -1
#
#         for node in graph.nodes():
#             s = 0
#             if node not in seed_set:
#                 s = independent_cascade(graph, seed_set, node, r)
#                 if s > best_spread:
#                     best_spread = s
#                     best_node = node
#         seed_set.append(best_node)
#
#     return seed_set

def general_greedy(graph, budget, r=10000):
    seed_set = []

    # For the number of budget
    for i in range(0, budget):
        best_node = -1
        best_spread = -1

        for node in graph.nodes():
            s = 0
            if node not in seed_set:
                for i in range(r):
                    temp = src.functions.IC.independent_cascade(graph, seed_set)
                    total_spread = 0
                    for i in temp:
                        total_spread += len(i)
                    s += total_spread
                if s > best_spread:
                    best_spread = s
                    best_node = node
        seed_set.append(best_node)

    return seed_set


# def independent_cascade(G, S, node, p=0.1, r=3):
#     from copy import deepcopy
#     from random import random
#     count = 0
#
#     for i in range(r):
#         T = deepcopy(S)
#         T.append(node)
#         active_nodes = T[:]
#         while active_nodes.__len__() > 0:
#             new_active_nodes = []
#             for u in active_nodes:
#                 for v in G.neighbors(u):
#                     if (v not in T) and (v not in active_nodes):
#                         if random() <= p:
#                             T.append(v)
#                             new_active_nodes.append(v)
#             active_nodes = deepcopy(new_active_nodes)
#         count += len(T)
#     print(count / r)
#     return count / r
