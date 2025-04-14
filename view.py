import networkx as nx
import matplotlib.pyplot as plt

def desenhar_grafo(grafo, caminho_hamiltoniano=None, output_file="assets/grafo.png"):
    G = nx.Graph()

    for vertice, vizinhos in grafo.items():
        for vizinho in vizinhos:
            G.add_edge(vertice, vizinho)

    pos = nx.spring_layout(G)  
    nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=500, font_size=10)

    if caminho_hamiltoniano:
        edges = [(caminho_hamiltoniano[i], caminho_hamiltoniano[i + 1]) for i in range(len(caminho_hamiltoniano) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color="red", width=2)

    plt.savefig(output_file)
    plt.show()


if __name__ == "__main__":
    grafo = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1, 3],
        3: [1, 2]
    }

    caminho_hamiltoniano = [0, 1, 3, 2]

    desenhar_grafo(grafo, caminho_hamiltoniano)