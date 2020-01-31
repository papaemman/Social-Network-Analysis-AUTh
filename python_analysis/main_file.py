from python_analysis import file_handling
from python_analysis import chen_im_algorithms, CELF
from python_analysis.celfpp import celf_pp
from python_analysis.simulation import IC, LT

"""
###     0. Configuration
"""
seeds_number = 50
R = 1000
filename = "mention_retweet_graph.txt"
# For Linear Threshold Model use "LT"
# For Independent Cascade Model use "IC"
im_model = "IC"

"""
###     1. Reading the graph
"""
# file_handling.csv_to_txt("mention_retweet_graph.csv", "mention_retweet_graph.txt")
G = file_handling.read_file(filename)
# G = file_handling.test_example()

"""
###     2. Details of dataset
"""

# dataset_detail.run_details(G)

"""
###     3. Influence Maximization algorithms
"""

chen_im_algorithms.im_algorithms(G, seeds_number, im_model)

# gga = general_greedy(G, seeds_number, R)
# print("Result of GeneralGreedy ",  gga)

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

total = 0
k = IC.independent_cascade(G, celf[0])
for i in k:
    print(i)
    total += len(i)
print("Total nodes that activated with IC model: %d" % total)


print("==========================================")
print("Simulation based on Linear Threshold")

total = 0
k = LT.linear_threshold(G, celf[0])
for i in k:
    print(i)
    total += len(i)
print("Total nodes that activated with LT model: %d" % total)
