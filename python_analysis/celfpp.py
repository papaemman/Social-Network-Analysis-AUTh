import heapq
from python_analysis.GeneralGreedy import independent_cascade

class Node:
    """
    Class that represents a node as the paper describes
    """
    def __init__(self, node):
        self.node = node
        self.mg1 = 0
        self.prev_best = None
        self.mg2 = 0
        self.flag = None
        self.list_index = 0


def celf_pp(graph, k):
    S = []      # Seed set initialize
    Q = heapq() # Contain nodes
    last_seed = None
    cur_best = None

    for u in graph.nodes():
        node = Node(u)
        node.mg1 = independent_cascade(graph, [], [node])
        node.prev_best = cur_best
        node.mg2 = independent_cascade(graph, [node], [cur_best])
        node.flag = 0

        cur_best = cur_best if cur_best and cur_best.mg1 > node.mg1 else node
        Q.push()