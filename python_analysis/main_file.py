
from python_analysis.GeneralGreedy import general_greedy
from python_analysis import file_handling, dataset_detail
from python_analysis import chen_im_algorithms

"""
    0. Configuration
"""
seeds_number = 100
filename = "mention_retweet_graph.txt"
# For Linear Threshold Model use "LT"
# For Independent Cascade Model use "IC"
im_model = "LT"

"""
    1. Reading the graph
"""
file_handling.csv_to_txt("mention_retweet_graph.csv", "mention_retweet_graph.txt")
G = file_handling.read_file(filename)

"""
###     2. Details of dataset
"""

# dataset_detail.run_details(G)

"""
###     3. Influence Maximization
"""

chen_im_algorithms.im_algorithms(filename, seeds_number, im_model)

"""
###     2. Greedy algorithm
"""
# gga = general_greedy(G, seeds_number, r=10000)
# print("Result of GeneralGreedy ",  gga)

