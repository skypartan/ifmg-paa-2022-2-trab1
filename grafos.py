class Grafo:

    def __init__(self) -> None:
        self.vertices = []
        self.arestas = []

    def add_vertice(self, nome):
        if nome in self.vertices:
            return

        self.vertices.append(nome)

    def add_aresta(self, vert1, vert2, peso):
        if vert1 not in self.vertices:
            print("vert1 não existe")
        if vert2 not in self.vertices:
            print("vert2 não existe")
        
        for a in self.arestas:
            if (vert1 == a[0] and vert2 == a[1]) or (vert1 == a[1] and vert2 == a[0]):
                return

        self.arestas.append((vert1, vert2, peso))

    def saidas(self, vertice):
        tmp = []

        for a in self.arestas:
            if a[0] == vertice:
                tmp.append((a[1], a[2]))
            if a[1] == vertice:
                tmp.append((a[0], a[2]))
        
        return tmp

    def __getitem__(self, item):
        return self.saidas(item)

    def __str__(self):
        msg = 'V = {0}:\n' + \
              'A = {1}'
        
        ft = '{\n'
        for a in self.arestas:
            ft += '({0}, {1}): {2},\n'.format(a[0], a[1], a[2])
        ft = ft + '  }'
        
        return msg.format(self.vertices, ft)


g1 = Grafo()
g1.add_vertice(1)
g1.add_vertice(2)
g1.add_vertice(3)
g1.add_vertice(4)
g1.add_vertice(5)
g1.add_vertice(6)
g1.add_aresta(1, 2, 3)
g1.add_aresta(2, 4, 2)
g1.add_aresta(2, 5, 1)
g1.add_aresta(2, 6, 5)
g1.add_aresta(3, 5, 7)
g1.add_aresta(3, 6, 1)
g1.add_aresta(4, 2, 2)
g1.add_aresta(4, 5, 4)
g1.add_aresta(5, 4, 4)
g1.add_aresta(5, 2, 1)
g1.add_aresta(5, 3, 7)
g1.add_aresta(6, 2, 5)
g1.add_aresta(6, 3, 1)

g2 = Grafo()
g2.add_vertice(1)
g2.add_vertice(2)
g2.add_vertice(3)
g2.add_vertice(4)
g2.add_vertice(5)
g2.add_vertice(6)
g2.add_vertice(7)
g2.add_vertice(8)
g2.add_vertice(9)
g2.add_aresta(1, 4, 3)
g2.add_aresta(2, 4, 5)
g2.add_aresta(2, 5, 2)
g2.add_aresta(2, 9, 5)
g2.add_aresta(3, 5, 3)
g2.add_aresta(4, 1, 3)
g2.add_aresta(4, 2, 5)
g2.add_aresta(4, 8, 7)
g2.add_aresta(5, 2, 2)
g2.add_aresta(5, 3, 3)
g2.add_aresta(5, 7, 9)
g2.add_aresta(5, 8, 2)
g2.add_aresta(6, 8, 4)
g2.add_aresta(6, 9, 3)
g2.add_aresta(7, 5, 9)
g2.add_aresta(8, 4, 7)
g2.add_aresta(8, 5, 2)
g2.add_aresta(8, 4, 6)
g2.add_aresta(9, 2, 5)
g2.add_aresta(9, 3, 6)


# la1 = {
#     1: [(2, 3)],
#     2: [],
#     3: [],
#     4: [],
#     5: [],
#     6: []
# }