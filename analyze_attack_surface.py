import networkx as nx
from itertools import combinations

def calculate_attack_surface(graph, start_nodes, target_nodes, p):
    total_sum = 0
    for s in start_nodes:
        for t in target_nodes:
            for path in nx.all_simple_paths(graph, s, t):
                path_length = len(path) - 1
                total_sum += p ** path_length
    return total_sum

def calculate_attack_surface_probability(graph, start_nodes, target_nodes, p):
    probabilities = []
    for s in start_nodes:
        for t in target_nodes:
            for path in nx.all_simple_paths(graph, s, t):
                path_length = len(path) - 1
                probabilities.append(p ** path_length)
    return calculate_union(probabilities)

def calculate_union(probabilities):
    union = 0
    for i in range(1, len(probabilities) + 1):
        for j in combinations(probabilities, i):
            product = 1
            for s in j:
                product *= s
            if i % 2 == 1:
                union += product
            else:
                union -= product
    return union
