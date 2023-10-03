import networkx as nx

def calculate_attack_surface(graph, start_nodes, target_nodes, p):
    total_sum = 0
    for s in start_nodes:
        for t in target_nodes:
            for path in nx.all_simple_paths(graph, s, t):
                path_length = len(path) - 1
                total_sum += p ** path_length
    return total_sum



