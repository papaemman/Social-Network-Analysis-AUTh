import networkx as nx
from networkx.algorithms import approximation


def details(graph):
    cliques_number = nx.graph_clique_number(graph)
    print("Number of cliques in the graph %d:" % cliques_number)
    clique = approximation.max_clique(graph)
    print("Maximum clique of the graph is: %.2d" % len(clique))
    print(clique)
    shortest_path = nx.shortest_path(graph)
    print("Shortest path: ", shortest_path)
    try:
        diameter = nx.diameter(graph)
        print("Diameter of the graph: %d" % diameter)
    except:
        print("Graph is not connected!")


def measures(graph):
    if nx.is_connected(graph):
        degree = nx.degree_centrality(graph)
        print("Degree centrality:\n", degree)

        closeness = nx.closeness_centrality(graph)
        print("Closeness centrality:%.f\n", closeness)

        betweenness_centrality = nx.betweenness_centrality(graph)
        print("Betweenness centrality:%.f\n", betweenness_centrality)


def cluster(graph):
    clusters = nx.algorithms.cluster.clustering(graph)
    print(clusters)


def community(graph):
    communities = nx.algorithms.community.greedy_modularity_communities(graph)
    print("Communities by modularity:")
    for com in communities:
        print(list(com))
    communities = nx.algorithms.community.asyn_lpa_communities(graph)
    print("Communities by asynchronous label propagation:")
    for com in communities:
        print(list(com))


def run_details(graph):
    details(graph)
    print("=================================")
    print("")
    measures(graph)
    print("=================================")
    print("")
    cluster(graph)
    print("=================================")
    print("")
    community(graph)
    print("=================================")
    print("")



