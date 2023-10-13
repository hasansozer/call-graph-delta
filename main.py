import networkx as nx
import gmatch4py as gm
import time
import json
import matplotlib.pyplot as plt
import os

from analyze_attack_surface import calculate_attack_surface
from analyze_delta import render_delta
from read_config import read_config

config_file_path = "config-ansible.json"
graph_objects = []
entry_nodes = []
target_nodes = []

def load_directed_graph_from_json(json_filename, entry_names, target_names):
    with open(json_filename, 'r') as json_file:
        data = json.load(json_file)
    graph = nx.DiGraph()
    entry_nodes.clear()
    target_nodes.clear()
    for node, neighbors in data.items():
        for name in entry_names:
            if name in node:
                entry_nodes.append(node)
        for name in target_names:
            if name in node:
                target_nodes.append(node)
        graph.add_node(node)
        graph.add_edges_from((node, neighbor) for neighbor in neighbors)
    return graph

# plot distances
def plot_values(values):
    plt.plot(values, marker='o')
    plt.title('Edit Distance between Consecutive Graphs')
    plt.xlabel('Graph Pair Index')
    plt.ylabel('Edit Distance')
    plt.xticks(range(len(values)), range(1, len(values) + 1))
    plt.grid(True)
    plt.show()

def calculate_tree_impurity(graph):
    n = graph.number_of_nodes()
    e = graph.number_of_edges()
    print("n ", n, " e ", e)

    if n <= 2:
        raise ValueError("Number of nodes should be greater than 2 for tree impurity calculation.")

    impurity = 2 * (e - n + 1) / ((n - 1) * (n - 2))
    return impurity

if __name__ == "__main__":

    edit_distances = []
    attack_surfaces =[]
    impurities = []

    file_paths, entry_names, target_names = read_config(config_file_path)

    print("File Paths:")
    for path in file_paths:
        print(path)

    print("\nFunction Names:")
    print("entry:", entry_names)
    print("target:", target_names)

    for file_path in file_paths:
        graph = load_directed_graph_from_json(file_path, entry_names, target_names)
        print(file_path)
        graph_objects.append(graph)
        impurity = calculate_tree_impurity(graph)
        impurities.append(impurity)
        if entry_nodes and target_nodes:
            surface = calculate_attack_surface(graph, entry_nodes, target_nodes, 0.5)
            print("e ", len(entry_nodes), " t ", len(target_nodes), " s ", surface)

    for i in range(len(graph_objects) - 1):
        ged = gm.GraphEditDistance(0, 1, 0, 1)  # all edit costs are equal to 1
        result = ged.compare([graph_objects[i], graph_objects[i+1]], None)
        distance = ged.similarity(result)
        #impurity = calculate_tree_impurity(graph_objects[i])
        print("d ", distance[1][0])
        edit_distances.append(distance[1][0])
        #impurities.append(impurity)

    #plot_values(attack_surfaces)

    #render_delta(graph_objects[1], graph_objects[2])

