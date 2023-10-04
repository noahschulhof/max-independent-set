import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(edge_file, additional_edges = None):
    df = pd.read_csv(edge_file, header = None)

    edges = df.values.tolist()

    graph = nx.Graph()

    for edge in edges:
        graph.add_edge(edge[0], edge[1])

    pos = nx.spring_layout(graph, seed = 23456, k = 0.2)

    nx.draw(graph, pos, with_labels = True, node_color = 'lightblue', node_size=100, font_size=4)

    if additional_edges is not None:
        new_edges = []
        for i in range(len(additional_edges) - 1):
            new_edges.append((additional_edges[i], additional_edges[i + 1]))
        
        graph.add_edges_from(new_edges)
        nx.draw_networkx_edges(graph, pos, edgelist = new_edges, edge_color = 'red')
    
        ax = plt.gca()

        # Position and text content of the textbox
        x_pos = 0.5
        y_pos = 0.95
        textbox_text = additional_edges

        # Add the textbox to the Axes object
        ax.text(x_pos, y_pos, textbox_text, transform = ax.transAxes, fontsize = 14, color = 'red',
                bbox = dict(facecolor = 'white', edgecolor = 'black', boxstyle = 'round,pad = 0.5'), ha = 'center')

    return(plt)