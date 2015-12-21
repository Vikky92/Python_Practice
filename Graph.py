""" A Python Class
A simple Python graph class, demonstrating the essential 
facts and functionalities of graphs.
"""

class Graph(object): #declaring the class 
    def __init__(self, graph_dict={}):
        """ initializes a graph object """
        self.__graph_dict = graph_dict   #defining the graph

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())  #vertices of the nodes

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges() #calling the generate_edge function

    def add_vertex(self, vertex):  #adding the node and edges shall be a list
        """ If the vertex "vertex" is not in 
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = [] #empty list

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        edge = set(edge) #we make a set out of the two vertices
        
        (vertex1, vertex2) = tuple(edge)
        
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2) #appending the vertex co
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        """ A static method generating the edges of the 
            graph "graph". Edges are represented as sets 
            with one (a loop back to the vertex) or two 
            vertices 
        """
        edges = [] #list for the edges
        for vertex in self.__graph_dict: 
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res


if __name__ == "__main__":

    g = { "a" : ["d"],
          "b" : ["c"],
          "c" : ["b", "c", "d", "e"],
          "d" : ["a", "c"],
          "e" : ["c"],
          "f" : []
        }


    graph = Graph(g)

    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

    print("Add vertex:")
    graph.add_vertex("z")

    print("Vertices of graph:")
    print(graph.vertices())
 
    print("Add an edge:") 
    x=raw_input("Enter the first vertex ")
    y=raw_input("Enter the second vertex ")
    graph.add_edge({x,y})
    
    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

    print('Adding an edge {"x","y"} with new vertices:')
    graph.add_edge({x,y})
    
    print("Vertices of graph:")
    print(graph.vertices())
    
    print("Edges of graph:")
    print(graph.edges())