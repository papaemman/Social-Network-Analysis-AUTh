from random import randint
from numpy import array, dot, zeros, diag, ones, int
from numpy.linalg import inv, det

import time

STEPS = 6
NODES = 1000
BUDGET = 100


def create_adjacency(nodes):
    adjacency = zeros((nodes, nodes))
    for i in range(nodes):
        for j in range(nodes):
            if i == j:
                adjacency[i][j] = 0
            else:
                x = randint(0, 10)
                if x < 2:
                    adjacency[i][j] = -1
                elif x > 8:
                    adjacency[i][j] = 1
                else:
                    adjacency[i][j] = 0
    return adjacency


def svim(number_of_nodes, t, p):
    c = ones(number_of_nodes).transpose()
    for i in range(t):
        c = dot(c, p)
    return c


def stochastic(adj):

    d = zeros((len(adj)))
    for i in range(len(adj)):
        for j in range(len(adj)):
            d[i] += abs(adj[i][j])
    D = diag(d)
    y = det(D)
    d_1 = inv(D)

    return dot(adj, d_1), d


def bubbleSort(arr, id):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

                id[j], id[j+1] = id[j+1], id[j]



steps = STEPS
number_of_nodes = NODES
budget = BUDGET
state_of_node = [number_of_nodes]
seed_set = zeros(budget)

adj = create_adjacency(number_of_nodes)
time_start = time.time()
p, d = stochastic(adj)
c = svim(number_of_nodes, steps, p)

# Sort array
sorted = ones(number_of_nodes)
for i in range(len(c)):
    sorted[i] = i
bubbleSort(c, sorted)

for i in range(budget):
    seed_set[i] = sorted[number_of_nodes-i-1]
time_end = time.time()
print("================================")
# print(seed_set)
print("SVIM-S running time: %f" % (time_end-time_start))


def Nmaxelements(list1, N):
    final_list = []

    for i in range(0, N):
        max1 = 0
        max2 = 0

        for j in range(len(list1)):
            if list1[j] > max1:
                max1 = list1[j]
                max2 = j

        list1[max2] = -1
        final_list.append(max2)
    return final_list


# Heuristic
seed_set_heuristic = []
time1 = time.time()
seed_set_heuristic = Nmaxelements(list(d), budget)
time2 = time.time()
print("================================")
# print(seed_set_heuristic)
print("Heuristic running time: %f" % (time2-time1))


# Simulation

def simulation(seed):

    node_state = [-1]*number_of_nodes
    node_state_temp = [-1]*number_of_nodes
    probability_matrix = list(d)
    #seed_set = seed_set.astype(int)
    for i in range(len(seed)):
        node_state[seed[i]] = 1
        node_state_temp[seed[i]] = 1

    for t in range(steps):
        for i in range(number_of_nodes):
            # Random select of a neighbor
            neighbor = randint(0, probability_matrix[i])
            # Find neighbor and change state
            k = 0
            for j in range(number_of_nodes):
                if adj[i][j] != 0:
                    if k == neighbor:
                        if adj[j][i] > 0:
                            node_state_temp[i] = node_state[j]
                        else:
                            node_state_temp[i] = -node_state[j]
                    k += 1
        node_state = node_state_temp.copy()

    total = 0
    white_seeds = []
    for i in range(number_of_nodes):
        if node_state[i] == 1:
            white_seeds.append(i)
            total += 1
    return total, white_seeds


total, white_seeds = simulation(seed_set.astype(int))
print("+++++++++++++++++++ SVIMS ++++++++++++++++++++++++++")
print("Total number of white nodes: %d" % total)
print(white_seeds)


total, white_seeds = simulation(seed_set_heuristic)
print("+++++++++++++++++++ Heuristic ++++++++++++++++++++++++++")
print("Total number of white nodes: %d" % total)
print(white_seeds)
