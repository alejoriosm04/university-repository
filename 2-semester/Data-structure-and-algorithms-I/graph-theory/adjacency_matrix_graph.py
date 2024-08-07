from colorama import Fore, Back, Style


class Graph():
    def __init__(self, num_vertices):
        self.adjacency_matrix = []
        for i in range(num_vertices):
            self.adjacency_matrix.append([0 for j in range(num_vertices)])
            self.adjacency_matrix[i][i] = float("Inf")

    def add_edge(self, u, v, weight):
        try:
            self.adjacency_matrix[u][v] = weight
        except:
            print(f'Error: {u} or {v} is not a valid vertex')

    def remove_edge(self, u, v):
        try:
            self.adjacency_matrix[u][v] = 0
            self.adjacency_matrix[v][u] = 0
        except:
            print(f'Error: {u} or {v} is not a valid vertex')

    def print_graph(self):
        # Print header
        print("   ", end="")
        for item in range(len(self.adjacency_matrix)):
            print(f"  {item}  ", end="")
        print()

        # Print body
        i = 0
        for row in self.adjacency_matrix:
            print(f"{i}  ", end="")
            i += 1
            for relation in row:
                if relation == float("Inf"):
                    print(f" {Fore.WHITE}{Back.BLUE} ∞ {Style.RESET_ALL} ", end="")
                elif relation != 0:
                    print(f" {Fore.WHITE}{Back.RED} {relation} {Style.RESET_ALL} ", end="")
                else:
                    print(f" {Fore.WHITE}{Back.CYAN} {relation} {Style.RESET_ALL} ", end="")
            print()


def prueba1():
    graph = Graph(6)
    graph.add_edge(0,2,4)
    graph.add_edge(1,3,1)
    graph.print_graph()
    graph.remove_edge(1,3)
    graph.print_graph()


if __name__ == '__main__':
    prueba1()