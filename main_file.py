from src.functions import file_handling
from src.functions import chen_im_algorithms, CELF
from src.functions import celfpp
from src.functions import IC, LT

"""
###     0. Configuration
"""
seeds_number = 50
R = 1000
filename = "mention_retweet_graph.txt"


"""
###     1. Reading the graph
"""
# To recreate data files(csv) as txt uncomment the following lines
# file_handling.csv_to_txt("mention_retweet_graph.csv", "mention_retweet_graph.txt")
# file_handling.csv_to_txt("retweet_graph.csv", "retweet_graph.txt")

G = file_handling.read_file(filename)
# G = file_handling.test_example()

"""
###     2. Details of dataset
"""

# dataset_detail.run_details(G)

"""
###     3. Influence Maximization algorithms
"""

# gga = general_greedy(G, seeds_number, R)
# print("Result of GeneralGreedy ",  gga)

newGreedy, degree_discount_ic_seeds, degree_discount_seeds, simpath_seeds = chen_im_algorithms.im_algorithms(G, seeds_number)

celf = CELF.celf(G, seeds_number)
print("Result of CELF: ",  celf)

## TODO doesn't work
# celfpp = celf_pp(G, seeds_number)
# print("Result of CELF++: ",  celf)


"""
###     4. Simulate seed results
"""

print("==========================================")
print("Simulation based on Independent Cascade")

# CELF
celf_total = 0
k = IC.independent_cascade(G, celf[0])
for i in k:
    print(i)
    celf_total += len(i)
print("Total nodes that activated with CELF algorithm in IC model: %d" % celf_total)

# General Greedy
gga_total = 0
k = IC.independent_cascade(G, gga)
for i in k:
    print(i)
    gga_total += len(i)
print("Total nodes that activated with General Greedy in IC model: %d" % gga_total)


# Degree discount
dd_ic_total = 0
k = IC.independent_cascade(G, degree_discount_ic_seeds)
for i in k:
    print(i)
    dd_ic_total += len(i)
print("Total nodes that activated with Degree Discount in IC model: %d" % dd_ic_total)


## TODO    Na dw o simpath se ti montelo trexei

print("==========================================")
print("Simulation based on Linear Threshold")

dd_total = 0
k = LT.linear_threshold(G, degree_discount_seeds)
for i in k:
    print(i)
    dd_total += len(i)
print("Total nodes that activated with Degree Discount in LT model: %d" % dd_total)
