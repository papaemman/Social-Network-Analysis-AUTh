import networkx as nx


def read_file(filename="email.txt"):

    G = nx.Graph()
    f = open(filename, 'r')

    for line in f:
        line = line.split()

        G.add_node(line[0])
        G.add_node(line[1])
        G.add_edge(line[0], line[1])
    graph = nx.convert_node_labels_to_integers(G, label_attribute="ID")
    return graph


def karate_club():
    return nx.karate_club_graph()
