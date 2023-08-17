from graphviz import Digraph

class Graph:
    def __init__(self, G):
        self.dot = Digraph(format='png')
        for node, attrs in G.nodes(data=True):
            color = attrs.get('color', None)
            self.dot.node(node, color=color)

        for src, dst, attrs in G.edges(data=True):
            color = attrs.get('color', None)
            self.dot.edge(src, dst, color=color)

    def save_graph(self, filename):
        self.filename = filename
        self.dot.save(filename + ".dot")

    def render_graph(self):
        self.dot.render(self.filename + ".png", view=True)