import networkx as nx
import os


def read_file(filename):

    G = nx.Graph()
    f = open(filename, 'r')

    for line in f:
        line = line.split()

        G.add_node(line[0])
        G.add_node(line[1])
        G.add_edge(line[0], line[1])
    graph = nx.convert_node_labels_to_integers(G, label_attribute="ID")
    return graph


def csv_to_txt(csv_file, txt_file):
    import csv
    G = nx.Graph()

    with open(os.path.abspath(csv_file)) as csv_file1:
        csv_reader = csv.reader(csv_file1, delimiter=',')
        line = 0
        for row in csv_reader:
            if line != 0:
                G.add_node(row[0])
                G.add_node(row[1])
                G.add_edge(row[0], row[1])
            line += 1

    with open(txt_file, "w") as my_output_file:
        with open(csv_file, "r") as my_input_file:
            my_output_file.write('%d %d' % (len(G.nodes), len(G.edges)))
            line = 0
            for row in G.edges():
                if line != 0:
                    my_output_file.write('\n' + row[0] + " " + row[1])
                line += 1
        my_output_file.close()


def karate_club():
    return nx.karate_club_graph()


def test_example():
    source = [0, 3, 3, 2, 3, 0, 3, 0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 4, 5]
    target = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9, 6, 7, 8, 9]
    graph = nx.DiGraph()
    for i in range(len(source)):
        graph.add_edge(source[i], target[i])
    return graph
