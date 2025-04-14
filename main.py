from view import desenhar_grafo

def is_hamiltonian_path(grafo, caminho, visitado, vertice_atual, n):
    if len(caminho) == n:
        return True

    for vizinho in grafo[vertice_atual]:
        if not visitado[vizinho]:
            visitado[vizinho] = True
            caminho.append(vizinho)

            if is_hamiltonian_path(grafo, caminho, visitado, vizinho, n):
                return True

            caminho.pop()
            visitado[vizinho] = False

    return False


def encontre_o_caminho_hamiltoniano(grafo):
    n = len(grafo)  

    for inicio_vertice in range(n):
        visitado = [False] * n
        caminho = [inicio_vertice]
        visitado[inicio_vertice] = True

        if is_hamiltonian_path(grafo, caminho, visitado, inicio_vertice, n):
            return caminho

    return None


if __name__ == "__main__":
    grafo = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1, 3],
        3: [1, 2]
    }

    result = encontre_o_caminho_hamiltoniano(grafo)
    if result:
        print("Caminho Hamiltoniano encontrado:", result)
    else:
        print("Nenhum Caminho Hamiltoniano encontrado.")

    desenhar_grafo(grafo, result)