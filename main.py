class Node:
    def __init__(self, key_, value_=None):
        self.key = key_
        self.value = value_

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)

    def __str__(self):
        return self.key


class NeighbourList:
    def __init__(self):
        self.graph = {}

    def is_empty(self):
        return self.graph == {}

    def insert_vertex(self, vertex):
        if vertex not in self.graph.keys():
            self.graph[vertex] = {}

    def insert_edge(self, vertex1, vertex2, edge=None):
        if vertex2 not in self.graph.keys():
            self.graph[vertex2] = {}
        self.graph[vertex1][vertex2] = edge
        self.graph[vertex2][vertex1] = edge

    def delete_edge(self, vertex1, vertex2):
        self.graph[vertex1].pop(vertex2)
        self.graph[vertex2].pop(vertex1)

    def delete_vertex(self, vertex):
        self.graph.pop(vertex)

        for key in self.graph:
            for key2 in self.graph[key]:
                i = None
                if key2 == vertex:
                    i = key2
                    self.graph[key].pop(i)
                    break

    def get_vertex(self,vertex_id):
        return vertex_id

    def vertices(self):
        return [k for k in self.graph]

    def neighbours(self, vertex_id):
        wynik = []
        for nghbr, edge in self.graph[vertex_id].items():
            wynik.append((nghbr, edge))
        return wynik


class NeighbourMatrix:
    def __init__(self):
        self.graph = [[]]
        self.vertex_list = []

    def is_empty(self):
        return self.graph == []

    def get_vertex(self,vertex_id):
        return self.vertex_list[vertex_id]

    def get_vertex_id(self, vertex):
        if len(self.vertex_list) == 0:
            return None
        else:
            for i in range(len(self.vertex_list)):
                if self.vertex_list[i] == vertex:
                    idx = i
                    return idx
            return None

    def insert_vertex(self, vertex):
        if self.get_vertex_id(vertex) is None:
            if len(self.vertex_list)==0:
                self.graph[0].append(0)
                self.vertex_list.append(vertex)
            else:
                for row in self.graph:
                    row.append(0)
                self.vertex_list.append(vertex)
                self.graph.append([0] * len(self.vertex_list))

    def insert_edge(self, vertex1, vertex2, edge=1):
        vertex1_id = self.get_vertex_id(vertex1)
        vertex2_id = self.get_vertex_id(vertex2)

        if vertex2_id is None:
            self.insert_vertex(vertex2)
            vertex2_id = self.get_vertex_id(vertex2)

        self.graph[vertex1_id][vertex2_id] = edge
        self.graph[vertex2_id][vertex1_id] = edge

    def delete_vertex(self, vertex):
        vertex_id = self.get_vertex_id(vertex)
        self.graph.pop(vertex_id)
        self.vertex_list.pop(vertex_id)

        for i in range(len(self.vertex_list)):
            self.graph[i][vertex_id] = 0

    def delete_edge(self, vertex1, vertex2):
        vertex1_id = self.get_vertex_id(vertex1)
        vertex2_id = self.get_vertex_id(vertex2)

        self.graph[vertex1_id][vertex2_id] = 0
        self.graph[vertex2_id][vertex1_id] = 0

    def vertices(self):
        return [i for i in range(len(self.vertex_list))]

    def neighbours(self, vertex_id):
        wynik = []
        for i in range(len(self.vertex_list)):
            if self.graph[vertex_id][i] != 0:
                edge = self.graph[vertex_id][i]
                wynik.append((i, edge))

        return wynik
