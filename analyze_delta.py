import networkx as nx
from networkx.algorithms import graph_edit_distance

from Graph import Graph

def parse_dot_file(dot_file):
    G = nx.DiGraph()

    with open(dot_file, 'r') as f:
        for line in f:
            if '->' in line:
                parts = line.strip().split('->')
                source = parts[0].strip()
                target = parts[1].split(';')[0].strip()
                G.add_edge(source, target)

    return G

# Define a function to filter out nodes with undesired labels
def filter_node(node_label):
    if node_label.startswith('__') or 'python_library' in node_label:
        return False
    return True

def get_delta_graph(G1, G2):
    delta_nodes = set(G2.nodes()) - set(G1.nodes())
    delta_edges = set(G2.edges()) - set(G1.edges())

    highlighted_G = G1.copy()

    for node in delta_nodes:
        highlighted_G.add_node(node, color='red')

    for edge in delta_edges:
        src, dst = edge
        highlighted_G.add_edge(src, dst, color='red')

    return highlighted_G

def prune_uncolored_nodes(G):
    colored_nodes = [node for node, data in G.nodes(data=True) if 'color' in data and data['color'] == 'red']
    filtered_nodes = [node for node in colored_nodes if filter_node(node)]
    return G.subgraph(filtered_nodes)

def analyze_and_render_delta(dot_file1, dot_file2):
    G1 = parse_dot_file(dot_file1)
    G2 = parse_dot_file(dot_file2)

    edit_distance = graph_edit_distance(G1, G2)
    print(f"Edit Distance: {edit_distance}")

    DG = get_delta_graph(G1, G2)
    g = Graph(DG)
    g.save_graph('delta')
    g.render_graph()

def render_delta(G1, G2):
    DG = get_delta_graph(G1, G2)
    g = Graph(prune_uncolored_nodes(DG))
    g.save_graph('delta-pruned')
    g.render_graph()
