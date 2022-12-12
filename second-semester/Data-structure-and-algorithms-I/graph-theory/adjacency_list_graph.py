from colorama import Fore, Back, Style


class Data():
    def __init__(self, data, description):
        self.data = data
        self.description = description

    def __str__(self):
        return f'{self.data} :: {self.description}'

    def seeData(self):
        return f'[ w={self.data}:{self.description} ]'


class Nodes_Lists():
    def __init__(self):
        self.services = []

    def add_service(self, node):
        self.services.append(node)

    def list_graph(self):
        text = "rutas: "
        for item in self.services:
            text += f' {item.seeData()} '
        return text


class Graph():
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        # List of vertices
        self.graph = [None] * self.num_vertices

    def add_edge(self, u, v, weight):
        try:
            if u != v:
                if self.graph[u] == None:
                    self.graph[u] = Nodes_Lists()
                self.graph[u].add_service(Data(weight, f"Service {v}"))
                if self.graph[v] == None:
                    self.graph[v] = Nodes_Lists()
                self.graph[v].add_service(Data(weight, f"Service {u}"))
            else:
                print(f'Error: {u} and {v} are the same services')
        except:
            print(f'Error: {u} or {v} is not a valid service')

    def remove_edge(self):
        pass

    def print_graph(self):
        for item in range(self.num_vertices):
            print(f'[{item}] -> ', end='')
            conecctions = self.graph[item]
            print("[", end='')
            if conecctions != None:
                print(conecctions.list_graph(), end='')
            print("]")


def prueba1():
    graph = Graph(6)
    graph.add_edge(0, 2, 4)
    graph.print_graph()


if __name__ == '__main__':
    prueba1()