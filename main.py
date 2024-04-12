import networkx as nx
from networkx.algorithms.isomorphism.isomorph import graph_could_be_isomorphic as isomorphic

# Create an example graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4)])

# Function to find automorphisms
def find_automorphisms(graph):
    automorphisms = []
    for perm in nx.aut_iso.enumerate(G):
        mapping = perm.mapping
        if nx.is_isomorphic(graph, nx.relabel_nodes(graph, mapping)):
            automorphisms.append(mapping)
    return automorphisms

# Find automorphisms
automorphisms = find_automorphisms(G)

# Print the automorphisms
if automorphisms:
    print("Automorphisms found:")
    for idx, automorphism in enumerate(automorphisms):
        print(f"Automorphism {idx + 1}: {automorphism}")
else:
    print("No automorphisms found.")
