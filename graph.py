# This is Markov Chain
import random

# define the graph in terms of vertices

class Vertex:

    def __init__(self, value): # value will be the word
        self.value = value
        self.adjacent = {} #keep track of vertices
        self.neighbors = []
        self.neighbors_weights = []

    def add_edge_to(self, vertex, weight= 0):
        self.adjacent[vertex] = weight

    def increment_edge(self, vertex):
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1

    def get_probability_map(self):
        for (vertex, weight) in self.adjacent.items():
            self.neighbors.append(vertex)
            self.neighbors_weights.append(weight)

    def next_word(self,):
# put in graph
        return random.choices(self.neighbors, weights=self.neighbors_weights)[0]

class Graph:

    def __init__(self):
        self.vertices = {}

    def get_vertex_values(self):
        # what are the values of all the vertices, or all words
        return set(self.vertices.keys())

    def add_vertex(self, value):
        self.vertices[value] = Vertex(value)

    def get_vertex(self, value):

        # value isn't in graph? add it!

        if value not in self.vertices:
            self.add_vertex(value)

        return self.vertices[value]  # get vertex object

    def get_next_word(self, current_vertex):
        return self.vertices[current_vertex.value].next_word()

    def generate_probability_mappings(self):
        for vertex in self.vertices.values():
            vertex.get_probability_map()



