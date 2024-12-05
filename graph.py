from edge import Edge

class Graph:
    #Список смежности
    def __init__(self):
        self.list = {}

    #функция для добавления ребра
    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.list:
            self.list[from_node] = []
        self.list[from_node].append(Edge(to_node, weight))
        
    #функция для получения соседей
    def get_neighbors(self, node):
        return self.list.get(node, [])
