import networkx as nx
import gmatch4py as gm
import time
import json
import matplotlib.pyplot as plt
from analyze_delta import render_delta

file_paths = [
    'C:/Users/hasans/PycharmProjects/pygraphdelta/callgraphs/fabric-2.4.0.json',
    'C:/Users/hasans/PycharmProjects/pygraphdelta/callgraphs/fabric-2.5.0.json',
    'C:/Users/hasans/PycharmProjects/pygraphdelta/callgraphs/fabric-2.6.0.json',
    'C:/Users/hasans/PycharmProjects/pygraphdelta/callgraphs/fabric-2.7.0.json',
    'C:/Users/hasans/PycharmProjects/pygraphdelta/callgraphs/fabric-2.7.1.json',
    'C:/Users/hasans/PycharmProjects/pygraphdelta/callgraphs/fabric-3.0.0.json',
    'C:/Users/hasans/PycharmProjects/pygraphdelta/callgraphs/fabric-3.0.1.json',
    'C:/Users/hasans/PycharmProjects/pygraphdelta/callgraphs/fabric-3.1.0.json',
]
#file_paths = [
#    'C:/Users/hasans/PycharmProjects/pygraphdelta/callgraphs/autojump-v22.3.1.json',
#    'C:/Users/hasans/PycharmProjects/pygraphdelta/callgraphs/autojump-v22.3.2.json',
#    'C:/Users/hasans/PycharmProjects/pygraphdelta/callgraphs/autojump-v22.3.3.json',
#    'C:/Users/hasans/PycharmProjects/pygraphdelta/callgraphs/autojump-v22.3.4.json',
#    'C:/Users/hasans/PycharmProjects/pygraphdelta/callgraphs/autojump-v22.3.5.json',
#    'C:/Users/hasans/PycharmProjects/pygraphdelta/callgraphs/autojump-v22.4.0.json',
#    'C:/Users/hasans/PycharmProjects/pygraphdelta/callgraphs/autojump-v22.4.1.json',
#    'C:/Users/hasans/PycharmProjects/pygraphdelta/callgraphs/autojump-v22.5.0.json',
#    'C:/Users/hasans/PycharmProjects/pygraphdelta/callgraphs/autojump-v22.5.1.json',
#    'C:/Users/hasans/PycharmProjects/pygraphdelta/callgraphs/autojump-v22.5.3.json'
#]
#file_paths = [
#    'C:/Users/hasans/PycharmProjects/pygraphdelta/callgraphs/asciinema-1.3.0.json',
#    'C:/Users/hasans/PycharmProjects/pygraphdelta/callgraphs/asciinema-1.4.0.json',
#    'C:/Users/hasans/PycharmProjects/pygraphdelta/callgraphs/asciinema-2.0.0.json',
#    'C:/Users/hasans/PycharmProjects/pygraphdelta/callgraphs/asciinema-2.0.1.json',
#    'C:/Users/hasans/PycharmProjects/pygraphdelta/callgraphs/asciinema-2.0.2.json',
#    'C:/Users/hasans/PycharmProjects/pygraphdelta/callgraphs/asciinema-2.1.0.json',
#    'C:/Users/hasans/PycharmProjects/pygraphdelta/callgraphs/asciinema-2.2.0.json',
#    'C:/Users/hasans/PycharmProjects/pygraphdelta/callgraphs/asciinema-2.3.0.json'
#]
graph_objects = []

def load_directed_graph_from_json(json_filename):
    with open(json_filename, 'r') as json_file:
        data = json.load(json_file)
    graph = nx.DiGraph()
    for node, neighbors in data.items():
        graph.add_node(node)
        graph.add_edges_from((node, neighbor) for neighbor in neighbors)
    return graph

# plot distances
def plot_distances(edit_distances):
    plt.plot(edit_distances, marker='o')
    plt.title('Edit Distance between Consecutive Graphs')
    plt.xlabel('Graph Pair Index')
    plt.ylabel('Edit Distance')
    plt.xticks(range(len(edit_distances)), range(1, len(edit_distances) + 1))
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    for file_path in file_paths:
        graph = load_directed_graph_from_json(file_path)
        print(file_path)
        graph_objects.append(graph)

    edit_distances = []
    for i in range(len(graph_objects) - 1):
        ged = gm.GraphEditDistance(0, 1, 0, 1)  # all edit costs are equal to 1
        result = ged.compare([graph_objects[i], graph_objects[i+1]], None)
        distance = ged.similarity(result)
        print(distance[1][0])
        edit_distances.append(distance[1][0])

    plot_distances(edit_distances)

    render_delta(graph_objects[1], graph_objects[2])

