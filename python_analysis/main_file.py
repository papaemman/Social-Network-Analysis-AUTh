from python_analysis.GeneralGreedy import general_greedy
from python_analysis import file_handling, dataset_detail
from python_analysis import chen_im_algorithms, CELF

"""
###     0. Configuration
"""
seeds_number = 3
R = 1000
filename = "mention_retweet_graph.txt"
# For Linear Threshold Model use "LT"
# For Independent Cascade Model use "IC"
im_model = "LT"

"""
###     1. Reading the graph
"""
# file_handling.csv_to_txt("mention_retweet_graph.csv", "mention_retweet_graph.txt")
G = file_handling.read_file(filename)
# G = file_handling.test_example()

"""
###     2. Details of dataset
"""

dataset_detail.run_details(G)

"""
###     3. Influence Maximization
"""

# chen_im_algorithms.im_algorithms(G, seeds_number, im_model)

gga = general_greedy(G, seeds_number, R)
print("Result of GeneralGreedy ",  gga)

celf = CELF.celf(G, seeds_number)
print("Result of CELF ",  celf, 0.1, R)
