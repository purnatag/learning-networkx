import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

edge_list = [(0,6), (1,6), (2,7), (3,7), (4,8), (5,8), (6,9), (7,9), (8,9)]
G.add_edges_from(edge_list)
labels = {}
labels[0] = r"$x$"
labels[1] = r"$y$"
labels[2] = r"$y$"
labels[3] = r"$z$"
labels[4] = r"$z$"
labels[5] = r"$x$"
labels[6] = r"$X$"
labels[7] = r"$X$"
labels[8] = r"$X$"
labels[9] = r"$+$"

pos = nx.spring_layout(G, seed=3113795652)

nx.draw_networkx_nodes(G, pos, node_size=500, node_color="yellow")
nx.draw_networkx_edges(G, pos, width=1)
nx.draw_networkx_labels(G, pos, font_size=14, labels=labels)

plt.show()