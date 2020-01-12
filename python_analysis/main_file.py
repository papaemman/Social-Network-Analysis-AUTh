
import networkx as nx
from python_analysis.GeneralGreedy import general_greedy
from python_analysis import file_handling, dataset_detail

"""
    0. Configuration
"""
seeds_number = 10
filename = "email.txt"

"""
    1. Reading the graph
"""

G = file_handling.karate_club()

"""
###     2. Details of dataset
"""

dataset_detail.run_details(G)


"""
###     2. Greedy algorithm
"""
gga = general_greedy(G, seeds_number, r=10000)
print("Result of GeneralGreedy ",  gga)


"""
###     3. New Greedy algorithm
"""




"""
###     CELF Optimization improves performance about 700 times faster than
###     the greedy algorithm but still need much time to complete a task.
"""