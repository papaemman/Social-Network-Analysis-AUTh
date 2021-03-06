from src.functions import file_handling
from src.functions import chen_im_algorithms, CELF
from src.functions import IC, LT
from src.functions import GeneralGreedy
import networkx as nx
import time
from networkx.algorithms.community import greedy_modularity_communities
"""
###     0. Configuration
"""
seeds_number = 15
R = 10
filename = "mention_graph.txt"


"""
###     1. Reading the graph
"""
# To recreate data files(csv) as txt uncomment the following lines
# file_handling.csv_to_txt("./data/processed/mention_graph1.csv", "mention_graph.txt")
# file_handling.csv_to_txt("./data/processed/retweet_graph1.csv", "retweet_graph.txt")

G = file_handling.read_file(filename)
# G = file_handling.test_example()
#G = file_handling.karate_club()

# """
# ###     2. Details of dataset
# """
#
# # dataset_detail.run_details(G)

"""
###     3. Influence Maximization algorithms
"""
print("============= IM algorithms running ==============")
time_start_greedy = time.time()
gga = GeneralGreedy.general_greedy(G, seeds_number, r=R)
time_end_greedy = time.time()
print("GeneralGreedy algorithm seed set: ",  gga)
print("in time: %f" % (time_end_greedy - time_start_greedy))

# simpath_seeds
newGreedy, degree_discount_ic_seeds, degree_discount_seeds = chen_im_algorithms.im_algorithms(G, seeds_number, R=R)

time_start_celf = time.time()
celf = CELF.celf(G, seeds_number, n_iters=R)
time_end_celf = time.time()
print("CELF seed set: ",  celf[0])
print("in time: %f" % (time_end_celf - time_start_celf))

## TODO doesn't work
# celfpp = celf_pp(G, seeds_number)
# print("Result of CELF++: ",  celf)
print("============= IM algorithms finish ==============")
print()

"""
###     4. Simulate seed results
"""

print("==========================================")
print("Simulation based on Independent Cascade")
print()

# General Greedy
gga_total = 0
k = IC.independent_cascade(G, gga)
for i in k:
    print(i)
    gga_total += len(i)
print("Total nodes that activated with General Greedy in IC model: %d" % gga_total)

# newGreedy
new_ga_total = 0
k = IC.independent_cascade(G, newGreedy)
for i in k:
    new_ga_total += len(i)
print("Total nodes that activated with newGreedy in IC model: %d" % new_ga_total)

# CELF
celf_total = 0
k = IC.independent_cascade(G, celf[0])
for i in k:
    celf_total += len(i)
print("Total nodes that activated with CELF algorithm in IC model: %d" % celf_total)


# Degree discount IC
dd_ic_total = 0
k = IC.independent_cascade(G, degree_discount_ic_seeds)
for i in k:
    dd_ic_total += len(i)
print("Total nodes that activated with Degree Discount in IC model: %d" % dd_ic_total)


print("==========================================")
print("Simulation based on Linear Threshold")
print()

dd_total = 0
k = LT.linear_threshold(G, degree_discount_seeds)
for i in k:
    dd_total += len(i)
print("Total nodes that activated with Degree Discount in LT model: %d" % dd_total)

time_our1 = time.time()

G2 = nx.to_directed(G)
bet = nx.betweenness_centrality(G2)
bet2 = ({k: v for k, v in sorted(bet.items(), key=lambda item: item[1], reverse=True)[:seeds_number]})
myList = list(bet2.keys())
print(myList)
time_our2 = time.time()
print("Total time was: ", time_our2 - time_our1)
our_total = CELF.monte_carlo(G2,seed_set=myList[:-1],node=myList[-1],R=R)


print("Total nodes = ", our_total)

C = list(greedy_modularity_communities(G,weight=None))
print(len(C))

