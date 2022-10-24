import grafos


def steiner_tree(grafo, vertices):
    gr = grafos.Grafo()
    
    visited = set()
    step(visited, grafo, vertices[0], gr, vertices)
    
    return gr


def step(visitados: set, grafo: grafos.Grafo, partida: int, grafo_res: grafos.Grafo, esperados: list) -> bool:
    possui_candidato = False

    if partida not in visitados:
        # print(partida)
        visitados.add(partida)
        for neighbour in grafo.saidas(partida):
            if neighbour[0] in visitados:
                continue

            viz_valido = False
            viz_valido = step(visitados, grafo, neighbour[0], grafo_res, esperados)
            if neighbour[0] in esperados:
                viz_valido = True

            if viz_valido:
                grafo_res.add_vertice(partida)
                grafo_res.add_vertice(neighbour[0])
                grafo_res.add_aresta(partida, neighbour[0], neighbour[1])
            
            if viz_valido:
                possui_candidato = True

    return possui_candidato


# -----------------------------------------------------------------------------

# print("GRAFO 1")
# grafo = grafos.g1
# vertices = [2, 4, 5]

# print("entrada")
# print(grafo)
# print("vertices")
# print(vertices)

# tree = steiner_tree(grafo, vertices)
# print("steiner tree")
# print(tree)


print("GRAFO 2")
grafo = grafos.g2
vertices = [5, 8, 6]

print("entrada")
print(grafo)
print("vertices")
print(vertices)

tree = steiner_tree(grafo, vertices)
print("steiner tree")
print(tree)